from datetime import timedelta, datetime

from newslynx.lib import dates
from newslynx.sc import SousChef
from .common import share_counts


class ContentTimeseriesCounts(SousChef):

    """
    Fetch share counts for an organization's content items.
    """
    timeout = 1000

    def setup(self):
        max_age = self.options.get('max_age')
        if max_age:
            self.max_age = dates.now() - timedelta(days=max_age)
        else:
            self.max_age = datetime(1900, 1, 1)

    def run(self):
        """
        Count shares for content items.
        """
        # Count shares for all content items up to a max age.
        if not len(self.urls):
            for content_item in self.api.orgs.simple_content():
                created = dates.parse_iso(content_item['created'])
                if created < self.max_age:
                    continue
                url = content_item.get('url')
                if url:
                    data = share_counts(url)
                    data.pop('url', None)
                    data['content_item_id'] = content_item.get('id')
                    yield data

    def load(self, data):
        """
        Bulk load metrics.
        """
        status_resp = self.api.content.bulk_create_timeseries(list(data))
        return self.api.jobs.poll(**status_resp)


class Counts(SousChef):

    """
    Fetch share counts for an an arbitray list of urls.
    """

    def run(self):
        self.log.info('Fetching counts for {}'.format(self.options['urls']))
        urls = self.options.get('urls', [])
        if not isinstance(urls, list):
            urls = urls.split(',')
        for u in urls:
            d = share_counts(u)
            d['url'] = u
            yield d

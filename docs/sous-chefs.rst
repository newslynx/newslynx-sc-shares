
Sous Chefs
-------------
**newslynx-sc-shares** provides access to the following Sous Chefs

Timeseries Share Counts for Content Items
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Computes a timeseries of share counts for an organization's content
   items.
-  This Sous Chef runs the python module
   ``newslynx_sc_shares.ContentTimeseriesCounts``.
-  API Slug: ``share-counts-to-content-timeseries``

Usage
^^^^^

Standalone
''''''''''

Run this Sous Chef via the api, passing in arbitrary runtime options,
and stream it's output.

.. code:: shell

    $ newslynx api sous-chefs cook -d=newslynx_sc_shares/content_timeseries.yaml --passthrough **options

Run this Sous Chef via the api, and if applicable, send it's output to
bulkload.

.. code:: shell

    $ newslynx api sous-chefs cook -d=newslynx_sc_shares/content_timeseries.yaml **options

Do either of the above two, but pass in a recipe file

.. code:: shell

    $ newslynx api sous-chefs cook -d=recipe.yaml

Recipes
'''''''

Add this Sous Chef to your authenticated org

.. code:: shell

    $ newslynx api sous-chefs create -d=newslynx_sc_shares/content_timeseries.yaml

Create a Recipe with this Sous Chef with command line options.

.. code:: shell

    $ newslynx api recipes create sous_chef=share-counts-to-content-timeseries **options

Alternatively pass in a recipe file.

.. code:: shell

    $ newslynx api recipes create sous_chef=share-counts-to-content-timeseries --data=recipe.yaml

Save the outputted ``id`` of this recipe, and execute it via the API.
**NOTE** This will place the recipe in a task queue.

.. code:: shell

    $ newslynx api recipes cook id=<id>

Alternatively, run the Recipe, passing in arbitrary runtime options, and
stream it's output: **NOTE** Will not execute the SousChef's ``load``
method.

.. code:: shell

    $ newslynx api recipes cook id=<id> --passthrough **options

Development
'''''''''''

Pass runtime options to ``share-counts-to-content-timeseries`` and
stream output. **NOTE** Will not execute the SousChef's ``load`` method.

.. code:: shell

    $ newslynx sc-run newslynx_sc_shares/content_timeseries.yaml option=value1

Alternatively pass in a recipe file

.. code:: shell

    $ newslynx sc-run newslynx_sc_shares/content_timeseries.yaml --recipe=recipe.yaml

Options
^^^^^^^

In addition to default recipe options,
``share-counts-to-content-timeseries`` also accepts the following

-  ``days``

   -  The number of days past a content item's creation date after which
      we will stop computing these counts.

   -  Should be rendered with a ``number`` form.
   -  Accepts inputs of type:

      -  ``numeric``

   -  Defaults to ``30``

-  ``content_item_types``

   -  The content item types to calculate share counts for.

   -  Should be rendered with a ``checkbox`` form.
   -  Choose from:

      -  ``video``
      -  ``article``
      -  ``slideshow``
      -  ``interactive``
      -  ``podcast``
      -  ``all``

   -  Accepts inputs of type:

      -  ``string``

   -  Defaults to ``all``

Metrics
^^^^^^^

``share-counts-to-content-timeseries`` generates the following Metrics

-  ``facebook_shares``

   -  Display name: ``Facebook Shares``

   -  Type: ``cumulative``

   -  Content Levels:

      -  ``timeseries``
      -  ``summary``
      -  ``comparison``

   -  Org Levels:

      -  ``timeseries``
      -  ``summary``

-  ``facebook_likes``

   -  Display name: ``Facebook Likes``

   -  Type: ``cumulative``

   -  Content Levels:

      -  ``timeseries``
      -  ``summary``
      -  ``comparison``

   -  Org Levels:

      -  ``timeseries``
      -  ``summary``

-  ``facebook_comments``

   -  Display name: ``Facebook Comments``

   -  Type: ``cumulative``

   -  Content Levels:

      -  ``timeseries``
      -  ``summary``
      -  ``comparison``

   -  Org Levels:

      -  ``timeseries``
      -  ``summary``

-  ``linkedin_shares``

   -  Display name: ``LinkedIn Shares``

   -  Type: ``cumulative``

   -  Content Levels:

      -  ``timeseries``
      -  ``summary``
      -  ``comparison``

   -  Org Levels:

      -  ``timeseries``
      -  ``summary``

-  ``pinterest_shares``

   -  Display name: ``Pinterest Shares``

   -  Type: ``cumulative``

   -  Content Levels:

      -  ``timeseries``
      -  ``summary``
      -  ``comparison``

   -  Org Levels:

      -  ``timeseries``
      -  ``summary``

-  ``reddit_upvotes``

   -  Display name: ``Reddit UpVotes``

   -  Type: ``cumulative``

   -  Content Levels:

      -  ``timeseries``
      -  ``summary``
      -  ``comparison``

   -  Org Levels:

      -  ``timeseries``
      -  ``summary``

-  ``reddit_downvotes``

   -  Display name: ``Reddit DownVotes``

   -  Type: ``cumulative``

   -  Content Levels:

      -  ``timeseries``
      -  ``summary``
      -  ``comparison``

   -  Org Levels:

      -  ``timeseries``
      -  ``summary``

-  ``twitter_shares``

   -  Display name: ``Twitter Shares``

   -  Type: ``cumulative``

   -  Content Levels:

      -  ``timeseries``
      -  ``summary``
      -  ``comparison``

   -  Org Levels:

      -  ``timeseries``
      -  ``summary``

-  ``googleplus_shares``

   -  Display name: ``Google Plus Shares``

   -  Type: ``cumulative``

   -  Content Levels:

      -  ``timeseries``
      -  ``summary``
      -  ``comparison``

   -  Org Levels:

      -  ``timeseries``
      -  ``summary``



Share counts for arbitrary urls.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Accepts a list of urls and returns their share counts.
-  This Sous Chef runs the python module ``newslynx_sc_shares.Counts``.
-  API Slug: ``share-counts-for-urls``

Usage
^^^^^

Standalone
''''''''''

Run this Sous Chef via the api, passing in arbitrary runtime options,
and stream it's output.

.. code:: shell

    $ newslynx api sous-chefs cook -d=newslynx_sc_shares/count.yaml --passthrough **options

Run this Sous Chef via the api, and if applicable, send it's output to
bulkload.

.. code:: shell

    $ newslynx api sous-chefs cook -d=newslynx_sc_shares/count.yaml **options

Do either of the above two, but pass in a recipe file

.. code:: shell

    $ newslynx api sous-chefs cook -d=recipe.yaml

Recipes
'''''''

Add this Sous Chef to your authenticated org

.. code:: shell

    $ newslynx api sous-chefs create -d=newslynx_sc_shares/count.yaml

Create a Recipe with this Sous Chef with command line options.

.. code:: shell

    $ newslynx api recipes create sous_chef=share-counts-for-urls **options

Alternatively pass in a recipe file.

.. code:: shell

    $ newslynx api recipes create sous_chef=share-counts-for-urls --data=recipe.yaml

Save the outputted ``id`` of this recipe, and execute it via the API.
**NOTE** This will place the recipe in a task queue.

.. code:: shell

    $ newslynx api recipes cook id=<id>

Alternatively, run the Recipe, passing in arbitrary runtime options, and
stream it's output: **NOTE** Will not execute the SousChef's ``load``
method.

.. code:: shell

    $ newslynx api recipes cook id=<id> --passthrough **options

Development
'''''''''''

Pass runtime options to ``share-counts-for-urls`` and stream output.
**NOTE** Will not execute the SousChef's ``load`` method.

.. code:: shell

    $ newslynx sc-run newslynx_sc_shares/count.yaml option=value1

Alternatively pass in a recipe file

.. code:: shell

    $ newslynx sc-run newslynx_sc_shares/count.yaml --recipe=recipe.yaml

Options
^^^^^^^

In addition to default recipe options, ``share-counts-for-urls`` also
accepts the following

-  ``urls``

   -  The number of days past a content item's creation date after which
      we will stop computing these counts.

   -  **Required**
   -  Should be rendered with a ``text`` form.
   -  Accepts inputs of type:

      -  ``string``

-  ``sources``

   -  The sources to gather share counts from.

   -  Should be rendered with a ``checkbox`` form.
   -  Choose from:

      -  ``twitter``
      -  ``facebookfql``
      -  ``reddit``
      -  ``linkedin``
      -  ``facebook``
      -  ``pinterest``
      -  ``googleplus``
      -  ``all``

   -  Accepts inputs of type:

      -  ``string``

   -  Defaults to ``all``




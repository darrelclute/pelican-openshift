====================
Pelican on OpenShift
====================

This is a base repository you can utilize to host your Pelican based site on
OpenShift.  With this setup you do not have to worry about building your site
locally and then pushing it up, you simply push to OpenShift and your site will
build there.

Deploy a Python cartridge to your OpenShift account and you can utilize this as
the template of building out your content.

.. code-block:: bash
    
    rhc app create -a pelican -t http://cartreflect-claytondev.rhcloud.com/github/gsterjov/openshift-advanced-python-cartridge

Add this upstream repo

.. code-block:: bash
    
    cd pelican
    git remote add upstream -m master https://github.com/darrelclute/pelican-openshift.git
    git pull -s recursive -X theirs upstream master

The build script is setup so that you will pull the theme you are using via Git
instead of maintaining it with your OpenShift repository.  To change themes
edit the 'git clone' lines in .openshift/action_hooks/build.

All other configuration data is stored in the conf directory, this includes
Apache configuration and Pelican configuration.

The data directory is the expected location for all of your content, place your
Markdown or reStructuredText sources here.

If you are utilizing any of the pelican plugins add the appropriate plugins to
your pelicanconf.py

Once you complete your customization you can push this up.

.. code-block:: bash
    
    git push



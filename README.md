coddy-sitetools
===============

Tools that i used for develop sites, like - blog, cms, twitter aggregation, open social and other cool stuff :)
Work in progress. I planed make some stable version in future.
Some docs in russian in ...


## About this project.

I want to bring together the components that I use at work.
Here's a list:
* coddy-site : application that keep everything working together
* coddy-blog : i think this is a blog app

will be done soon:
* coddy-shop
* coddy-catalog

I add implementations for some popular apps.

There are things that i just plan to add in the future:
* authority - user profiles and authorisation tools
* imaginary - tool that i used for work with images
* userpic - app for generate and add logo for users
* links - links aggregator
* twitter - twitter ;)


## Installation.

For work you will need:
* Python 2.7
* Django (latest)
* django-south
* django-treebeard
* django-debug-toolbar
* django-crispy_forms

* django-taggit - https://github.com/alex/django-taggit.git
* django-taggit-templatetags - https://github.com/feuervogel/django-taggit-templatetags.git

You can install it like pip install -r project-directory/requirements/dev.txt

For user profile work you may need to edit this
<pre><code>
CUSTOM_USER_MODEL = 'users_app.users.ConsumerProfile'
AUTH_PROFILE_MODULE = 'users_app.users.ConsumerProfile'
AUTHENTICATION_BACKENDS = [
    'user_app.users.ConsumerBackend',
    'django.contrib.auth.backends.ModelBackend',
]
</code></pre>

End edit login url
`LOGIN_URL = '/you-site/login/'`
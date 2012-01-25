Django newsletter
=================

Django newsletter is simple Django application for sending newsletter and managing subscriptions.

Installation
------------
- clone project to some empty folder
- copy newsletter folder from cloned project to your Django project
- copy templates/newsletter folder from cloned project to your Django project and customize files to your needs. You need also newsletter_base.html from templates/.
- look sat ettings.py (in cloned project) for variables EMAIL_FROM, EMAIL_HOST, EMAIL_SUBJECT_PREFIX, SITE_NAME, SUBSCRIBE_URL, UNSUBSCRIBE_URL; copy them to your settings and configure them to your needs
- add 'newsletter' to INSTALLED_APPS
- look at urls.py (in cloned projec) for url examples for newsletter subscription, ... Copy to yours urls.py and configure them to your needs.
- configure ADMINS in yours project settings.py
- python manage.py syncdb

Info
----
You send newsletter in Django admin by selecting created newsletter and 'Send newsletter' in Action select box (then Go).

If you run Django project in DEBUG mode, it will send newsletter only to ADMINS.

You like this little script, you find it useful or want new feature? 
----------------------------------------
You can donate a bitcoin or few on:
1WF6hQj5eJuR5drSaPCFKoqz2Z7GAzDnq

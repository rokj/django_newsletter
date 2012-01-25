# -*- coding: utf-8 -*-
import os

DEBUG = True
TEMPLATE_DEBUG = True

ADMINS = (
    ('', ''),
)

SEND_BROKEN_LINK_EMAILS = True
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'django_newsletter', # Or path to database file if using sqlite3.
        'USER': '', # Not used with sqlite3.
        'PASSWORD': '', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Ljubljana'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

ugettext = lambda s: s

LANGUAGES = (
  ('sl', ugettext('Slovenian')),
  ('en', ugettext('English')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

if DEBUG == True:
    SITE_URL = 'http://127.0.0.1:8000'
else:
    SITE_URL = 'http://www.your-site.net'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
if DEBUG == True:
    MEDIA_ROOT = '/django_newsletter/static/'
else:
    MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
if DEBUG == True:
    MEDIA_URL = 'http://127.0.0.1:8000/static/'
else:
    MEDIA_URL = 'http://www.your-site.net/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
if DEBUG == True:
    ADMIN_MEDIA_PREFIX = '/static/admin/'
else:
    ADMIN_MEDIA_PREFIX = 'http://www.your-site.net/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'CHANGE_IT'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'django_newsletter.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\', '/'),
    os.path.join(os.path.dirname(__file__), 'templates/posts').replace('\\', '/')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    # 'django.contrib.comments',
    'newsletter',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n"
)

EMAIL_FROM = 'Email From <email_from@internet.net>'
EMAIL_HOST = '1.2.3.4'
EMAIL_SUBJECT_PREFIX = 'Email subject prefix -'
SITE_NAME = 'Site name'
SUBSCRIBE_URL = "%s/newsletter/subscribe/key=%s"
UNSUBSCRIBE_URL = "%s/newsletter/unsubscribe/key=%s"


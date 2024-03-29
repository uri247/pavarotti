"""Django settings for pavarotti project.
"""
import os
#BASEDIR = os.path.abspath(os.path.dirname(__file__)) + os.sep
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
                            
DATABASES = None

if( os.getenv('SERVER_SOFTWARE','').startswith('Google App Engine') or
    os.getenv('SETTINGS_MODE') == 'prod'):
    #We are on google, or want to work with google database
    DATABASES = { 'default': {
        'ENGINE': 'google.appengine.ext.django.backends.rdbms',
        'INSTANCE': 'london.org.il:database:data',
        'NAME': 'pavarotti_db',
    } }
elif( os.getenv('COMPUTERNAME') == 'DT1' ):
    #I'm in my home, use the mysql server. First get the password
    from maipai import secrets
    password = secrets.query('cut', 'maipai', 'password')
    DATABASES = { 'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pavarotti',
        'USER': 'root',
        'PASSWORD': password,
        'HOST': 'precise',
    } }
else:
    #use sqlite
    DATABASES = { 'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'c:\\local\\data\\pavarotti.sqlite',                              
    } }


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
my_static_dir = os.path.abspath( os.path.join( PROJECT_PATH, '..', 'static' ) )
if( os.path.sep != '/' ):
    my_static_dir = my_static_dir.replace( os.path.sep, '/' )
                               

STATIC_ROOT = my_static_dir

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'y=kpmbdvd9*h_(^u3_axw9+h8dp@ycs(48+v*ax$vl+lq82ygm'

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
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pavarotti.urls'
#ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'pavarotti.wsgi.application'


my_tmpl_dir = os.path.abspath( os.path.join( PROJECT_PATH, '..', 'templates' ) )
if( os.path.sep != '/' ):
    my_tmpl_dir = my_tmpl_dir.replace( os.path.sep, '/' )
                               

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #"c:/uri/pp/pavarotti/templates"
    my_tmpl_dir,
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'faves',
    'django.contrib.admin',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

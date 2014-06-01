from __future__  import unicode_literals

from django.conf.global_settings import TEST_RUNNER


SECRET_KEY = 'not-anymore'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'polymodels',
]

if not TEST_RUNNER.endswith('DiscoverRunner'):
    # Use a byte string to prevent 1.4.x from raising at import time.
    TEST_RUNNER = b'discover_runner.DiscoverRunner'
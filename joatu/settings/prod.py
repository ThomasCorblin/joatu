from joatu.settings.base import *
DEBUG = False
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )
try:
    from tutorial.settings.local import *
except:
    pass

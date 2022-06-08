from .base import *
from decouple import config


SECRET_KEY = 'django-insecure-uni%#e+87cz0cuf+z5*eb!@k$zfu-*m0f*t2ca^y_*wgn@f(p8'


DEBUG = False

ALLOWED_HOSTS = ['*']



STATICFILES_DIRS = [

    'weebs/static'

]

MEDIA_URL = '/media/'



STATIC_ROOT = 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



django_heroku.settings(locals())

AWS_ACCESS_KEY_ID =  config('AWS_ACCESS_KEY_ID')    

AWS_SECRET_ACCESS_KEY =  config('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DEFAULT_FILE_STORAGE = 'myblog.storage_backends.MediaStorage'
from deajodido.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-3eh!c!w_&@pn))c^nrmq*cy(#48orq%+4sj#vw6l_z9b&obu&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['138.197.223.47', 'dejodido.com']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'deajodido',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Google's Keys
GMAPS_API_KEY = 'AIzaSyAbXCwLfYYs3Hyb8XXvxm5-wzvRNm2JI3Y'
GMAPS_API_KEY_JS= 'AIzaSyC3EcXKhyPwcWgVlPAzDGplTa00HkKD0KQ'

#SocialAUTH's Keys
SOCIAL_AUTH_FACEBOOK_KEY = '805766712952383'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'd7b13e308d24be4726f0c81721259a97'  # App Secret
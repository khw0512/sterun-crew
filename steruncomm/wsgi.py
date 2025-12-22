import os

from django.core.wsgi import get_wsgi_application

# prod로 실행하도록 수정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.prod')

application = get_wsgi_application()
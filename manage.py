import os
import sys

from dotenv import load_dotenv # 추가

def main():
    
    # .env 파일 로드
    load_dotenv() # 추가
    
    """Run administrative tasks."""
    # getenv 함수를 통해 환경변수 값을 가져오고 서버를 실행하도록 변경
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv('DJANGO_SETTINGS_MODULE', 'config.settings'))
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
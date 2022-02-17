import os;

from rest_framework import status

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'microdomains.settings')
import django; django.setup()

from django.test import TestCase


class MainPageAPIViewTestCase(TestCase):

    def test_main_page_get(self):
        # 인천 테스트
        request = self.client.get(
            path="http://localhost:8000/ui/main/?latitude=37.4239727&longitude=126.6543867"
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_200_OK)

        # 부산 테스트
        request = self.client.get(
            path="http://localhost:8000/ui/main/?latitude=35.1769654&longitude=129.1033877"
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_200_OK)
        
        # 파라미터 잘못보냄
        request = self.client.get(
            path="http://localhost:8000/ui/main/?latude=35.1769654&longide=129.1033877"
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_400_BAD_REQUEST)
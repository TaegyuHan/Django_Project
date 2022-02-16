import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'microdomains.settings')
import django; django.setup()

from django.test import TestCase


class UserTestCase(TestCase):
    def setUp(self) -> None:
        os.environ.get("DJANGO_SETTINGS_MODULE")
        pass

    def test_user_join_create_post(self):
        """ 회원가입  테스트 """
        json_data = {
			"firebase_uid": "tiVRbcLxEKPcmsjhGZm0pRnAsxg6",
			"google_id": "test@email.com",
			"google_profile_image": "https://image/url",
			"google_name": "test_google_name",
			"app_name": "test_app_name",
			"latitude": 41.40338,
			"longitude": 2.17403
		}
        request = self.client.post(
            path="http://localhost:8000/user/join",
            data=json_data,
            format="json"
        )
        print(request.data)
        self.assertEqual(request.status_code, 201)

    def test_user_delete_post(self):
        """ 회원 삭제 테스트 """

        # 존재 하지 않는 테스트
        json_data = {
            "firebase_uid": "tiVRbcLxEKPcmsjhGZm0pRnAsxg4"
        }
        request = self.client.post(
            path="http://localhost:8000/user/login",
            data=json_data,
            format="json"
        )
        print(request.data)
        self.assertEqual(request.status_code, 404)

        # 존재 해서 삭제
        json_data = {
            "firebase_uid": "tiVRbcLxEKPcmsjhGZm0pRnAsxg5"
        }
        request = self.client.post(
            path="http://localhost:8000/user/login",
            data=json_data,
            format="json"
        )
        print(request.data)
        self.assertEqual(request.status_code, 204)

    def test_user_login_post(self):
        """ 로그인 테스트 """
        # 없는 회원 확인
        json_data = {
            "firebase_uid": "tiVRbcLxEKPcmsjhGZm0pRnAsxg4"
        }
        request = self.client.post(
            path="http://localhost:8000/user/login",
            data=json_data,
            format="json"
        )
        print(request.data)
        self.assertEqual(request.status_code, 404)

        # 존재하는 회원 확인
        json_data = {
            "firebase_uid": "tiVRbcLxEKPcmsjhGZm0pRnAsxg5"
        }
        request = self.client.post(
            path="http://localhost:8000/user/login",
            data=json_data,
            format="json"
        )
        print(request.data)
        self.assertEqual(request.status_code, 200)
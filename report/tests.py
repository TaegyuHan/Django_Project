import os;

from rest_framework import status

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'microdomains.settings')
import django; django.setup()

from django.test import TestCase


class UserTestCase(TestCase):
    def setUp(self) -> None:
        os.environ.get("DJANGO_SETTINGS_MODULE")
        pass

    def test_create_category_post(self):
        # 성공 테스트
        json_data = {
            "content": "broken"
		}
        request = self.client.post(
            path="http://localhost:8000/report/category/",
            data=json_data,
            content_type='application/json'
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_201_CREATED)

        # 실패 테스트
        json_data = {
            "content_test": "broken"
        }
        request = self.client.post(
            path="http://localhost:8000/report/category/",
            data=json_data,
            content_type='application/json'
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_400_BAD_REQUEST)


    def test_category_delete(self):
        """ 삭제 테스트 """
        # 삭제 실패
        request = self.client.delete(
            path="http://localhost:8000/report/category/1",
            content_type='application/json'
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_404_NOT_FOUND)

        # 삭제 성공
        request = self.client.delete(
            path="http://localhost:8000/report/category/2",
            content_type='application/json'
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_204_NO_CONTENT)


    def test_report_get(self):
        request = self.client.get(
            path="http://localhost:8000/report/"
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_200_OK)

    def test_report_post(self):
        # 실패 테스트
        json_data = {
            "title": "post test",
            "explanation": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "latitude": 41.40338,
            "longitude": 2.17403,
            "recommendation": 0,
            "solved": 0,
            "category": 2
        }
        request = self.client.post(
            path="http://localhost:8000/report/",
            data=json_data,
            content_type='application/json'
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_400_BAD_REQUEST)

        # 성공 테스트
        json_data = {
            "title": "post test",
            "explanation": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "latitude": 41.40338,
            "longitude": 2.17403,
            "recommendation": 0,
            "solved": 0,
            "user": "tiVRbcLxEKPcmsjhGZm0pRnAsxg6",
            "category": 2
        }
        request = self.client.post(
            path="http://localhost:8000/report/",
            data=json_data,
            content_type='application/json'
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_201_CREATED)

    def test_report_detail_get(self):
        id = 1 # report 번호

        # 성공 테스트
        request = self.client.get(
            path=f"https://localhost:8000/report/{id}/"
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_200_OK)

    def test_report_detail_put(self):
        id = 1  # report 번호

        # 성공 테스트
        json_data = {
            "id": 1,
            "title": "post test3",
            "explanation": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "latitude": 41.40338,
            "longitude": 2.17403,
            "recommendation": 0,
            "solved": 0,
            "user": "tiVRbcLxEKPcmsjhGZm0pRnAsxg6",
            "category": 2
        }
        request = self.client.put(
            path=f"https://localhost:8000/report/{id}/",
            data=json_data,
            content_type='application/json'
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_200_OK)

        # 다른사람이 수정 시도 테스트
        json_data = {
            "id": 1,
            "title": "post test3",
            "explanation": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "latitude": 41.40338,
            "longitude": 2.17403,
            "recommendation": 0,
            "solved": 0,
            "user": "tiVRbcLxEKPcmsjhGZm0pRnAsxg7",
            "category": 2
        }
        request = self.client.put(
            path=f"https://localhost:8000/report/{id}/",
            data=json_data,
            content_type='application/json'
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_400_BAD_REQUEST)

    def test_report_detail_delete(self):
        # 삭제 테스트
        id = 211  # report 번호
        request = self.client.delete(
            path=f"https://localhost:8000/report/{id}/"
        )
        print(request.data)

        self.assertEqual(request.status_code,
                         status.HTTP_204_NO_CONTENT)


    def test_report_recommendation_get(self):
        # 성공 테스트
        request = self.client.get(
            path="https://localhost:8000/report/recommendation/"
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_200_OK)


    def test_report_recommendation_post(self):
        # 존재하지 않는 report 추천
        json_data = {
            "user": "tiVRbcLxEKPcmsjhGZm0pRnAsxg6",
            "report": 2
        }
        request = self.client.post(
            path="https://localhost:8000/report/recommendation/",
            data=json_data,
            content_type='application/json'
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_400_BAD_REQUEST)

        # 이미 추천함
        json_data = {
            "user": "tiVRbcLxEKPcmsjhGZm0pRnAsxg6",
            "report": 3
        }
        request = self.client.post(
            path="https://localhost:8000/report/recommendation/",
            data=json_data,
            content_type='application/json'
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_200_OK)

        # 추천 성공
        json_data = {
            "user": "tiVRbcLxEKPcmsjhGZm0pRnAsxg6",
            "report": 1
        }
        request = self.client.post(
            path="http://localhost:8000/report/recommendation/",
            data=json_data,
            content_type='application/json'
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_201_CREATED)

    def test_comment_get(self):
        request = self.client.get(
            path="https://localhost:8000/report/comment/"
        )
        print(request.data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)


    def test_comment_post(self):
        json_data = {
            "content": "comment test2",
            "user": "tiVRbcLxEKPcmsjhGZm0pRnAsxg6",
            "report": 3
        }
        request = self.client.post(
            path="https://localhost:8000/report/comment/",
            data=json_data,
            content_type='application/json'
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_201_CREATED)

    def test_comment_detail_get(self):
        id = 1
        request = self.client.get(
            path=f"https://localhost:8000/report/comment/{id}/"
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_200_OK)

    def test_comment_detail_put(self):
        id = 5

        ## 성공 테스트
        json_data = {
            "content": "comment put test",
            "user": "tiVRbcLxEKPcmsjhGZm0pRnAsxg6",
            "report": 3
        }
        request = self.client.put(
            path=f"https://localhost:8000/report/comment/{id}/",
            data=json_data,
            content_type='application/json'
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_200_OK)

        # userid 가 다른경우 실패
        json_data = {
            "content": "comment put test",
            "user": "tiVRbcLxEKPcmsjhGZm0pRnAsxg7",
            "report": 3
        }
        request = self.client.put(
            path=f"https://localhost:8000/report/comment/{id}/",
            data=json_data,
            content_type='application/json'
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_400_BAD_REQUEST)

    def test_comment_detail_delete(self):
        id = 5
        request = self.client.delete(
            path=f"https://localhost:8000/report/comment/{id}/"
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_204_NO_CONTENT)

class ReportDetailCommentsAPIViewTestCase(TestCase):

    def test_get(self):
        id = 11
        request = self.client.get(
            path=f"https://localhost:8000/report/{id}/comments/"
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_200_OK)


class ReportDetailImageAPIViewTestCase(TestCase):

    def test_get(self):
        id = 24
        request = self.client.get(
            path=f"https://localhost:8000/report/{id}/images/"
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_200_OK)


class ReportDetailSolvedImageAPIViewTestCase(TestCase):

    def test_get(self):
        id = 24
        request = self.client.get(
            path=f"https://localhost:8000/report/{id}/images/"
        )
        print(request.data)
        self.assertEqual(request.status_code,
                         status.HTTP_200_OK)
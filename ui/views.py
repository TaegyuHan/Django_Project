from django.db import connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from report.models import Report
from report.serializers import ReportSerializer
from haversine import haversine

from sql_utils.query_pretty import print_sql


class NearReportAPIView(APIView):
    """ 메인 페이지 API

        - GET : 10km 이내인 게시물들을 추천 수 내림차순으로 정렬
            parameter:
                latitude: 위도
                longitude: 경도
    """
    def get(self, request):
        # 위도 1도 차이: 약 111.195km
        # 경도 1도 차이: 약 88.804km
        
        # 거리 차이 필터
        km = 10

        try:
            tmp = 0.2 #도
            latitude = float(request.GET["latitude"])
            bot_latitude, top_latitude = latitude - tmp, latitude + tmp

            tmp = 0.8 #도
            longitude = float(request.GET["longitude"])
            bot_longitude, top_longitude = longitude - tmp, longitude + tmp

            models = Report.objects.filter(
                # 위도 필터
                latitude__gte=bot_latitude,
                latitude__lte=top_latitude,
                # 경도 필터
                longitude__gte=bot_longitude,
                longitude__lte=top_longitude
            ).order_by("recommendation")

            print_sql(models)

            filter_model = []
            for model in models:
                distance = haversine(
                    (latitude, longitude), # 현재 위치
                    (model.latitude, model.longitude) # 상대 위치
                )
                # 거리 필터
                if distance <= km:
                    filter_model.append(model)

            serializer = ReportSerializer(filter_model, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except KeyError: # 위도 경도 입력 안한 에러
            response_data = {
                "content": "Please enter the latitude and longitude."
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            print()

        except KeyError: # 위도 경도 입력 안한 에러
            response_data = {
                "content": "Please enter the latitude and longitude."
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class NearReportListAPIView(APIView):

    def get(self, request):
        # 위도 1도 차이: 약 111.195km
        # 경도 1도 차이: 약 88.804km

        # 거리 차이 필터
        km = 10

        try:
            tmp = 0.2  # 도
            latitude = float(request.GET["latitude"])
            bot_latitude, top_latitude = latitude - tmp, latitude + tmp

            tmp = 0.8  # 도
            longitude = float(request.GET["longitude"])
            bot_longitude, top_longitude = longitude - tmp, longitude + tmp

            with connection.cursor() as cursor:
                cursor.callproc('SP_GET_REPORT_LIST', [
                    bot_latitude,
                    top_latitude,
                    bot_longitude,
                    top_longitude
                ])
                data = cursor.fetchall()

                col_name = [
                    "id",
                    "title",
                    "explanation",
                    "solved_title",
                    "solved_explanation",
                    "category_id",
                    "content",
                    "image",
                    "user_id",
                    "latitude",
                    "longitude",
                    "recommendation",
                    "solved",
                    "app_name",
                    "google_profile_image",
                    "created_at",
                    "updated_at",
                    "solved_created_at",
                    "solved_updated_at",
                ]

                json_data = []
                for row in data:
                    json_data.append(dict(zip(col_name, row)))

            return Response(json_data, status=status.HTTP_200_OK)

        except KeyError:  # 위도 경도 입력 안한 에러
            response_data = {
                "content": "Please enter the latitude and longitude."
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class NearSolvedReportListAPIView(APIView):

    def get(self, request):
        # 위도 1도 차이: 약 111.195km
        # 경도 1도 차이: 약 88.804km

        # 거리 차이 필터
        km = 10

        try:
            tmp = 0.2  # 도
            latitude = float(request.GET["latitude"])
            bot_latitude, top_latitude = latitude - tmp, latitude + tmp

            tmp = 0.8  # 도
            longitude = float(request.GET["longitude"])
            bot_longitude, top_longitude = longitude - tmp, longitude + tmp

            with connection.cursor() as cursor:
                cursor.callproc('SP_GET_SOLVED_REPORT_LIST', [
                    bot_latitude,
                    top_latitude,
                    bot_longitude,
                    top_longitude
                ])
                data = cursor.fetchall()

                col_name = [
                    "id",
                    "title",
                    "explanation",
                    "solved_title",
                    "solved_explanation",
                    "category_id",
                    "content",
                    "image",
                    "user_id",
                    "latitude",
                    "longitude",
                    "recommendation",
                    "solved",
                    "app_name",
                    "google_profile_image",
                    "created_at",
                    "updated_at",
                    "solved_created_at",
                    "solved_updated_at",
                ]

                json_data = []
                for row in data:
                    json_data.append(dict(zip(col_name, row)))

            return Response(json_data, status=status.HTTP_200_OK)

        except KeyError:  # 위도 경도 입력 안한 에러
            response_data = {
                "content": "Please enter the latitude and longitude."
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class NearReportListAllAPIView(APIView):

    def get(self, request):
        # 위도 1도 차이: 약 111.195km
        # 경도 1도 차이: 약 88.804km

        # 거리 차이 필터
        km = 10

        try:
            tmp = 0.2  # 도
            latitude = float(request.GET["latitude"])
            bot_latitude, top_latitude = latitude - tmp, latitude + tmp

            tmp = 0.8  # 도
            longitude = float(request.GET["longitude"])
            bot_longitude, top_longitude = longitude - tmp, longitude + tmp

            with connection.cursor() as cursor:
                cursor.callproc('SP_GET_MY_REPORT_UNION', [
                    bot_latitude,
                    top_latitude,
                    bot_longitude,
                    top_longitude
                ])
                data = cursor.fetchall()

                col_name = [
                    "id",
                    "title",
                    "explanation",
                    "solved_title",
                    "solved_explanation",
                    "category_id",
                    "content",
                    "image",
                    "user_id",
                    "latitude",
                    "longitude",
                    "recommendation",
                    "solved",
                    "app_name",
                    "google_profile_image",
                    "created_at",
                    "updated_at",
                    "solved_created_at",
                    "solved_updated_at",
                ]

                json_data = []
                for row in data:
                    json_data.append(dict(zip(col_name, row)))

            return Response(json_data, status=status.HTTP_200_OK)

        except KeyError:  # 위도 경도 입력 안한 에러
            response_data = {
                "content": "Please enter the latitude and longitude."
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class MyReportListAPIView(APIView):

    def get(self, request):
        try:

            with connection.cursor() as cursor:
                cursor.callproc("SP_GET_MY_REPORT", (request.GET["uid"],))
                data = cursor.fetchall()

            col_name = [
                "id",
                "title",
                "explanation",
                "solved_title",
                "solved_explanation",
                "category_id",
                "content",
                "image",
                "user_id",
                "latitude",
                "longitude",
                "recommendation",
                "solved",
                "app_name",
                "google_profile_image",
                "created_at",
                "updated_at",
                "solved_created_at",
                "solved_updated_at"
            ]

            json_data = []
            for row in data:
                json_data.append(dict(zip(col_name, row)))

            return Response(json_data, status=status.HTTP_200_OK)

        except KeyError:
            response_data = {
                "content": "Please enter the uid parameter."
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
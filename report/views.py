from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.db import connection
from user.models import  User
from .models import (
    Category, Report,
    ReportRecommendation, Comment,
    ReportImage, ReportSolvedImage
)
from .serializers import (
    CategorySerializer, CommentSerializer,
    ReportSerializer, ReportRecommendationSerializer,
    ReportImageSerializer, ReportSolvedImageSerializer
)

class CategoryAPIView(APIView):
    """ 카테고리

        - GET : 카테고리 리스트 확인
        - POST : 카테고리 생성
    """

    def get(self, request):
        model = Category.objects.all()
        serializer = CategorySerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):
    """ 카테고리 디테일

        - GET : 선택한 카테고리 확인
        - PUT : 카테고리 수정
        - POST : 카테고리 생성
        - DELETE : 카테고리 삭제
    """

    def _get_object(self, id):
        try:
            return Category.objects.get(id=id)

        except Category.DoesNotExist:
            return status.HTTP_404_NOT_FOUND

    def _doesnt_exist(self):
        response_data = {
            "content": "It doesn't exist."
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        model = self._get_object(id)
        if model == status.HTTP_404_NOT_FOUND:
            return self._doesnt_exist()

        serializer = CategorySerializer(model)
        return Response(serializer.data)

    def put(self, request, id):
        model = self._get_object(id)
        if model == status.HTTP_404_NOT_FOUND:
            return self._doesnt_exist()

        serializer = CategorySerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        model = self._get_object(id)
        if model == status.HTTP_404_NOT_FOUND:
            return self._doesnt_exist()

        # model.delete()
        response_data = {
            "content": "Deleted successfully."
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)


class ReportAPIView(APIView):
    """ 보고서

        - GET : 보고서 리스트 확인
        - POST : 보고서 생성
    """

    def get(self, request):
        model = Report.objects.all()
        serializer = ReportSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReportSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReportDetailAPIView(APIView):
    """ 보고서 디테일

        - GET : 선택한 보고서 확인
        - PUT : 보고서 수정
        - DELETE : 보고서 삭제
    """

    def _get_object(self, id):
        try:
            return Report.objects.get(id=id)

        except Report.DoesNotExist:
            return status.HTTP_404_NOT_FOUND

    def _get_objects(self, model, report_id):
        try:
            return model.objects.get(report_id=report_id)

        except model.DoesNotExist:
            return status.HTTP_404_NOT_FOUND

    def _doesnt_exist(self):
        """ 존재 하지 않는 호출 """
        response_data = {
            "content": "It doesn't exist."
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    def _different_exist(self, request_user_id, model_user_id):
        """ userid가 다른경우 """
        response_data = {
            "content": "The UID is different.",
            'report_user': model_user_id,
            'request_user': request_user_id
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        with connection.cursor() as cursor:
            cursor.callproc('SP_GET_REPORT_DETAIL', [id])
            data = cursor.fetchall()

        col_name = [
            "id",
            "title",
            "explanation",
            "latitude",
            "longitude",
            "recommendation",
            "solved",
            "created_at",
            "updated_at",
            "user",
            "google_profile_image",
            "app_name",
            "category"
        ]

        try:
            json_data = dict(zip(col_name, data[0]))
        except IndexError: # report 존재 안할 경우
            response_data = {
                "content": "The report does not exist."
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        return Response(json_data, status=status.HTTP_200_OK)

    def put(self, request, id):
        model = self._get_object(id)

        # id 가 존재하지 않는경우
        if model == status.HTTP_404_NOT_FOUND:
            return self._doesnt_exist()

        # 회원이 등록한 report가 아닌경우
        if request.data["user"] != model.user.firebase_uid:
            return self._different_exist(model_user_id=model.user.firebase_uid,
                                         request_user_id=request.data["user"])
        # 수정 성공
        serializer = ReportSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        model = self._get_object(id)

        # id 가 존재하지 않는경우
        if model == status.HTTP_404_NOT_FOUND:
            return self._doesnt_exist()

        # 댓글 삭제
        comment_data = self._get_objects(model=Comment, report_id=id)
        if comment_data != status.HTTP_404_NOT_FOUND:
            comment_data.delete()

        # 이미지 삭제
        reprot_image_data = self._get_objects(model=ReportImage, report_id=id)
        if reprot_image_data != status.HTTP_404_NOT_FOUND:
            reprot_image_data.delete()

        # 해결 이미지 삭제
        report_solved_image_data = self._get_objects(model=ReportSolvedImage, report_id=id)
        if report_solved_image_data != status.HTTP_404_NOT_FOUND:
            report_solved_image_data.delete()

        # 추천 삭제
        report_recommendation_data = self._get_objects(model=ReportRecommendation, report_id=id)
        if report_recommendation_data != status.HTTP_404_NOT_FOUND:
            report_recommendation_data.delete()

        # 삭제
        model.delete()

        response_data = {
            "content": "Deleted successfully."
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)


class ReportDetailCommentsAPIView(APIView):
    """ 보고서 디테일 댓글

        - GET : 디테일 댓글 리스트
    """

    def get(self, request, id):
        with connection.cursor() as cursor:
            cursor.callproc('SP_GET_REPORT_COMMENTS', [id])
            data = cursor.fetchall()

        col_name = [
            "id",
            "content",
            "created_at",
            "updated_at",
            "firebase_uid",
            "google_profile_image",
            "app_name"
        ]

        json_data = []
        for row in data:
            json_data.append(dict(zip(col_name, row)))

        return Response(json_data, status=status.HTTP_200_OK)


class ReportDetailImageAPIView(APIView):
    """ 보고서 디테일 이미지

        - GET : 디테일 이미지 리스트
    """

    def get(self, request, id):
        model = ReportImage.objects.filter(report=id)
        serializer = ReportImageSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReportDetailSolvedImageAPIView(APIView):
    """ 보고서 디테일 해결 이미지

        - GET : 디테일 해결 이미지 리스트
    """

    def get(self, request, id):
        model = ReportSolvedImage.objects.filter(report=id)
        serializer = ReportSolvedImageSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReportRecommendationAPIView(APIView):
    """ 추천

        - GET : 추천 리스트 확인
        - POST : 추천 생성
    """
    def _get_report_object(self, id):
        try:
            return Report.objects.get(id=id)

        except Report.DoesNotExist:
            return status.HTTP_404_NOT_FOUND

    def get(self, request):
        model = ReportRecommendation.objects.all()
        serializer = ReportRecommendationSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        model = ReportRecommendation.objects.filter(
            user=request.data["user"],
            report_id=request.data["report"]
        )

        if not model: # 기존에 추천 안함
            # report 존재 안함
            model = self._get_report_object(id=request.data["report"])
            if model == status.HTTP_404_NOT_FOUND:
                response_data = {
                    "content": "The report does not exist."
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

            # 추천 성공
            serializer = ReportRecommendationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                model.recommendation += 1
                model.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # 기존에 추천 함
        response_data = {
            "content": "I already recommended it."
        }
        return Response(response_data, status=status.HTTP_200_OK)


class CommentAPIView(APIView):
    """ 댓글

        - GET : 댓글 리스트 확인
        - POST : 댓글 생성
    """

    def get(self, request):
        model = Comment.objects.all()
        serializer = CommentSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailAPIView(APIView):
    """ 댓글 디테일

        - GET : 선택한 댓글 확인
        - PUT : 댓글 수정
        - DELETE : 댓글 삭제
    """

    def get_object(self, id):
        try:
            return Comment.objects.get(id=id)

        except Comment.DoesNotExist:
            return status.HTTP_404_NOT_FOUND

    def _doesnt_exist(self):
        response_data = {
            "content": "It doesn't exist."
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    def _different_exist(self, request_user_id, model_user_id):
        """ userid가 다른경우 """
        response_data = {
            "content": "The UID is different.",
            'report_user': model_user_id,
            'request_user': request_user_id
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        model = self.get_object(id)
        if model == status.HTTP_404_NOT_FOUND:
            return self._doesnt_exist()

        serializer = CommentSerializer(model)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        model = self.get_object(id)

        # 존재 안하는 경우
        if model == status.HTTP_404_NOT_FOUND:
            return self._doesnt_exist()

        # 회원이 등록한 comment가 아닌경우
        if request.data["user"] != model.user.firebase_uid:
            return self._different_exist(model_user_id=model.user.firebase_uid,
                                         request_user_id=request.data["user"])

        serializer = CommentSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        model = self.get_object(id)
        if model == status.HTTP_404_NOT_FOUND:
            return self._doesnt_exist()

        model.delete()
        response_data = {
            "content": "Deleted successfully."
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)


class ReportImageviewset(ModelViewSet):
   queryset = ReportImage.objects.all()
   serializer_class = ReportImageSerializer


class ReportSolvedviewset(ModelViewSet):
   queryset = ReportSolvedImage.objects.all()
   serializer_class = ReportSolvedImageSerializer
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer


class UserJoinAPIView(APIView):
    """ 회원가입 기능

        - POST : 회원 가입
    """

    def post(self, request):

        try:
            # 데이터 검색 or 생성
            model, created = User.objects.get_or_create(
                firebase_uid=request.data["firebase_uid"],
                defaults={
                    "google_id": request.data["google_id"],
                    "google_profile_image": request.data["google_profile_image"],
                    "google_name": request.data["google_name"],
                    "app_name": request.data["app_name"],
                    "latitude": request.data["latitude"],
                    "longitude": request.data["longitude"],
                    "address": request.data["address"],
                    "updated_at": request.data["updated_at"]
                }
            )

            if not created: # 기존에 존재하는 회원 데이터 업데이트
                model.google_id = request.data["google_id"]
                model.google_profile_image = request.data["google_profile_image"]
                model.google_name = request.data["google_name"]
                model.app_name = request.data["app_name"]
                model.latitude = request.data["latitude"]
                model.longitude = request.data["longitude"]
                model.address = request.data["address"]
                model.updated_at = request.data["updated_at"]
            model.save()

            response_data = {
                "user_info": {
                    "firebase_uid": model.firebase_uid,
                    "google_id": model.google_id,
                    "google_profile_image": model.google_profile_image,
                    "google_name": model.google_name,
                    "app_name": model.app_name,
                    "latitude": model.latitude,
                    "longitude": model.longitude,
                    "address": model.address,
                    "created_at": model.created_at,
                    "updated_at": model.updated_at,
                }
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        except KeyError as e:
            error = {
                "error": "Please add the perfect data.",
                "except": "KeyError"
            }
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        except AttributeError as e:
            error = {
                "error": "Please add the perfect data.",
                "except": "AttributeError"
            }
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteAPIView(APIView):
    """ 회원 삭제 기능

        - POST : 삭제
    """

    def get_token_object(self, id):
        try:
            return Token.objects.get(user_id=id)

        except Token.DoesNotExist:
            return status.HTTP_404_NOT_FOUND

    def get_user_object(self, id):
        try:
            return User.objects.get(firebase_uid=id)

        except User.DoesNotExist:
            return status.HTTP_404_NOT_FOUND

    def post(self, request):

        token = self.get_token_object(id=request.data["firebase_uid"])
        if token != 404:
            token.delete()

        user = self.get_user_object(id=request.data["firebase_uid"])
        if user != 404:
            user.delete()

        if token == 404 or user == 404:
            response_data = {
                "user_info": request.data["firebase_uid"],
                "content": "It doesn't exist."
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        response_data = {
            "user_info": request.data["firebase_uid"],
            "content": "Deleted successfully!!"
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)


class UserLoginAPIView(APIView):
    """ 회원 로그인

        - POST : 로그인
    """

    def get_user_object(self, id):
        try:
            return User.objects.get(firebase_uid=id)

        except User.DoesNotExist:
            return status.HTTP_404_NOT_FOUND

    def post(self, request):

        user = self.get_user_object(id=request.data["firebase_uid"])

        if user == 404:
            response_data = {
                "content": "It doesn't exist."
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        user_serializer = UserSerializer(user)

        response_data = {
            "user_info": user_serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)
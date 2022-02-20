from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer, TokenSerializer


class UserJoinAPIView(APIView):
    """ 회원가입 기능

        - POST : 회원 가입
    """

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            token_data = Token.objects.create(user_id=request.data['firebase_uid']) # 토큰 생성

            response_data = {
                "user_info": serializer.data,
                "token": token_data.key
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

        user = self.get_user_object(id=request.data["firebase_uid"])
        user_serializer = UserSerializer(user)

        if user == 404:
            response_data = {
                "content": "It doesn't exist."
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        response_data = {
            "user_info": user_serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)
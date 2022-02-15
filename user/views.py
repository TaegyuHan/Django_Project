from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer


class UserAPIView(APIView):
    """ 회원가입

        - POST : - 회원 가입
                 - 회원 토큰 받기
    """

    def user_already_exists_check(self, firebase_uid):
        """ User 존재 확인 """
        try:
            user_data = User.objects.get(firebase_uid=firebase_uid)
            return user_data, status.HTTP_200_OK

        except User.DoesNotExist:
            return {"No Data 404"}, status.HTTP_404_NOT_FOUND

    def token_already_exists_check(self, token):
        """ Token 존재 확인 """
        try:
            token_data = Token.objects.get(key=token)
            return token_data, status.HTTP_200_OK

        except Token.DoesNotExist:
            return {"No Data 404"}, status.HTTP_404_NOT_FOUND

    def post(self, request):
        """ 회원가입 및 토큰 받기 데이터 받기 """

        UID_LEN = 28 # UID 길이 확인
        input_len = len(request.data['firebase_uid'])
        serializer = UserSerializer(data=request.data)

        # 기존에 있는 회원인지 확인
        data, status_code = self.user_already_exists_check(request.data['firebase_uid'])
        if status_code == status.HTTP_200_OK: # 기존에 있는 회원
            token_data = Token.objects.get(user_id=request.data['firebase_uid'])
            response_data = {
                "firebase_uid": request.data['firebase_uid'],
                "token": token_data.key,
            }
            return Response(response_data, status=status.HTTP_200_OK)

        elif status_code == status.HTTP_404_NOT_FOUND: # 신규 회원
            if serializer.is_valid():
                if input_len != UID_LEN:
                    return Response(data={
                        "content": f"Set the uid length to 28, input length: {input_len}",
                        "input firebase_uid": f"{input_len}"
                    },
                    status=status.HTTP_400_BAD_REQUEST)

                serializer.save() # DB 저장
                token_data = Token.objects.create(user_id=request.data['firebase_uid']) # 토큰 생성
                response_data = {
                    "user": serializer.data,
                    "token": token_data.key,
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
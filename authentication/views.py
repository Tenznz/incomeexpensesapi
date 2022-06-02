import jwt
from django.contrib.sites.shortcuts import get_current_site
from jwt.algorithms import get_default_algorithms
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from incomeexpensesapi import settings
from .models import User
from .serializers import UserSerializer, LoginSerializer
from .utils import Util
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request=request).domain
        relative_link = reverse(viewname='email-verify')
        abs_url = 'http//:' + current_site + relative_link + '?token=' + str(token)
        email_body = 'Hi,' + user.username + " Use below link to verify your email\ndomain: " + abs_url
        data = {'body': email_body, 'to': [user.email], 'subject': 'verify your email'}
        Util.send_email(data)
        return Response({
            'message': 'user created successfully',
            'data': user_data
        }, status=status.HTTP_201_CREATED)


class VerifyEmail(views.APIView):
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING), ], )
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=get_default_algorithms())
            user = User.objects.get(id=payload.get('user_id'))
            user.is_verified = True
            user.save()
            return Response({
                'message': 'activation successful'
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            'message': 'login successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

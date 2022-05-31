from django.contrib.sites.shortcuts import get_current_site
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer
from .utils import Util


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
            'data': user_data
        }, status=status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):
    def get(self, request):
        pass

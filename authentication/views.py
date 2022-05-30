from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import UserSerializer


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response({
            'data': user_data
        }, status=status.HTTP_201_CREATED)
    # def get(self,request):
    #     user=User.objects.get()
    #     serializer= self.serializer_class()
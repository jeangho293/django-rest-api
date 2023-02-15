from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from users.services import UserService
from users.serializers import UserSerializer


class UserView(APIView):
    _service = UserService
    _serializer = UserSerializer

    def get(self, request):
        data = self._service().list()
        response = self._serializer(data, many=True)
        return Response({"data": response.data})

    def post(self, request):
        # NOTE: Need Validator
        data = self._service().add(**request.data)
        return Response({"data": data}, status=201)

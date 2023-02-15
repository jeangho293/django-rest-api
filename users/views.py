from django.shortcuts import render

# Create your views here.
from users.models import User
from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# @csrf_exempt
# def users_service(request):
#     if request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#     if request.method == "GET":
#         user = User.manager.get(pk=1)
#         serializer = UserSerializer(user)
#         return JsonResponse(data={"data": serializer.data}, safe=False)


class UserList(APIView):
    def get(self, request):
        users = User.manager.get_user_list()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        return Response()

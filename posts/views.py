from rest_framework.views import APIView
from rest_framework.response import Response
from posts.services import PostService


# Create your views here.
class PostView(APIView):
    __service = PostService()

    def get(self, request):
        data = self.__service.list()
        return Response({"data": data})

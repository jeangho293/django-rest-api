from rest_framework.views import APIView
from rest_framework.response import Response
from pydantic import ValidationError
from users.validators import UserValidator
from users.services import UserService


# Create your views here.
class UserCreateView(APIView):
    _service = UserService()

    def post(self, request):
        try:
            UserValidator(**request.data)
            self._service.add(**request.data)
            return Response()
        except ValidationError as e:
            return Response({"error_message": e.errors()[0]["msg"]}, status=400)
        except ValueError as e:
            return Response({"error_message": e.args[0]}, status=400)

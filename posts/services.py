from posts.serializers import PostSerializer


class PostService:
    __serializer = PostSerializer

    def list(self):
        return self.__serializer().find_all()

# from django.http import Http404
# from django.shortcuts import render
#
# # Create your views here.
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from test_app.models import Blog
# from test_app.serializer import BlogSerializer
#
#
# class BlogList(APIView):
#     # blog list 보여줄때
#     def get(self, request):
#         blogs = Blog.objects.all()
#         # many=True : 여러개의 객체 serialization
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data)
#
#     # blog 글 작성할 때
#     def post(self, request):
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#
# class BlogDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Blog.objects.get(pk=pk)
#         except Blog.DoesNotExist:
#             raise Http404
#     # blog detail 보기
#     def get(self, request, pk, format=None):
#         blog = self.get_object(pk)
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)
#
#     # blog 수정하기
#     def put(self, request, pk, format=None):
#         blog = self.get_object(pk)
#         serializer = BlogSerializer(blog, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         blog = self.get_object(pk)
#         blog.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
#


from rest_framework import mixins, generics

from test_app.models import Blog
from test_app.serializer import BlogSerializer


class BlogList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BlogDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


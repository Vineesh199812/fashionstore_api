from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import blogs,users

#url: localhost:8000/posts/{post_id}
#method: post
#data: (postId:7, userId:5, "title":"Good Morning", "content":"Hello")
class PostView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"data":blogs})

    def post(self,request,*args,**kwargs):
        blog=request.data
        blogs.append(blog)
        return Response(data=blog)

#url : social/posts/{pid}
class PostDetailView(APIView):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        blog=[b for b in blogs if b["postId"]==pid].pop()
        return Response(data=blog)

#url:localhost:8000/posts?liked_by=2
#method:get

#request.query_params
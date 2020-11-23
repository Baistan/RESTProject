from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Blog.models import Post, Blog
from Blog.serializer import PostSerializer, BlogSerializer


@api_view(['POST'])
def blogCreate(request):
    if request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

@api_view(['GET','POST'])
def postView(request,pk):
    if request.method == 'GET':
        posts = Post.objects.filter(blog_id=pk)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        try:
            blog = Blog.objects.get(id=pk)
            post = Post(blog=blog)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


@api_view(['GET'])
def blogList(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def postList(request):
    post = Post.objects.all()
    serializer = PostSerializer(post,many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def blogUpdate(request,pk):
    if request.method == 'PUT':
        try:
            blog = Blog.objects.get(id=pk)
        except Blog.DoesNotExist:
            return Response({'SERVER RESPONSE':'PAGE NOT FOUND'},status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'SERVER RESPONSE':'Blog successfuly update'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def postUpdate(request,blog_id,post_id):
    if request.method == 'PUT':
        blog = Blog.objects.get(id=blog_id)
        post = Post(id=post_id,blog=blog)
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors)


@api_view(['DELETE'])
def blogDelete(request,pk):
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        return Response({'SERVER RESPONCE': 'page not found'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        blog.delete()
        return Response({'SERVER RESPONSE':'Blog successfuly deleted'},status=status.HTTP_200_OK)

@api_view(['DELETE'])
def postDelete(request,blog_id,post_id):
    if request.method == 'DELETE':
        blog = Blog.objects.get(id=blog_id)
        post = Post(id=post_id, blog=blog)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
 
from rest_framework.views import APIView
from django.http import Http404

from rest_framework import mixins
from rest_framework import generics

from django.contrib.auth.models import User
from snippets.serializers import UserSerializer

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics 

from rest_framework import permissions

from snippets.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	The viewset automatically provides 'list' and 'detail' actions.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
	"""
	This views automatically provides 'list' , 'create' , 'retrieve' ,
	'update' and 'destroy' actions.

	Additionally we also provide an extra 'highlight' action.
	"""

	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly , IsOwnerOrReadOnly)

	@action(detail=True , renderer_classes = [renderers.StaticHTMLRenderer])
	def highlight(self , request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def perform_create(self , serializer):
		serializer.save(owner = self.request.user) 
		
# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#     def perform_create(self, serializer):
#     	serializer.save(owner=self.request.user)

# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                       IsOwnerOrReadOnly,)


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'snippets': reverse('snippet-list', request=request, format=format)
#     })


# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer,)

#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)

# @csrf_exempt

# @api_view(['GET' , 'POST'])

# def snippet_list(request , format = None):
# 	"""
# 	List all code snippets , or create a new snippet
# 	"""
# 	if request.method == 'GET':
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets , many = True)
# 		return Response(serializer.data)
# 		#return JsonResponse(serializer.data, safe = False)

# 	elif request.method == 'POST':
# 		#data = JSONParser().parse(request)
# 		serializer = SnippetSerializer(data = request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data , status=status.HTTP_201_CREATED)
# 			#return JsonResponse(serializer.data , status = 201)
# 		return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
# 				# JsonResponse(serializer.errors, status = 400)

# # @csrf_exempt

# @api_view(['GET' , 'PUT' , 'DELETE' ])
# def snippet_detail(request, pk , format = None):
# 	"""
# 	 Retrieve , Update or delete a code snippet
# 	"""
# 	try:
# 		snippet = Snippet.objects.get(pk=pk)
# 	except Snippet.DoesNotExist:
# 		 return Response(status=status.HTTP_404_NOT_FOUND)
# 		# return HttpResponse(status=404)

# 	if request.method == 'GET':
# 		serializer = SnippetSerializer(snippet)	
# 		return Response(serializer.data)

# 		# JsonResponse(serializer.data)

# 	elif request.method == 'PUT':
# 		#data = JSONParser().parse(request)	
# 		serializer = SnippetSerializer(snippet, data =request.data)	
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)
	
# 	elif request.method == 'DELETE':
# 		snippet.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)
# 		# HttpResponse(status = 204)		



# class SnippetList(APIView):
# 	"""
# 	List all code snippets , or create a new snippet
# 	"""
# 	def get(self, request , format = None):
# 		#request.method == 'GET':
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets , many = True)
# 		return Response(serializer.data)
# 			#return JsonResponse(serializer.data, safe = False)

# 	def post(self , request, format=None):
# 		#data = JSONParser().parse(request)
# 		serializer = SnippetSerializer(data = request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data , status=status.HTTP_201_CREATED)
# 			#return JsonResponse(serializer.data , status = 201)
# 		return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
# 				# JsonResponse(serializer.errors, status = 400)

# # @csrf_exempt

# #@api_view(['GET' , 'PUT' , 'DELETE' ])
# class SnippetDetail(APIView):
# 	"""
# 	 Retrieve , Update or delete a code snippet
# 	"""
# 	# try:
# 	# 	snippet = Snippet.objects.get(pk=pk)
# 	# except Snippet.DoesNotExist:
# 	# 	 return Response(status=status.HTTP_404_NOT_FOUND)
# 	# 	# return HttpResponse(status=404)

# 	def get_object(self, pk):
# 		try:
# 			return Snippet.objects.get(pk=pk)
# 		except Snippet.DoesNotExist :
# 			raise Http404	

# 	def get(self, request , pk , format = None):
# 		snippet = self.get_object(pk)
# 		serializer = SnippetSerializer(snippet)	
# 		return Response(serializer.data)

# 		# JsonResponse(serializer.data)

# 	def put(self , request , pk , format = None):
# 		snippet = self.get_object(pk)
# 		#data = JSONParser().parse(request)	
# 		serializer = SnippetSerializer(snippet, data =request.data)	
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
	
# 	def delete(self, request , pk , format = None):
# 		snippet = self.get_object(pk)
# 		snippet.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)
# 		# HttpResponse(status = 204)		



# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)







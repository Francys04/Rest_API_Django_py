from django.shortcuts import render, redirect
# create first views
from django.http import JsonResponse

# create rest_api response
from rest_framework.decorators import api_view
from rest_framework.response import Response

# for admin
from .models import Advocate, Company
# serializer
from .serializers import AdvocateSerializer, CompanySerializer
# use Q method for search cahracteres or word in api by http://127.0.0.1:8000/advocates/?query=word_to_find
from django.db.models import Q

# create APIView base
from rest_framework.views import APIView

# Create your views here.

#       CRUD
# GET /advocates
# POST /advocates

# GET /advocates/:id
# for update PUT /advocates/:id
# DELETE /advocates/:id



# call endpoints
# add decorators -> functionality to function
@api_view(['GET'])
def endpoints(request):
    data=['/advocates', 'advocates/:username']
    return Response(data)


@api_view(['GET', 'POST'])
# another view
def advocate_list(request):
    # data = ['Alex', 'Max', 'John']
    
    # query, CRUD, Handles get request
    if request.method == 'GET':
        query = request.GET.get('query')
        if query == None:
            query = ''
        # if value contains  letterns of the original names
        # http://127.0.0.1:8000/advocates/?query=name_create_by_admin
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        # use serializer
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)

    # POST, handle with put json format to input new data in db with rest api
    if request.method == 'POST':

        advocate = Advocate.objects.create(
            username=request.data['username'],
            bio=request.data['bio']
        )
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer)



# API
# @api_view(['POST'])
# def add_advocate(request):
#     Advocate.objects.create(
#         username=request.data['username']
#     )
#     return Response('added')


# # update and delete and put
# @api_view(['GET', 'PUT', 'DELETE'])
# # access the domain od username
# def advocate_details(request, username):
#     advocate = Advocate.objects.get(username=username)
    
# # get
#     if request.method == 'GET':
#         # many=False return a single object
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)
    
# # put 
#     if request.method == 'PUT':
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']
        
#         advocate.save()
        
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer)
    
#     # Delete and rturn message thet was delete
#     if request.method == 'DELETE':
#         advocate.delete()
#         return Response('user was deleted')



#another example class based viws, put path in urls.py
class AdvocateDetail(APIView):
    def get_object(self, username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            raise JsonResponse('Advocate dosent exist')
        
        
    def get(self, request, username):
        advocate = self.get_object(username)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
    
    # request of put fun
    def put(self,request, username):
        advocate = self.get_object(username)
        
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
    # delete
    def delete(self, request, username):
        advocate = self.get_object(username)
        advocate.delete()
        return Response('user was deleted')
    
    
    
# Compony model
@api_view(['GET'])
def companies_list(request):
    companies = Company.objects.get()
    serializer = CompanySerializer(companies, many = False)
    return Response(serializer.data)
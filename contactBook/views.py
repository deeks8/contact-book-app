from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from .ApiV1_0 import ApiContact
from .cache import *

def paginate(request, data, strength):
    paginator = Paginator(data, strength)
    page = request['page']
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return data.object_list

def hash_key(key, key_prefix, version):
    new_key ='%s%s%s'%(key_prefix, version, key)
    if len(new_key) > 250:
        m = hashlib.md5()
        m.update(new_key)
        new_key = m.hexdigest()
    return new_key


class AddContact(APIView):


    '''
        :Author: Deeksha
        Add a new contact
        :param request: contains the parameter sent by the user
        :param format:
        :return: return message
        '''
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):
        returnData=ApiContact.addContact(self,request.data,format=None)
        if returnData == "Success":
            return Response(returnData, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(returnData, status=status.HTTP_400_BAD_REQUEST)

class EditContact(APIView):
    '''
        :Author: Deeksha
        Edit an existing contact
        :param request: contains the parameter sent by the user
        :param format:
        :return: return message
        '''
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):
        returnData=ApiContact.editContact(self,request.data,format=None)
        if returnData == "Success":
            return Response(returnData, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(returnData, status=status.HTTP_400_BAD_REQUEST)


class DeleteContact(APIView):

    '''
        :Author: Deeksha
        Delete contact
        :param request: contains the parameter sent by the user
        :param format:
        :return: return message
        '''
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):
        returnData=ApiContact.deleteContact(self,request.data,format=None)
        if returnData == "Success":
            return Response(returnData, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(returnData, status=status.HTTP_400_BAD_REQUEST)

class SearchContact(APIView):

    '''
        :Author: Deeksha
        Search contact by name or email
        :param request: contains the parameter sent by the user
        :param format:
        :return: return message
        '''
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):
        if "Name" in request.data:
            cache_service = CacheService(qs_type=str(request.data['Name']) )
        else:
            cache_service = CacheService(qs_type=str(request.data['EmailId']))
        event_queryset = cache_service.get_from_cache()
        if not event_queryset:
            event_queryset = ApiContact.searchContact(self,request.data,format=None)
            cache_service.set_to_cache(event_queryset)
        if event_queryset == "Error":
            # Useless to cache error request
            return Response(event_queryset, status=status.HTTP_400_BAD_REQUEST)
        else:
            returnData = paginate(request.data, event_queryset, 10)
            return Response(returnData, status=status.HTTP_202_ACCEPTED)


class SearchContactByName(APIView):

    '''
        :Author: Deeksha
        Search contact by name
        :param request: contains the parameter sent by the user
        :param format:
        :return: return message
        '''
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):
        cache_service = CacheService(qs_type=str(request.data['Name']))
        event_queryset = cache_service.get_from_cache()
        if not event_queryset:
            event_queryset = ApiContact.searchContact(self, request.data, format=None)
            cache_service.set_to_cache(event_queryset)
        if event_queryset == "Error":
            # Useless to cache error request
            return Response(event_queryset, status=status.HTTP_400_BAD_REQUEST)
        else:
            returnData = paginate(request.data, event_queryset, 10)
            return Response(returnData, status=status.HTTP_202_ACCEPTED)


class SearchContactByEmail(APIView):

    '''
        :Author: Deeksha
        Search contact by email
        :param request: contains the parameter sent by the user
        :param format:
        :return: return message
        '''
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):
        cache_service = CacheService(qs_type=str(request.data['EmailId']))
        event_queryset = cache_service.get_from_cache()
        if not event_queryset:
            event_queryset = ApiContact.searchContact(self, request.data, format=None)
            cache_service.set_to_cache(event_queryset)
        if event_queryset == "Error":
            # Useless to cache error request
            return Response(event_queryset, status=status.HTTP_400_BAD_REQUEST)
        else:
            returnData = paginate(request.data, event_queryset, 10)
            return Response(returnData, status=status.HTTP_202_ACCEPTED)






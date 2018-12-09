from ..models import *
from django.db.models import Q

def addContact(self,request,format=None):
    try:

        contactObj, created = Contact.objects.get_or_create(EmailId=request['EmailId'])
        if created:
            contactObj.Name = request['Name']
            contactObj.PhoneNumber = request['PhoneNumber']
            contactObj.save()
            return "Success"
        else:
            return "Email already exists"
    except Exception as e:
        print (e)
        return "Error"


def editContact(self,request,format=None):
    try:
        contactObj = Contact.objects.get(EmailId=request['EmailId'])
        if "Name" in request:
            contactObj.Name = request['Name']
        if "PhoneNumber" in request:
            contactObj.PhoneNumber = request['PhoneNumber']
        contactObj.save()
        return "Success"
    except Exception as e:
        return "Error"

def deleteContact(self,request,format=None):
    try:
        contactObj = Contact.objects.get(EmailId=request['EmailId'])
        contactObj.delete()
        return "Success"
    except Exception as e:
        return "Error"


def searchContactByName(self,request,format=None):
    try:
        returnData = []
        contactObj = Contact.objects.filter(Name__icontains=request['Name'])
        for each in contactObj:
            returnData.append({"Name":each.Name,"EmailId":each.EmailId,"PhoneNumber":each.PhoneNumber})
        return returnData
    except Exception as e:
        return "Error"


def searchContactByEmail(self,request,format=None):
    try:
        returnData = []
        contactObj = Contact.objects.filter(EmailId__icontains=request['EmailId'])
        for each in contactObj:
            returnData.append({"Name":each.Name,"EmailId":each.EmailId,"PhoneNumber":each.PhoneNumber})
        return returnData
    except Exception as e:
        return "Error"


def searchContact(self,request,format=None):
    try:
        returnData = []
        if "Name" in request:
            contactObj = Contact.objects.filter(Name__icontains=request['Name'])
        else:
            contactObj = Contact.objects.filter(EmailId__icontains=request['EmailId'])
        for each in contactObj:
            returnData.append({"Name":each.Name,"EmailId":each.EmailId,"PhoneNumber":each.PhoneNumber})
        return returnData
    except Exception as e:
        return "Error"


from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from base.models import Item
from django_portfolio.models import *
from .serializers import *


@api_view(['GET'])
def getSkillDetail(request):
    skillDetail = SkillDetail.objects.all()
    serializer = SkillDetailSerializer(skillDetail, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAdditionalSkills(request):
    additionalSkills = AdditionalSkills.objects.all()
    serializer = AdditionalSkillsSerializer(additionalSkills, many=True)
    return Response(serializer.data)


# @api_view(['POST'])
# def addItem(request):
#     serializer = ItemSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

from django.shortcuts import render
from aiogram import Bot, Dispatcher, executor, types
from .models import Proposal
from rest_framework.response import Response
from rest_framework.views import APIView
import json
import telegram
import requests
from .serializers import ProposalSerializers
from rest_framework import status



class APIBOT(APIView):
    def get(self, request):
        proposal = Proposal.objects.all().filter(status="WT")
        serializer = ProposalSerializers(proposal, many=True)
        quantity = proposal.count()
        print(f"Quantity of filtered proposals: {quantity}")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = ProposalSerializers(data=request.data)
        if serializer.is_valid():
            app = serializer.save()
            return Response({'app': serializer.data}, status=status.HTTP_201_CREATED)

        if not serializer.is_valid():
            print(serializer.data)
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
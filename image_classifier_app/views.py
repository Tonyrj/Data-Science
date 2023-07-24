from django.shortcuts import render

# Create your views here.
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from .models import UploadedImage
from .serializers import UploadedImageSerializer

class ImageUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request):
        file_serializer = UploadedImageSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            image_path = os.path.join(settings.MEDIA_ROOT, file_serializer.data['image'])
            #SPACE FOR CONNECTING TO THE MODEL AND GETTING THE RESULT
            result = 'MODEL RESULT'
            return Response({'result': result}, status=status.HTTP_200_OK)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

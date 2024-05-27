from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status as http_status



# class robotData(APIView):
#     def post(self, request):
#         serializer = roboSerializer(data=request.data)
#         try:
#             if serializer.is_valid():
#                 roboData = serializer.data['roboData']
#                 status = serializer.data['status']
#                 RoboData.objects.create(
#                     roboData=roboData,
#                     status=status
#                 )
#
#                 return JsonResponse({
#                     'status': 200,
#                     'message': 'Data create successfully',
#                 })
#             return JsonResponse({
#                 "status": 400,
#                 "message": serializer.errors
#             })
#         except Exception as e:
#             print(str(e))
#             return JsonResponse({
#                 'status': 400,
#                 'message': 'Something Went Wrong',
#                 'error': str(e)
#             })
#


class getrobotData(APIView):

    def get(self, request, status):
        try:
            # Create a new RoboData instance with the provided status
            new_data = RoboData.objects.create(status=status)

            # Convert the newly created object to a dictionary format
            new_data_dict = {
                'id': new_data.id,
                'status': new_data.status,
                'created_at': new_data.created_at
            }

            return Response({
                'status': 200,
                'message': 'Data created successfully',
                'new_data': new_data_dict
            })

        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'errors': str(e)
            })
class getrobotDataStatus(APIView):

    def get(self, request,status,id):
        try:
            data = list(RoboData.objects.filter(status=status,id=id).values())

            return Response({
                'status': 200,
                'data': data
            })

        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'errors': str(e)
            })




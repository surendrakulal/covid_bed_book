from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import BedListSerializer
from .models import BedList
from rest_framework import status
import json
from django.core.exceptions import ObjectDoesNotExist
from .filters import BedListFilter
from django_filters.utils import translate_validation
import requests


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])  
def bed_list(request):
    filterset = BedListFilter(request.GET, queryset=BedList.objects.all())
    if not filterset.is_valid():
         raise translate_validation(filterset.errors)
    serializer = BedListSerializer(filterset.qs, many=True)
    return JsonResponse({'bedlist': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def bed_booking(request):
    payload = json.loads(request.body)
    
    try:
        bedlist = BedList.objects.create(
            PatientName=payload["PatientName"],
            Contact_Number=payload["Contact_Number"],
            Gender=payload["Gender"],
            Patient_address=payload["Patient_address"],
            patient_critical_level=payload["patient_critical_level"],
            Pincode=payload["Pincode"],
            Hospital=payload["Hospital"],
            Timeslot=payload["Timeslot"]
        )
        serializer = BedListSerializer(bedlist)
        return JsonResponse({'bedlist': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def reschedule_book(request, bed_id):

    payload = json.loads(request.body)
    try:
        bed_item = BedList.objects.filter(id=bed_id)
        # returns 1 or 0
        bed_item.update(**payload)
        bedlist = BedList.objects.get(id=bed_id)
        serializer = BedListSerializer(bedlist)
        return JsonResponse({'bedlist': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def cancel_book(request, bed_id):
    try:
        bedlist = BedList.objects.get(id=bed_id)
        bedlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
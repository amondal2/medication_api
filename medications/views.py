from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import DatabaseError
from .models import Medication

class ListMedications(APIView):
    def get(self, request):
        ''' endpoint to list all medications '''
        medication_data = []
        queryset = Medication.objects.all()
        for medication in queryset:
            medication_data.append({
                'id': medication.pk,
                'name': medication.name
            })

        return Response(
            status=200,
            data=medication_data
        )

    def post(self, request):
        ''' endpoint to create a new medication '''
        medication_name = request.data.get('medication_name')
        if not medication_name:
            error_payload = {
                'error': 'no medication name provided'
            }
            return Response(
                status=400,
                data=error_payload
            )

        try:
            medication = Medication.objects.create(
                name=medication_name
            )
        except DatabaseError:
            error_payload = {
                'error': 'database error occurred'
            }
            return Response(
                status=400,
                data=error_payload
            )

        return Response(
            status=200,
            data= {
                'name': medication.name,
                'id': medication.pk
            }
        )
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import DatabaseError
from .models import Patient
from medications.models import Medication

class ListPatients(APIView):
    def get(self, request):
        ''' endpoint to list all patients '''
        patient_data = []
        queryset = Patient.objects.all()
        for patient in queryset:
            patient_data.append({
                'id': patient.pk,
                'name': patient.name
            })

        return Response(
            status=200,
            data=patient_data
        )

    def post(self, request):
        ''' endpoint to create a new patient '''
        patient_name = request.data.get('patient_name')
        if not patient_name:
            error_payload = {
                'error': 'no patient name provided'
            }
            return Response(
                status=400,
                data=error_payload
            )

        try:
            patient = Patient.objects.create(
                name=patient_name
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
                'name': patient.name,
                'id': patient.pk
            }
        )

class AddMedication(APIView):
    def post(self, request, pk=None):
        ''' endpoint to add a medication to a patient '''
        if not pk:
            error_payload = {
                'error': 'no patient id provided'
            }
            return Response(
                status=400,
                data=error_payload
            )

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
            medication = Medication.objects.get(
                name=medication_name
            )
            patient = Patient.objects.get(
                pk=pk
            )
        except (Medication.DoesNotExist, Patient.DoesNotExist) as e:
            error_payload = {
                'error': str(e)
            }
            return Response(
                status=400,
                data=error_payload
            )

        patient.medications.add(medication)
        patient.save()

        data = {
            'patient id': patient.pk,
            'medications': [
                med.name for med in patient.medications.all()
            ]
        }

        return Response(
            status=200,
            data=data
        )

class RemoveMedication(APIView):
    def post(self, request, pk=None):
        ''' endpoint to remove a medication from a patient '''
        if not pk:
            error_payload = {
                'error': 'no patient id provided'
            }
            return Response(
                status=400,
                data=error_payload
            )

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
            medication = Medication.objects.get(
                name=medication_name
            )
            patient = Patient.objects.get(
                pk=pk
            )
        except (Medication.DoesNotExist, Patient.DoesNotExist) as e:
            error_payload = {
                'error': str(e)
            }
            return Response(
                status=400,
                data=error_payload
            )

        patient.medications.remove(medication)
        patient.save()

        data = {
            'patient id': patient.pk,
            'medications': [
                med.name for med in patient.medications.all()
            ]
        }

        return Response(
            status=200,
            data=data
        )
from django.contrib import admin
from django.urls import path
from patients.views import ListPatients, AddMedication, RemoveMedication
from medications.views import ListMedications

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', ListPatients.as_view()),
    path('medications/', ListMedications.as_view()),
    path('patient/<int:pk>/add/', AddMedication.as_view()),
    path('patient/<int:pk>/remove/', RemoveMedication.as_view())
]

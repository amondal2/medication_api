# Medication Management API

## Database architecture

We have two models currently: Patient and Medication. Patient contains a name and age field. Medication only contains a name field and is a many-to-many relationship with the Patient model. We will use the sqlite db that comes pre-packaged with Python for now.

## Endpoints

The api exposes a few endpoints for both models.

1. GET /patients/ returns a JSON list of all patients' name and database id.
2. POST /patients/ creates a new patient in the database and returns its id.
This endpoint requires a JSON body with the patient name parameter:
{
    patient_name: agastya
}
3. GET /medications/ returns a JSON list of all medications' name and database id.
4. POST /medications/ creates a new medication in the database and returns its id.
This endpoint requires a JSON body with the medication name parameter:
{
    medication_name: advil
}
5. POST /patient/{id}/add/ associates a given medication with the patient, given the
patient's database id. It returns all medications associated with the given
patient after the association is complete. This endpoint requires a JSON body with the
medication name parameter, and returns a 400 response if either the medication or patient
are not found.
{
    medication_name: advil
}
6. POST /patient/{id}/remove/ removes a given medication for the patient, given the
patient's database id. It returns all medications associated with the given
patient after the removal is complete. This endpoint requires a JSON body with the
medication name parameter, and returns a 400 response if either the medication or patient
are not found.
{
    medication_name: advil
}

## Running Locally

I have set up a Makefile to run the API locally. To run, simply:
0. clone the directory locally: `git clone https://github.com/amondal2/medication_api.git`
1. run `make run` in the root  `wellframe_api` directory
2. the shell will print which localhost:port combination it's running on (usually localhost:8000). access this with the above endpoints to test the api.
define({ "api": [
  {
    "type": "post",
    "url": "/create/condition",
    "title": "Populate a FHIR Condition template with the supplied values",
    "name": "CreateCondition",
    "group": "Create",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Unique ID of this condition.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "codeSystem",
            "description": "<p>Code system used for this condition.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "code",
            "description": "<p>Code used for this condition.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "display",
            "description": "<p>Text associated with this condition.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "subjectReference",
            "description": "<p>The ID of the patient to whom this condition pertains.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "practitionerReference",
            "description": "<p>The ID of the practitioner who diagnosed this condition.</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./src/FHIR/create.py",
    "groupTitle": "Create"
  },
  {
    "type": "post",
    "url": "/create/dispense",
    "title": "Populate a FHIR MedicationDispense template with the supplied values",
    "name": "CreateDispense",
    "group": "Create",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Unique ID of this dispense of medication.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "medicationReference",
            "description": "<p>The ID of the medication involved in this dispense.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "subjectReference",
            "description": "<p>The ID of the patient that is taking this medication.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "practitionerReference",
            "description": "<p>The ID of the practitioner that prescribed this medication.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "organizationReference",
            "description": "<p>The ID of the organization the practitioner is associated with.</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./src/FHIR/create.py",
    "groupTitle": "Create"
  },
  {
    "type": "post",
    "url": "/create/medication",
    "title": "Populate a FHIR Medication template with the supplied values",
    "name": "CreateMedication",
    "group": "Create",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Unique ID of this medication.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "codeSystem",
            "description": "<p>Code system used for this medication.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "code",
            "description": "<p>Code used for this medication.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "display",
            "description": "<p>Text associated with this medication.</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./src/FHIR/create.py",
    "groupTitle": "Create"
  },
  {
    "type": "post",
    "url": "/create/organization",
    "title": "Populate a FHIR Organization template with the supplied values",
    "name": "CreateOrganization",
    "group": "Create",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Unique ID of this organization.</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./src/FHIR/create.py",
    "groupTitle": "Create"
  },
  {
    "type": "post",
    "url": "/create/patient",
    "title": "Populate a FHIR Patient template with the supplied values",
    "name": "CreatePatient",
    "group": "Create",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Unique ID of this patient.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "title",
            "description": "<p>Patient title.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "familyName",
            "description": "<p>Patient family name.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "givenName",
            "description": "<p>Patient given name.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "birthDate",
            "description": "<p>Patient date of birth.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "organizationReference",
            "description": "<p>ID of Organization with which the patient is registered.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "ethnicityCode",
            "description": "<p>Code used for patient ethnicity.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "ethnicityDisplay",
            "description": "<p>Text associated with patient ethnicity.</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./src/FHIR/create.py",
    "groupTitle": "Create"
  },
  {
    "type": "post",
    "url": "/create/practitioner",
    "title": "Populate a FHIR Practitioner template with the supplied values",
    "name": "CreatePractitioner",
    "group": "Create",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Unique ID of this practitioner.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "familyName",
            "description": "<p>Practitioner family name.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "givenName",
            "description": "<p>Practitioner given name.</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./src/FHIR/create.py",
    "groupTitle": "Create"
  }
] });

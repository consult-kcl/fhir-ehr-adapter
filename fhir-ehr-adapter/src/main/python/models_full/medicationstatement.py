#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.8.0.10521 (http://hl7.org/fhir/StructureDefinition/MedicationStatement) on 2018-01-16.
#  2018, SMART Health IT.


from . import domainresource

class MedicationStatement(domainresource.DomainResource):
    """ Record of medication being taken by a patient.
    
    A record of a medication that is being consumed by a patient.   A
    MedicationStatement may indicate that the patient may be taking the
    medication now, or has taken the medication in the past or will be taking
    the medication in the future.  The source of this information can be the
    patient, significant other (such as a family member or spouse), or a
    clinician.  A common scenario where this information is captured is during
    the history taking process during a patient visit or stay.   The medication
    information may come from e.g. the patient's memory, from a prescription
    bottle,  or from a list of medications the patient, clinician or other
    party maintains
    
    The primary difference between a medication statement and a medication
    administration is that the medication administration has complete
    administration information and is based on actual administration
    information from the person who administered the medication.  A medication
    statement is often, if not always, less specific.  There is no required
    date/time when the medication was administered, in fact we only know that a
    source has reported the patient is taking this medication, where details
    such as time, quantity, or rate or even medication product may be
    incomplete or missing or less precise.  As stated earlier, the medication
    statement information may come from the patient's memory, from a
    prescription bottle or from a list of medications the patient, clinician or
    other party maintains.  Medication administration is more formal and is not
    missing detailed information.
    """
    
    resource_type = "MedicationStatement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Type of medication usage.
        Type `str`. """
        
        self.dateAsserted = None
        """ When the statement was asserted?.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.derivedFrom = None
        """ Additional supporting information.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.dosage = None
        """ Details of how medication was taken.
        List of `DosageInstruction` items (represented as `dict` in JSON). """
        
        self.effectiveDateTime = None
        """ Over what period was medication consumed?.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ Over what period was medication consumed?.
        Type `Period` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.informationSource = None
        """ Person or organization that provided the information about the
        taking of this medication.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson, Organization` (represented as `dict` in JSON). """
        
        self.medicationCodeableConcept = None
        """ What medication was taken.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference = None
        """ What medication was taken.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
        
        self.notTaken = None
        """ y | n | unk.
        Type `str`. """
        
        self.note = None
        """ Further information about the statement.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.reasonForUseCodeableConcept = None
        """ Reason for why the medication is being/was taken.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonForUseReference = None
        """ Condition or observation that supports why the medication is
        being/was taken.
        List of `FHIRReference` items referencing `Condition, Observation` (represented as `dict` in JSON). """
        
        self.reasonNotTaken = None
        """ True if asserting medication was not given.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.status = None
        """ active | completed | entered-in-error | intended | stopped | on-
        hold.
        Type `str`. """
        
        self.subject = None
        """ Who is/was taking  the medication.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """
        
        super(MedicationStatement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationStatement, self).elementProperties()
        js.extend([
            ("category", "category", str, False, None, False),
            ("dateAsserted", "dateAsserted", fhirdate.FHIRDate, False, None, False),
            ("derivedFrom", "derivedFrom", fhirreference.FHIRReference, True, None, False),
            ("dosage", "dosage", dosageinstruction.DosageInstruction, True, None, False),
            ("effectiveDateTime", "effectiveDateTime", fhirdate.FHIRDate, False, "effective", False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("informationSource", "informationSource", fhirreference.FHIRReference, False, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("notTaken", "notTaken", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("reasonForUseCodeableConcept", "reasonForUseCodeableConcept", codeableconcept.CodeableConcept, True, None, False),
            ("reasonForUseReference", "reasonForUseReference", fhirreference.FHIRReference, True, None, False),
            ("reasonNotTaken", "reasonNotTaken", codeableconcept.CodeableConcept, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import dosageinstruction
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period

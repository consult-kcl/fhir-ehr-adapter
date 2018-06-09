#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.8.0.10521 (http://hl7.org/fhir/StructureDefinition/DeviceUseStatement) on 2018-01-16.
#  2018, SMART Health IT.


from . import domainresource

class DeviceUseStatement(domainresource.DomainResource):
    """ Record of use of a device.
    
    A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician.
    """
    
    resource_type = "DeviceUseStatement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.bodySite = None
        """ Target body site.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.device = None
        """ Reference to device used.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External identifier for this record.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indication = None
        """ Why device was used.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.notes = None
        """ Addition details (comments, instructions).
        List of `str` items. """
        
        self.recordedOn = None
        """ When statement was recorded.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.subject = None
        """ Patient using device.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.timingDateTime = None
        """ How often  the device was used.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingPeriod = None
        """ How often  the device was used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        """ How often  the device was used.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.whenUsed = None
        """ Period device was used.
        Type `Period` (represented as `dict` in JSON). """
        
        super(DeviceUseStatement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceUseStatement, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("indication", "indication", codeableconcept.CodeableConcept, True, None, False),
            ("notes", "notes", str, True, None, False),
            ("recordedOn", "recordedOn", fhirdate.FHIRDate, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("whenUsed", "whenUsed", period.Period, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import timing

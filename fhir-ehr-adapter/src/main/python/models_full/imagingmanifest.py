#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.8.0.10521 (http://hl7.org/fhir/StructureDefinition/ImagingManifest) on 2018-01-16.
#  2018, SMART Health IT.


from . import domainresource

class ImagingManifest(domainresource.DomainResource):
    """ Key Object Selection.
    
    A manifest of a set of DICOM Service-Object Pair Instances (SOP Instances).
    The referenced SOP Instances (images or other content) are for a single
    patient, and may be from one or more studies. The referenced SOP Instances
    may have been selected for a purpose, such as  conference, or consult.
    Reflecting a range of sharing purposes, typical ImagingManifest resources
    may include all SOP Instances in a study (perhaps for sharing through a
    Health Information Exchange); key images from multiple studies (for
    reference by a referring or treating physician); both a multi-frame
    ultrasound instance ("cine" video clip) and a set of measurements taken
    from that instance (for inclusion in a teaching file); and so on.
    """
    
    resource_type = "ImagingManifest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author = None
        """ Author (human or machine).
        Type `FHIRReference` referencing `Practitioner, Device, Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.authoringTime = None
        """ Time when the selection of instances was made.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Description text.
        Type `str`. """
        
        self.patient = None
        """ Patient of the selected objects.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.study = None
        """ Study identity of the selected instances.
        List of `ImagingManifestStudy` items (represented as `dict` in JSON). """
        
        self.title = None
        """ Reason for selection.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.uid = None
        """ SOP Instance UID.
        Type `str`. """
        
        super(ImagingManifest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingManifest, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("authoringTime", "authoringTime", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("study", "study", ImagingManifestStudy, True, None, True),
            ("title", "title", codeableconcept.CodeableConcept, False, None, True),
            ("uid", "uid", str, False, None, False),
        ])
        return js


from . import backboneelement

class ImagingManifestStudy(backboneelement.BackboneElement):
    """ Study identity of the selected instances.
    
    Study identity and locating information of the DICOM SOP instances in the
    selection.
    """
    
    resource_type = "ImagingManifestStudy"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.baseLocation = None
        """ Study access service endpoint.
        List of `ImagingManifestStudyBaseLocation` items (represented as `dict` in JSON). """
        
        self.imagingStudy = None
        """ Reference to ImagingStudy.
        Type `FHIRReference` referencing `ImagingStudy` (represented as `dict` in JSON). """
        
        self.series = None
        """ Series identity of the selected instances.
        List of `ImagingManifestStudySeries` items (represented as `dict` in JSON). """
        
        self.uid = None
        """ Study instance UID.
        Type `str`. """
        
        super(ImagingManifestStudy, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingManifestStudy, self).elementProperties()
        js.extend([
            ("baseLocation", "baseLocation", ImagingManifestStudyBaseLocation, True, None, False),
            ("imagingStudy", "imagingStudy", fhirreference.FHIRReference, False, None, False),
            ("series", "series", ImagingManifestStudySeries, True, None, True),
            ("uid", "uid", str, False, None, True),
        ])
        return js


class ImagingManifestStudyBaseLocation(backboneelement.BackboneElement):
    """ Study access service endpoint.
    
    Methods of accessing  (e.g., retrieving, viewing) the study.
    """
    
    resource_type = "ImagingManifestStudyBaseLocation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ WADO-RS | WADO-URI | IID.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.url = None
        """ Study access URL.
        Type `str`. """
        
        super(ImagingManifestStudyBaseLocation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingManifestStudyBaseLocation, self).elementProperties()
        js.extend([
            ("type", "type", coding.Coding, False, None, True),
            ("url", "url", str, False, None, True),
        ])
        return js


class ImagingManifestStudySeries(backboneelement.BackboneElement):
    """ Series identity of the selected instances.
    
    Series identity and locating information of the DICOM SOP instances in the
    selection.
    """
    
    resource_type = "ImagingManifestStudySeries"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.baseLocation = None
        """ Series access endpoint.
        List of `ImagingManifestStudySeriesBaseLocation` items (represented as `dict` in JSON). """
        
        self.instance = None
        """ The selected instance.
        List of `ImagingManifestStudySeriesInstance` items (represented as `dict` in JSON). """
        
        self.uid = None
        """ Series instance UID.
        Type `str`. """
        
        super(ImagingManifestStudySeries, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingManifestStudySeries, self).elementProperties()
        js.extend([
            ("baseLocation", "baseLocation", ImagingManifestStudySeriesBaseLocation, True, None, False),
            ("instance", "instance", ImagingManifestStudySeriesInstance, True, None, True),
            ("uid", "uid", str, False, None, True),
        ])
        return js


class ImagingManifestStudySeriesBaseLocation(backboneelement.BackboneElement):
    """ Series access endpoint.
    
    Methods of accessing (e.g. retrieving) the series.
    """
    
    resource_type = "ImagingManifestStudySeriesBaseLocation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ WADO-RS | WADO-URI | IID.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.url = None
        """ Series access URL.
        Type `str`. """
        
        super(ImagingManifestStudySeriesBaseLocation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingManifestStudySeriesBaseLocation, self).elementProperties()
        js.extend([
            ("type", "type", coding.Coding, False, None, True),
            ("url", "url", str, False, None, True),
        ])
        return js


class ImagingManifestStudySeriesInstance(backboneelement.BackboneElement):
    """ The selected instance.
    
    Identity and locating information of the selected DICOM SOP instances.
    """
    
    resource_type = "ImagingManifestStudySeriesInstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sopClass = None
        """ SOP class UID of instance.
        Type `str`. """
        
        self.uid = None
        """ Selected instance UID.
        Type `str`. """
        
        super(ImagingManifestStudySeriesInstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingManifestStudySeriesInstance, self).elementProperties()
        js.extend([
            ("sopClass", "sopClass", str, False, None, True),
            ("uid", "uid", str, False, None, True),
        ])
        return js


from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.8.0.10521 on 2018-01-16.
#  2018, SMART Health IT.


import os
import io
import unittest
import json
from . import endpoint
from .fhirdate import FHIRDate


class EndpointTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Endpoint", js["resourceType"])
        return endpoint.Endpoint(js)
    
    def testEndpoint1(self):
        inst = self.instantiate_from("endpoint-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Endpoint instance")
        self.implEndpoint1(inst)
        
        js = inst.as_json()
        self.assertEqual("Endpoint", js["resourceType"])
        inst2 = endpoint.Endpoint(js)
        self.implEndpoint1(inst2)
    
    def implEndpoint1(self, inst):
        self.assertEqual(inst.address, "http://fhir3.healthintersections.com.au/open/CarePlan")
        self.assertEqual(inst.connectionType.code, "hl7-fhir-rest")
        self.assertEqual(inst.connectionType.system, "http://hl7.org/fhir/endpoint-connection-type")
        self.assertEqual(inst.contact[0].system, "email")
        self.assertEqual(inst.contact[0].use, "work")
        self.assertEqual(inst.contact[0].value, "endpointmanager@example.org")
        self.assertEqual(inst.header[0], "bearer-code BASGS534s4")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://example.org/enpoint-identifier")
        self.assertEqual(inst.identifier[0].value, "epcp12")
        self.assertEqual(inst.name, "Health Intersections CarePlan Hub")
        self.assertEqual(inst.payloadMimeType[0], "application/fhir+xml")
        self.assertEqual(inst.payloadType[0].coding[0].code, "CarePlan")
        self.assertEqual(inst.payloadType[0].coding[0].system, "http://hl7.org/fhir/resource-types")
        self.assertEqual(inst.period.start.date, FHIRDate("2014-09-01").date)
        self.assertEqual(inst.period.start.as_json(), "2014-09-01")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Health Intersections CarePlan Hub<br/>CarePlans can be uploaded to/from this loccation</div>")
        self.assertEqual(inst.text.status, "generated")


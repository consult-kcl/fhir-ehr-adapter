#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.8.0.10521 on 2018-01-16.
#  2018, SMART Health IT.


import os
import io
import unittest
import json
from . import expansionprofile
from .fhirdate import FHIRDate


class ExpansionProfileTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ExpansionProfile", js["resourceType"])
        return expansionprofile.ExpansionProfile(js)
    
    def testExpansionProfile1(self):
        inst = self.instantiate_from("expansionprofile-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ExpansionProfile instance")
        self.implExpansionProfile1(inst)
        
        js = inst.as_json()
        self.assertEqual("ExpansionProfile", js["resourceType"])
        inst2 = expansionprofile.ExpansionProfile(js)
        self.implExpansionProfile1(inst2)
    
    def implExpansionProfile1(self, inst):
        self.assertTrue(inst.excludeNested)
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">[ Provide Rendering ]</div>")
        self.assertEqual(inst.text.status, "generated")


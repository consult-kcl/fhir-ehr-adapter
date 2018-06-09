#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.8.0.10521 on 2018-01-16.
#  2018, SMART Health IT.


import os
import io
import unittest
import json
from . import goal
from .fhirdate import FHIRDate


class GoalTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Goal", js["resourceType"])
        return goal.Goal(js)
    
    def testGoal1(self):
        inst = self.instantiate_from("goal-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Goal instance")
        self.implGoal1(inst)
        
        js = inst.as_json()
        self.assertEqual("Goal", js["resourceType"])
        inst2 = goal.Goal(js)
        self.implGoal1(inst2)
    
    def implGoal1(self, inst):
        self.assertEqual(inst.description.text, "Target weight is 160 to 180 lbs.")
        self.assertEqual(inst.extension[0].extension[0].url, "measure")
        self.assertEqual(inst.extension[0].extension[0].valueCodeableConcept.coding[0].code, "3141-9")
        self.assertEqual(inst.extension[0].extension[0].valueCodeableConcept.coding[0].display, "Weight Measured")
        self.assertEqual(inst.extension[0].extension[0].valueCodeableConcept.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.extension[0].extension[1].url, "detail")
        self.assertEqual(inst.extension[0].extension[1].valueRange.high.code, "[lb_av]")
        self.assertEqual(inst.extension[0].extension[1].valueRange.high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.extension[0].extension[1].valueRange.high.unit, "lbs")
        self.assertEqual(inst.extension[0].extension[1].valueRange.high.value, 180)
        self.assertEqual(inst.extension[0].extension[1].valueRange.low.code, "[lb_av]")
        self.assertEqual(inst.extension[0].extension[1].valueRange.low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.extension[0].extension[1].valueRange.low.unit, "lbs")
        self.assertEqual(inst.extension[0].extension[1].valueRange.low.value, 160)
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/goal-target")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.status, "in-progress")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p> A simple care goal for a patient to lose weight due to obesity.</p></div>")
        self.assertEqual(inst.text.status, "additional")


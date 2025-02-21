# Copyright (c) 2025, Arun Govind and Contributors
# See license.txt

import frappe
import unittest
from frappe.exceptions import ValidationError

class TestStudentEnrollment(unittest.TestCase):

    def setUp(self):
        """ Setup Test Data before running each test """
        self.student_enrollment = frappe.get_doc({
            "doctype": "Student Enrollment",
            "student_name": "John Doe",
            "email": "john.doe@example.com",
            "enrollment_date": frappe.utils.today(),
            "course": "Online",
            "status": "Draft"
        })

    def test_create_student_enrollment(self):
        """ Test Student Enrollment Creation """
        self.student_enrollment.insert()
        self.assertTrue(frappe.db.exists("Student Enrollment", self.student_enrollment.name))

    def test_mandatory_fields(self):
        """ Ensure mandatory fields are validated """
        enrollment = frappe.get_doc({"doctype": "Student Enrollment"})
        with self.assertRaises(ValidationError):
            enrollment.insert()

    def test_email_format_validation(self):
        """ Ensure invalid email raises validation error """
        self.student_enrollment.email = "invalid-email"
        with self.assertRaises(ValidationError):
            self.student_enrollment.insert()

    def test_future_enrollment_date(self):
        """ Ensure Enrollment Date cannot be in the future """
        self.student_enrollment.enrollment_date = frappe.utils.add_days(frappe.utils.today(), 10)
        with self.assertRaises(ValidationError):
            self.student_enrollment.insert()

    def test_workflow_transitions(self):
        """ Ensure Workflow transitions work correctly """
        self.student_enrollment.insert()

        # Transition to Submitted
        self.student_enrollment.status = "Submitted"
        self.student_enrollment.save()
        self.assertEqual(self.student_enrollment.status, "Submitted")

        # Transition to Approved
        self.student_enrollment.status = "Approved"
        self.student_enrollment.save()
        self.assertEqual(self.student_enrollment.status, "Approved")

        # Transition to Rejected
        self.student_enrollment.status = "Rejected"
        self.student_enrollment.save()
        self.assertEqual(self.student_enrollment.status, "Rejected")

    def tearDown(self):
        """ Cleanup test data """
        frappe.db.rollback()


# Copyright (c) 2025, Arun Govind and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from datetime import datetime
from frappe.utils import getdate,nowdate
from frappe.model.document import Document

class StudentEnrollment(Document):
    def validate(self):
        # Ensure Student Name, Course, and Email are provided
        mandatory_fields = ["student_name", "course", "email", "enrollment_date"]
        for field in mandatory_fields:
            if not getattr(self, field, None):
                frappe.throw(_(f"{field.replace('_', ' ').title()} is mandatory."))
        # Ensure Enrollment Date is not in the future
        if self.enrollment_date:
               today_date = getdate(nowdate())
               enrollment_date = getdate(self.enrollment_date)
               if enrollment_date > today_date:
                      frappe.throw(_("Enrollment Date cannot be in the future."))

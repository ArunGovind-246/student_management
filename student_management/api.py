import frappe
from frappe import _
from frappe.utils import validate_email_address, today
from frappe.exceptions import DoesNotExistError, ValidationError

@frappe.whitelist(allow_guest=False)
def create_student_enrollment(student_name, email, enrollment_date, course, status="Draft"):
    """
    Create a new Student Enrollment record.
    """
    try:
        # Validate Mandatory Fields
        if not student_name or not email or not enrollment_date or not course:
            frappe.throw(_("All fields are required: Student Name, Email, Enrollment Date, and Course"), ValidationError)

        # Validate Email Format
        if not validate_email_address(email):
            frappe.throw(_("Invalid Email Address"), ValidationError)

        # Validate Enrollment Date (should not be in the future)
        if enrollment_date > today():
            frappe.throw(_("Enrollment Date cannot be in the future"), ValidationError)

        # Create the Student Enrollment record
        enrollment = frappe.get_doc({
            "doctype": "Student Enrollment",
            "student_name": student_name,
            "email": email,
            "enrollment_date": enrollment_date,
            "course": course,
            "status": status
        })
        enrollment.insert(ignore_permissions=True)
        frappe.db.commit()

        return {
            "message": "Student Enrollment created successfully",
            "enrollment_id": enrollment.name
        }

    except ValidationError as e:
        frappe.log_error(f"Validation Error: {str(e)}", "Student Enrollment API")
        return {"error": str(e)}
    
    except frappe.DuplicateEntryError:
        frappe.log_error(f"Duplicate Entry: {email} already exists", "Student Enrollment API")
        return {"error": "A student with this email is already enrolled"}

    except Exception as e:
        frappe.log_error(f"Unexpected Error: {str(e)}", "Student Enrollment API")
        return {"error": "An unexpected error occurred. Please try again later."}


@frappe.whitelist(allow_guest=False)
def get_student_enrollment(enrollment_id=None, email=None):
    """
    Retrieve Student Enrollment records by ID or Email.
    """
    try:
        filters = {}

        if enrollment_id:
            filters["name"] = enrollment_id
        if email:
            filters["email"] = email

        if not filters:
            frappe.throw(_("At least one filter (Enrollment ID or Email) is required"), ValidationError)

        records = frappe.get_all(
            "Student Enrollment",
            filters=filters,
            fields=["name", "student_name", "email", "enrollment_date", "course", "status"]
        )

        if not records:
            frappe.throw(_("No Student Enrollment record found"), DoesNotExistError)

        return records

    except DoesNotExistError as e:
        frappe.log_error(f"Record Not Found: {str(e)}", "Student Enrollment API")
        return {"error": str(e)}

    except ValidationError as e:
        frappe.log_error(f"Validation Error: {str(e)}", "Student Enrollment API")
        return {"error": str(e)}

    except Exception as e:
        frappe.log_error(f"Unexpected Error: {str(e)}", "Student Enrollment API")
        return {"error": "An unexpected error occurred. Please try again later."}

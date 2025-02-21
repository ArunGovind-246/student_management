# Copyright (c) 2025, Arun Govind and contributors
# For license information, please see license.txt


import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data()
    return columns, data

def get_columns():
    return [
        {"label": "Course", "fieldname": "course", "fieldtype": "Data", "width": 350},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 450},
        {"label": "Count", "fieldname": "count", "fieldtype": "Int", "width": 400}
    ]

def get_data():
    data = frappe.db.sql("""
        SELECT course, status, COUNT(*) as count
        FROM `tabStudent Enrollment`
        GROUP BY course, status
        ORDER BY course, status
    """, as_dict=True)
    
    return data


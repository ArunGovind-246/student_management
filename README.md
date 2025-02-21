# 🎓 Student Management Module

A Frappe module for managing student enrollments, workflow approvals, reports, and dashboards.

---

## 📌 Features

✅ **Student Enrollment System** – Manage student enrollments with validation checks  
✅ **Workflow Management** – Automate approvals with a state-based workflow  
✅ **Reports & Dashboards** – View enrollment statistics & key metrics in real time  
✅ **Client & Server Validations** – Enforce business rules to maintain data integrity  
✅ **Automated Tests** – Ensure reliability with Frappe’s testing framework  

---

## 🚀 Installation & Setup

### 1️⃣ Install the App
Run the following commands in your Frappe Bench directory:

# Get the app (if not already installed)
bench get-app student_management

# Install it on your site
bench --site yoursite install-app student_management


---

## 2️⃣ Configure the Student Enrollment DocType

### 📌 Fields

| Field Name       | Field Type  | Mandatory | Description                         |
|-----------------|------------|-----------|-------------------------------------|
| Student Name    | Data       | ✅ Yes    | Full name of the student           |
| Email          | Data       | ✅ Yes    | Student’s email (validated)        |
| Enrollment Date | Date       | ✅ Yes    | Cannot be in the future            |
| Course         | Link/Select | ✅ Yes    | Course being enrolled in           |
| Status         | Select     | ✅ Yes    | Options: Draft, Submitted, Approved, Rejected |

### 📌 Client-Side Validations

✅ Ensure Email is in a valid format  
✅ Restrict Enrollment Date to today or past dates  

### 📌 Server-Side Validations

✅ Enforce mandatory fields before submission  
✅ Prevent future Enrollment Dates  
✅ Validate email format at the backend  

---

## 3️⃣ Set Up Workflow

To automate approvals, configure the Workflow in Frappe:

1️⃣ Navigate to: **Frappe Desk > Developer > Workflow**  
2️⃣ Create a new Workflow: **Student Enrollment Workflow**  
3️⃣ Set **Document Type**: Student Enrollment  
4️⃣ Define **Workflow States**:

| State     | Transitions             |
|----------|------------------------|
| Draft    | → Submitted (Initial submission) |
| Submitted | → Approved / Rejected (Admin approval process) |

5️⃣ Set **role-based permissions** (e.g., Only Admins can approve)  

---

## 4️⃣ Run Reports & Dashboards

### 📊 Enrollment Report

1️⃣ Navigate to: **Frappe Desk > Reports**  
2️⃣ Select: **Student Enrollment Report**  
3️⃣ Apply Filters:
   - **Course**  
   - **Date Range**  

### 📈 Dashboard Widget

1️⃣ Navigate to: **Frappe Desk > Dashboard**  
2️⃣ Add Widget: **"Student Enrollment Overview"**  
3️⃣ View Key Metrics:
   - Total Enrollments  
   - Pending Approvals  
   - Approved Enrollments  

---

## 🛠️ Running Tests

Run automated tests to verify module functionality:

```sh
bench --site yoursite run-tests --doctype "Student Enrollment"
```

### ✅ Tests Included:

- Student Enrollment creation  
- Mandatory fields validation  
- Email format validation  
- Future date restriction  
- Workflow transitions (Draft → Approved)  

---

## 📢 Assumptions & Notes

1️⃣ **Email Validation**: The email field must be in proper format.  
2️⃣ **Enrollment Date Restriction**: Cannot be set to a future date.  
3️⃣ **Workflow Permissions**: Only authorized users can approve enrollments.  
4️⃣ **Data Integrity**: Each student must have a unique email per enrollment.  

---

## 📩 Support

For issues or improvements, open a **GitHub Issue** or contact the **Student Management development team**. 🚀



#### License

Arun Govind

import frappe

def create():
    if not frappe.db.exists("DocType", "LC and BG Settings"):
        doc = frappe.get_doc({
            "doctype": "DocType",
            "name": "LC and BG Settings",
            "module": "Letter of Credit and Bank Guarantee",
            "custom": 0,
            "issingle": 1,
            "fields": [
                {
                    "fieldname": "lc_loan_account",
                    "fieldtype": "Link",
                    "options": "Account",
                    "label": "LC Loan Account"
                },
                {
                    "fieldname": "nrb_margin_account",
                    "fieldtype": "Link",
                    "options": "Account",
                    "label": "NRB Margin Account"
                },
                {
                    "fieldname": "lc_margin_account",
                    "fieldtype": "Link",
                    "options": "Account",
                    "label": "LC Margin Account"
                },
                {
                    "fieldname": "bank_charges_account",
                    "fieldtype": "Link",
                    "options": "Account",
                    "label": "Bank Charges/RTGS Account"
                },
                {
                    "fieldname": "insurance_account",
                    "fieldtype": "Link",
                    "options": "Account",
                    "label": "Insurance (L/C) Account"
                }
            ]
        })
        doc.insert(ignore_permissions=True)
        print("DocType created successfully.")
    else:
        print("DocType already exists.")

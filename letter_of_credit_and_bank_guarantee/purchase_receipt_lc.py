
####For Updating Receipt Quantity of Letter of Credit

import frappe
from frappe.utils import flt
def update_lc_receipt_quantity(doc, method):
    if doc.custom_lc_number:
        lc_doc = frappe.get_doc("Letter of Credit", doc.custom_lc_number)
        lc_doc.db_set("receipt_amount", flt(lc_doc.receipt_amount) + flt(doc.base_total))
        lc_doc.db_set("balance_payment", flt(lc_doc.receipt_amount) - flt(lc_doc.payment))
        






        
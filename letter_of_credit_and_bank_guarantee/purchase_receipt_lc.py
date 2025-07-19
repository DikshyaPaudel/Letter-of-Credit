
####For Updating Receipt Quantity of Letter of Credit

import frappe
def update_lc_receipt_quantity(doc, method):
    if doc.custom_lc_number:
        lc_doc = frappe.get_doc("Letter of Credit", doc.custom_lc_number)
        lc_doc.db_set("receipt_amount",lc_doc.receipt_amount+ doc.base_total)
        lc_doc.db_set("balance_payment",int(lc_doc.receipt_amount)-int(lc_doc.payment))
        






        
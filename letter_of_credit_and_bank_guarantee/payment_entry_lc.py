import frappe
from frappe.utils import flt

def update_lc_payment_details(doc, method):

    if not doc.custom_lc_no:
        return
    
    lc = frappe.get_doc("Letter of Credit", doc.custom_lc_no)
    settings = frappe.get_single("LC and BG Settings")
    
    if settings.nrb_margin_account and doc.paid_from == settings.nrb_margin_account:
        lc.db_set("nrb_margin", flt(doc.paid_amount) + flt(lc.nrb_margin))
    else:
        lc.db_set("payment", flt(doc.paid_amount) + flt(lc.payment))
        lc.db_set("total_margin", flt(lc.cash_margin) + flt(lc.nrb_margin))

    lc.db_set("balance_payment", flt(lc.receipt_amount) - flt(lc.payment))

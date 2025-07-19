import frappe

def update_lc_payment_details(doc, method):

    # paid from = 125500 - NRB Margin - S  or 125500 - NRB Margin - A

    if not doc.custom_lc_no:
        return
    
    lc = frappe.get_doc("Letter of Credit", doc.custom_lc_no)
    
    if doc.paid_from == "125500 - NRB Margin - S" and doc.custom_lc_no:
        
        lc.db_set("nrb_margin", doc.paid_amount + lc.nrb_margin)
       
    else:
        # lc=frappe.get_doc("Letter of Credit", doc.custom_lc_no)      
        lc.db_set("payment", doc.paid_amount + lc.payment)
        lc.db_set("total_margin",int(lc.cash_margin) + int(lc.nrb_margin))


    lc.db_set("balance_payment",int(lc.receipt_amount)-int(lc.payment))
    

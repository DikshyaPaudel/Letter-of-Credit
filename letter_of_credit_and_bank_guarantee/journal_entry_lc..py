
import frappe
from frappe.utils import flt

def update_lc(doc, method):
    if not doc.custom_lc_no:
        return

    lc = frappe.get_doc("Letter of Credit", doc.custom_lc_no)

    # Initialize total trackers
    loan_amount = 0
    nrb_margin = 0
    cash_margin = 0
    commission = 0
    payment = 0
    premium_amount=0

    # Set of known LC-related accounts
    handled_accounts = {
        "321103 - LC Loan - SCP",
        "125500 - NRB Margin - SCP",
        "125800 - LC Margin - SCP",
        "519001 - Bank Charges/Lc Rtgs - SCP",
        "519023-Insurance  (L/C) - SCP"
    }

    # Loop through all journal entry accounts
    for acc in doc.accounts:
        debit = flt(acc.debit_in_account_currency or 0)
        credit = flt(acc.credit_in_account_currency or 0)

        account = acc.account

        if account == "321103 - LC Loan - SCP":
            loan_amount += credit - debit

        elif account == "125500 - NRB Margin - SCP":
            nrb_margin += debit - credit

        elif account == "125800 - LC Margin - SCP":
            cash_margin += debit - credit

        elif account == "519001 - Bank Charges/Lc Rtgs - SCP":
            commission += debit - credit

        elif account == "519023-Insurance  (L/C) - SCP":
            premium_amount += debit - credit

        # Any other account is considered as payment (e.g., supplier)
        elif account not in handled_accounts:
            payment += debit - credit  


  

    # Set all LC fields together
    lc.db_set("loan_amount", loan_amount)
    lc.db_set("nrb_margin", nrb_margin)
    lc.db_set("cash_margin", cash_margin)
    lc.db_set("total_margin", nrb_margin + cash_margin)
    lc.db_set("lc_commission_and_charges", commission)
    lc.db_set("payment", payment)
    lc.db_set("premium_amount",premium_amount)
    lc.db_set("balance_payment", flt(lc.receipt_amount or 0) - payment)
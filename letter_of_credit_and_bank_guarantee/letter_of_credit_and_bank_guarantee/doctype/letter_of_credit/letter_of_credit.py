# Copyright (c) 2025, Dikshya Paudel and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document

class LetterofCredit(Document):

    def validate(self):
        self.update_revised_expiry_date()

    def update_revised_expiry_date(self):
        if self.due_date:
            for row in reversed(self.due_date):
                if row.due_date:
                    self.revised_expiry_date=row.due_date
                    break

    # def on_submit(self):    
        
    #     # self.update_bank_lc_limit()

    #     if self.custom_po_no:
    #         frappe.db.set_value("Purchase Order",self.custom_po_no,"custom_lc_number",self.name)
    #     else:
    #         return

    
 
    # def update_bank_lc_limit(self):
    #     # frappe.msgprint(f"Updating LC Limit for Bank: {self.bank}")

        
    #     bank_lc_limits = frappe.get_all("Bank LC Limit", fields=["name"])
    #     if not bank_lc_limits:
    #         frappe.throw("No Bank LC Limit found.")
    
    #     updated = False
    #     for bank_lc_limit in bank_lc_limits:
    #         bank_lc_limit_doc = frappe.get_doc("Bank LC Limit", bank_lc_limit.name)
            
    #         for lc_summary in bank_lc_limit_doc.lc_summary:
                
    #             if lc_summary.bank == self.bank:
    #                 if self.lc_category == "One off":
    #                     new_utilized_off= self.lc_utilized+lc_summary.utilized_one_off
    #                     new_balance_one_off= lc_summary.limit_one_off-lc_summary.utilized_one_off
    #                     if new_utilized_off > lc_summary.limit_one_off:
    #                         frappe.throw(f"Utilized One off - {new_utilized_off} exceeds Limit One off - {new_balance_one_off} ")
                        
    #                     lc_summary.utilized_one_off += self.lc_utilized 
    #                     lc_summary.balance_one_off = lc_summary.limit_one_off - lc_summary.utilized_one_off

    #                 elif self.lc_category == "Regular":
    #                     new_utilized_regular= self.lc_utilized+lc_summary.utilized_regular
    #                     new_balance_regular_off= lc_summary.limit_one_off-lc_summary.utilized_regular
    #                     if new_utilized_regular > lc_summary.limit_regular:
    #                         frappe.throw(f"Utilized Regular - {new_utilized_regular} exceeds Limit Regular - {new_balance_regular_off}")


    #                     lc_summary.utilized_regular += self.lc_utilized
    #                     lc_summary.balance_regular = lc_summary.limit_regular - lc_summary.utilized_regular

    #                 updated = True

                    
    #         if updated:
    #             bank_lc_limit_doc.save()
    #             # frappe.msgprint(f"Bank LC Limit updated in {bank_lc_limit.name}.")
    #             break  # stop after updating first relevant Bank LC Limitz

    #     if not updated:
    #         frappe.throw(f"No LC Limit record found for Bank: {self.bank}")

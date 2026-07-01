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
                    self.revised_expiry_date = row.due_date
                    break

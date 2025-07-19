
# Copyright (c) 2025, Dikshya Paudel and contributors
# For license information, please see license.txt

# import frappe


import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import now

class LCAmendmentSummary(Document):
	def on_submit(self):
		self.update_letter_of_credit()

	def update_letter_of_credit(self):

		if not self.lc_number:
			frappe.throw(_("Letter of Credit reference is missing"))
		
		lc_name = self.lc_number
		
		# Get current timestamp for all amendments in this batch
		current_time = now()
		
		# Get the current highest idx
		max_idx = frappe.db.sql("""
			SELECT IFNULL(MAX(idx), 0)
			FROM `tabLC Amendment`
			WHERE parent=%s AND parenttype='Letter of Credit'
		""", (lc_name,))[0][0]
		
		
		start_idx = max_idx + 1	
		latest_expiry_date = None	
		latest_amended_amount = None
		# latest_amended_quantity = None
		for i, amendment in enumerate(self.lc_amendment_details):
			new_idx = start_idx + i

			latest_expiry_date = amendment.expiry_date
			latest_amended_amount = amendment.amended_amount
			# latest_amended_quantity = amendment.quantity

			frappe.db.sql("""
				INSERT INTO `tabLC Amendment`
				(name, creation, modified, modified_by, owner,
				parent, parenttype, parentfield,
				amendment_date, validitydays, expiry_date,amended_amount, idx)
				VALUES (%s, %s, %s, %s, %s,
				%s, %s, %s,
				%s, %s, %s, %s, %s)
			""", (
				frappe.generate_hash(10), current_time, current_time, frappe.session.user, frappe.session.user,
				lc_name, "Letter of Credit", "lc_amendment_details",
				amendment.amendment_date,  amendment.validitydays,
				amendment.expiry_date,amendment.amended_amount, new_idx
			))


		updates={}	
		if latest_expiry_date:
			updates["revised_expiry_date"] = latest_expiry_date
		if latest_amended_amount:
			updates["revised_amount"] = latest_amended_amount
		# if latest_amended_quantity:
		# 	updates["custom_revised_quantity"] = latest_amended_quantity
		# 	updates["latest_quantity"] = latest_amended_quantity
		
			
		if updates:
			frappe.db.set_value("Letter of Credit", lc_name, updates)

// Copyright (c) 2025, Dikshya Paudel and contributors
// For license information, please see license.txt

frappe.ui.form.on("LC Amendment Summary", {
	refresh(frm) {
        console.log("Refreshed LC Amendment Summary");

	},
});

frappe.ui.form.on('LC Amendment Summary Child', {
    amendment_date: function(frm, cdt, cdn) {
        calculate_expiry_date(frm, cdt, cdn);
    },
    validitydays: function(frm, cdt, cdn) {
        calculate_expiry_date(frm, cdt, cdn);
    },
}
)
function calculate_expiry_date(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    if (row.amendment_date && row.validitydays) {
        let amendmentDate = frappe.datetime.str_to_obj(row.amendment_date);
        let expiryDate = frappe.datetime.add_days(amendmentDate, parseInt(row.validitydays));
        frappe.model.set_value(cdt, cdn, 'expiry_date', frappe.datetime.obj_to_str(expiryDate));
        console.log("Expiry Date:", expiryDate);
    }
}
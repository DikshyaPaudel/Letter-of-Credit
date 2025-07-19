// Copyright (c) 2025, Dikshya Paudel and contributors
// For license information, please see license.txt


frappe.ui.form.on("Bank LC Limit", {
	refresh(frm) {
        console.log("Refreshed Bank LC Limit");

         // 🔹 Detect child tables dynamically & attach event listeners
         $.each(frm.fields_dict, function (fieldname, field) {
            if (field.df.fieldtype === "Table") {
                frappe.ui.form.on(field.df.options, {
                    limit_regular: function (frm, cdt, cdn) {
                        calculate_balance_regular(cdt, cdn);
                        
                    },
                    limit_one_off: function (frm, cdt, cdn) {
                        calculate_balance_oneoff(cdt, cdn);
                    },

                });
            }
        });

	},
});

function calculate_balance_regular(cdt, cdn) {
    let row=locals[cdt][cdn];
    if(row.limit_regular){
        let balance = (row.limit_regular)- (row.utilized_regular || 0);
        console.log("Calculate Balance Regular")
        frappe.model.set_value(cdt, cdn, "balance_regular", balance);
    }

}

function calculate_balance_oneoff(cdt,cdn){
    let row=locals[cdt][cdn];
    if(row.limit_one_off){
        let balance = (row.limit_one_off) - (row.utilized_one_off || 0);
        frappe.model.set_value(cdt, cdn, "balance_one_off", balance);
    }
}

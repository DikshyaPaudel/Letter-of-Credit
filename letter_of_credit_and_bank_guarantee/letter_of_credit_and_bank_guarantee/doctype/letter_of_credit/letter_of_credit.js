// Copyright (c) 2025, Dikshya and contributors
// For license information, please see license.txt

frappe.ui.form.on("Letter of Credit", {
    refresh: function(frm) {
        frm.add_custom_button(__('Payment Entry'), function() {
            frappe.new_doc('Payment Entry', null, function(doc) {
                doc.payment_type = 'Pay';
                doc.party_type = 'Supplier';
                doc.custom_lc_no = frm.doc.name;
                // set party after party_type is processed

                setTimeout(function() {
                    frappe.model.set_value(doc.doctype, doc.name, 'party', frm.doc.supplier);
                    
                },900);
            });
        }, __('Actions'));

    

        
        frm.add_custom_button(__('Journal Entry'), function() {
            frappe.new_doc('Journal Entry',{
                custom_lc_no: frm.doc.name
            })
        }, __('Actions'));

        frm.add_custom_button(__('LC Amendment Summary'), function() {
            frappe.new_doc('LC Amendment Summary', {
                lc_number: frm.doc.name
            });
        })


        if (frm.doc.docstatus === 1) {
            console.log("Submitted")
            // Add main group button
            frm.add_custom_button('Status', () => {}, 'Actions');

            // Add sub-buttons for each status under "Status" group
            const statuses = ['Select', 'Open', 'Expired', 'Closed'];
            const colors = {
                Select: 'blue',
                Open: 'green',
                Expired: 'orange',
                Closed: 'red'
            };

            statuses.forEach((status) => {
                frm.add_custom_button(
                    status.charAt(0).toUpperCase() + status.slice(1),
                    function () {
                        // Update custom status field
                        frm.set_value('status_i', status);
                        frm.save();
                    },
                    'Status'  // Group under Status
                );
            });

         
        }
    
    },
    
    custom_lc_amount_base_currency: function(frm) {
        update_lc_amount(frm);
    },
    custom_exchange_rate: function(frm){
        update_lc_amount(frm);
    },

    lc_amount: function(frm){
        frm.set_value('total_limit', frm.doc.lc_amount);
    },
});

frappe.ui.form.on('Due Date LC',{

    due_date:function(frm, cdt, cdn) {
        update_revised_expiry_date(frm);
    },

    shipment_date: function(frm, cdt, cdn) {
        calculate_due_date(frm,cdt,cdn);
    },
    credit_days: function(frm,cdt,cdn){
        calculate_due_date(frm,cdt,cdn);
    }
})

function calculate_due_date(frm,cdt,cdn){
    let child = locals[cdt][cdn];
    if(child.shipment_date && child.credit_days){
        let shipmentDate= frappe.datetime.str_to_obj(child.shipment_date);
        let dueDate= frappe.datetime.add_days(shipmentDate,parseInt(child.credit_days));
        frappe.model.set_value(cdt,cdn,'due_date',frappe.datetime.obj_to_str(dueDate));
    }
}

function update_revised_expiry_date(frm) {
    if (!frm.doc.due_date || frm.doc.due_date.length === 0) return;

    let last = frm.doc.due_date[frm.doc.due_date.length - 1];
    if (last && last.due_date) {
        frm.set_value('revised_expiry_date', last.due_date);
    }

}
function update_lc_amount(frm) {
    if (frm.doc.custom_lc_amount_base_currency && frm.doc.custom_exchange_rate) {
        let lcAmount = frm.doc.custom_lc_amount_base_currency * frm.doc.custom_exchange_rate;
        frm.set_value('lc_amount', lcAmount);
    } else {
        frm.set_value('lc_amount', 0);
    }
}

}
# Letter of Credit & Bank Guarantee Module

A custom Frappe/ERPNext module for managing the full lifecycle of Letters of 
Credit (LC) and Bank Guarantees (BG) — built to replace manual, spreadsheet-based 
tracking that was prone to reconciliation errors.

## Why this exists

Construction and trade businesses often issue/manage multiple LCs and BGs per 
project, tracked manually across spreadsheets and paper trails. This leads to:
- Lost visibility into LC usage vs. limit
- Manual errors in tracking on/off (active/inactive) status
- No audit trail for issuance and usage events

This module brings LC/BG management directly into ERPNext, with automated 
validations so the system — not a person — catches inconsistencies.

## What it does

- **Issuance tracking** — records LC/BG issuance against a project, vendor, or 
  contract
- **Usage tracking** — logs drawdowns/usage against the LC, validating against 
  the issued limit
- **LC on/off transitions** — manages the active/inactive lifecycle state of 
  each LC/BG, with validation rules preventing invalid state changes 
  (e.g. usage logged against an inactive LC)
- **Automated validations & Integrations**:
  - **Dynamic Account Configuration**: Prevents hardcoded Chart of Accounts mapping by offering a Single DocType (`LC and BG Settings`) for users to define their own specific LC Loan and Margin accounts.
  - **ERPNext Core Integration**: Automatically hooks into standard ERPNext `Payment Entry`, `Journal Entry`, and `Purchase Receipt` submissions to dynamically update LC receipt amounts and margins without modifying core files.
  - **Expiry Date Revision**: Validates and automatically calculates the revised expiry date based on the latest shipment dates and credit days entered in the `Due Date LC` child table.

In production use, this reduced LC tracking errors to near zero compared to 
the prior manual process.

## Tech stack

- Python (Frappe Framework / ERPNext backend logic & hooks)
- JavaScript (Client-side scripts / Doctype form logic & custom buttons)

## Installation

This is a Frappe app — install it on a bench instance:

```bash
bench get-app https://github.com/DikshyaPaudel/Letter-of-Credit
bench --site [your-site] install-app letter_of_credit_and_bank_guarantee
```

## Module structure

- `letter_of_credit_and_bank_guarantee/` — main app directory


## License

MIT

# Copyright (c) 2022, libracore and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

@frappe.whitelist()
def get_open_transactions(customer):
    sql_query = """SELECT
            `tabPurchase Invoice Collection Debtor`.`collection_debtor` AS `collection_debtor`,
            `tabPurchase Invoice Collection Debtor`.`net_amount` AS `net_amount`,
            `tabPurchase Invoice Collection Debtor`.`gross_amount` AS `gross_amount`
        FROM `tabPurchase Invoice Collection Debtor`
        LEFT JOIN `tabSales Invoice Collection Debtor` ON 
            (`tabSales Invoice Collection Debtor`.`pinv_detail` = `tabPurchase Invoice Collection Debtor`.`name`
             AND `tabSales Invoice Collection Debtor`.`docstatus` < 2)
        WHERE
            `tabPurchase Invoice Collection Debtor`.`customer` = "{customer}"
            AND `tabSales Invoice Collection Debtor`.`name` IS NULL;""".format(customer=customer)
    
    data = frapp.db.sql(sql_query, as_dict=True)
    
    return data

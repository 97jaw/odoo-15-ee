# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
#import odoo.addons.decimal_precision as dp
from odoo.addons import decimal_precision as dp       #    odoo11

class RequisitionLine(models.Model):
    _name = "custom.internal.requisition.line"
    _description = "Requisition Line"
    
    requisition_id = fields.Many2one(
        'internal.requisition',
        string='Requisitions', 
    )
    product_id = fields.Many2one(
        'product.product',
        string='Product',
        required=True,
    )
    # TO Do odoo13 object not available
#     layout_category_id = fields.Many2one(
#         'sale.layout_category',
#         string='Section',
#     )
    description = fields.Char(
        string='Description',
        required=True,
    )
    qty = fields.Float(
        string='Quantity',
        default=1,
        required=True,
    )
    uom = fields.Many2one(
        'uom.uom',
        string='Unit of Measure',
        required=True,
    )
    
    @api.onchange('product_id')
    def set_uom(self):
        for rec in self:
            rec.description = rec.product_id.name
            rec.uom = rec.product_id.uom_id.id

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

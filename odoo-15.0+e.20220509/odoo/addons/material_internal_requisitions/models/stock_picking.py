# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class Picking(models.Model):
    _inherit = 'stock.picking'

    inter_requi_id = fields.Many2one(
        'internal.requisition',
        string='Internal Requisition',
        readonly=True,
    )
    
    #@api.multi
    #def _write(self, vals):
        #result = super(StockPicking, self)._write(vals)
        #for rec in self:
            #obj = self.inter_requi_id
            #if rec.state == 'done' and rec.inter_requi_id:
                #rec.inter_requi_id.write({'state' : 'receive'})
        #return result

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

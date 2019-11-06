# -*- coding: utf-8 -*-

from odoo import models, fields

class PlrSyndicate(models.Model):    
    _inherit = 'res.partner'

    associate_syndicate = fields.Boolean('Sindicato Associado', default=False)
    company_syndicate = fields.Many2many('plr.company', string='Empresas Vinculadas')
# -*- coding: utf-8 -*-

from odoo import api, models, fields
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError

from odoo.addons.br_base.tools import fiscal


class PlrCompany(models.Model):
	_name = 'plr.company'

	name = fields.Char(string='Nome', required=True)	
	legal_name = fields.Char(string='Razão Social', size=60, help="Nome utilizado em documentos fiscais")
	photo = fields.Binary(string='Imagem')
	cnpj = fields.Char(string='CNPJ', size=18)
	inscr_est = fields.Char(string='Inscrição Estadual', size=16)
	inscr_mun = fields.Char(string='Inscrição Municipal', size=18)
	address_zip = fields.Char(string='CEP', size=10)
	address_district = fields.Char(string='Bairro', size=32)
	address_street = fields.Char(string='Endereço', size=64)
	address_number = fields.Char(string='Número', size=10)
	address_complement = fields.Char(string='Complemento', size=10)
	address_city = fields.Many2one('res.state.city', string='Município')
	address_state = fields.Many2one('res.country.state', string='UF')
	address_country = fields.Many2one('res.country', string='País')
	ceo = fields.Char(string='Diretor/Presidente', required=True)
	faturamento = fields.Float(string='Faturamento', digits=(12,2),required=True)	
	lucro_liquido = fields.Float(string='Lucro Líquido', digits=(12,2), required=True)
	fornecedores = fields.Text(string='Fornecedores', required=True)
	criterio_medicao = fields.Text(string='Criterio de Medição', required=True)
	valor_distribuido = fields.Float(string='Valor Distribuido', digits=(12,2), required=True)
	numero_trabalhadores = fields.Integer(string='Número de Trabalhadores', required=True)
	numero_socios_sindicatos = fields.Integer(string='Número de Sócios Sindicatos', required=True)
	cipa = fields.Text(string='CIPA')
	comissao_negociacao = fields.Text(string='Comissão Negociação')
	info_complementar_dieese = fields.Text(string='Informações Complementares DIEESE')
	company_syndicate = fields.Many2one('res.partner', string='Sindicato Relacionado')
	
	
	_sql_constraints = [
        ('cnpj', 'unique (cnpj)', 'O CNPJ deve ser único')
    ]
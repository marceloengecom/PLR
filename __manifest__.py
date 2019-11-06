# -*- coding: utf-8 -*-
{
    'name': "PLR",

    'summary': """
        Participacao de Lucros e Resultados""",

    'description': """
        Participacao de Lucros e Resultados - Módulo produzido para FTM
    """,

    'author': "Marcelo Costa",
	'company': 'COMDESK Tecnologia',
    'website': "http://www.comdesk.com.br",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/plr_view.xml',        
        'views/syndicate_resPartner_view.xml',
        'reports/report1.xml',
    ],
    'images': [],
	'license': 'AGPL-3',
	'installable': True,
	'application': True,
	'auto_install': False,
    }
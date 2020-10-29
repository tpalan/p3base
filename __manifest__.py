{
    'name': "p3base",

    'summary': """
        palan3 odoo customizations""",

    'description': """
        Modifies standard odoo configuration:
	- sets correct address & date formats for Austria/German
	- add Leistungszeitraum attribute to invoice	
    """,

    'author': "Tom Palan <thomas@palan.at>",
    'website': "http://www.palan.at",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/data.sql',
        'views/views.xml'
    ],
    'installable': True
}

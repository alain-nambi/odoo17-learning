{
    'name': "Real Estate Advertisement",
    'version': '1.0',
    'depends': ['base'],
    'author': "RAKOTOARIVELO Alain Nambinintsoa",
    'category': 'Category',
    'description': """
    Our new module will cover a business area which is very specific
    and therefore not included in the standard set of modules: real estate.
    It is worth noting that before developing a new module,
    it is good practice to verify that Odoo doesn’t
    already provide a way to answer the specific business case.
    """,
    # # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
        'views/estate_type_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}

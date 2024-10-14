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
        # 'views/mymodule_view.xml',
        'security/ir.model.access.csv',
    ],
    # # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
    'installable': True,
    'application': True,
    'auto_install': False
}

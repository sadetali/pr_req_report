{
    'name': 'Product Request Report',
    'version': '18.0.3.0',
    'category': 'Inventory',
    'summary': 'Product request report with internal variant support for transfers',
    'license': 'LGPL-3',
    'author': 'Anwar Sadeth Ali Mohamed Ayyatil',
    
    'depends': [
        'stock',
        'product',
    ],

    'data': [
        # Security (VERY IMPORTANT - must be first)
        'security/ir.model.access.csv',

        # Views
        'views/product_template_views.xml',
        'views/stock_picking_views.xml',

        # Reports
        'report/report.xml',
        'report/template.xml',
    ],

    'installable': True,
    'application': False,
}

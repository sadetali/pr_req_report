{
    'name': 'Product Request Report',
    'version': '18.0.2.1',
    'category': 'Inventory',
    'summary': 'Compact grouped product request report for internal transfers',
    'license': 'LGPL-3',
    'depends': ['stock', 'product'],
    'data': [
        'views/product_template_views.xml',
        'report/report.xml',
        'report/template.xml'
    ],
    'installable': True,
    'application': False
}

{
    'name': 'Sales order multi lots selection with available product quantity',
    'version': '12.0.4',
    'category': 'Sales Management',
    'summary': 'Sales order multi lots selection with available product quantity',
    'description': """ Using this module you can select multiple lot in sale order line and you can only select lot number if product lot number is avaialble  with  Lot quantity.
    """,
    'price': 18,
    'currency': 'EUR',
    'author': 'Kiran Kantesariya',
    'email': 'risingsuntechcs@gmail.com',
    'license': 'OPL-1',
    'depends': ['sale_management','sale_stock'],
    # "live_test_url" : "https://youtu.be/FguV-HyV5y4",
    'data': [
        'views/sale_view.xml',
        'report/sale_report_templates.xml',
    ],
    'qweb': [
        ],
    'images': ['static/description/main_screenshot.jpg'],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}

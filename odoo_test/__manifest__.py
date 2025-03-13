# Copyright 2023 Etech
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Odoo Test',
    'description': """
        Double purchase validation""",
    'version': '16',
    'license': 'AGPL-3',
    'author': 'Eufonie Dev',
    'website': 'https://eufonie.fr',
    'depends': [
        "purchase"
    ],
    'data': [
        'views/res_partner_views.xml',
        'views/purchase_order_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'odoo_test/static/src/js/purchase_order_list_view.js',
            'odoo_test/static/src/xml/purchase_approve_all.xml',
        ],
    }
}

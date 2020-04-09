# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Library Base',
    'description': """
        Base of library""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'KMEE',
    'website': 'www.kmee.com.br',
    'depends': [
        'base',
        'contacts',
        'web_responsive',
        'book_product',
    ],
    'data': [
        'security/library_book_rent.xml',
        'security/library_rent_policy.xml',
        'security/library_book_asset.xml',
        'security/library_partner_relation.xml',
        # 'security/res_partner.xml',

        'data/ir_sequence_data.xml',

        'wizards/wizard_library_book_return.xml',
        'wizards/wizard_library_book_rent.xml',
        'views/library_book_asset.xml',
        'views/library_book_rent.xml',
        'views/res_partner.xml',
        'views/library_rent_policy.xml',
        'views/library_partner_relation.xml',
    ],
    'demo': [
        'demo/library_partner_relation.xml',
        'demo/res_partner.xml',
        'demo/library_book_asset.xml',
        'demo/library_rent_policy.xml',
    ],
}

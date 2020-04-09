# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Book Product',
    'description': """
        Product customizations for Book stores and libraries""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'KMEE',
    'website': 'www.kmee.com.br',
    'depends': [
        'product',
    ],
    'data': [
        # 'security/res_partner.xml',
        # 'security/product_product.xml',

        'views/book_product_menu.xml',

        'views/res_partner.xml',
        'views/product_product.xml',
    ],
    'demo': [
        'demo/res_partner.xml',
        'demo/product_product.xml',
    ],
    "external_dependencies": {"python": ["isbn_hyphenate", "is_isbn"]},
    # Nome do pacote!!! https://github.com/khimsh/is_isbn/blob/master/setup.py#L40 Não o nome da lib!
}

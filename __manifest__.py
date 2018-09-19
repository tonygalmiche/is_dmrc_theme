# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Module Odoo InfoSaône - Thème pour DMRC',
    'summary': 'Module Odoo InfoSaône - Thème pour DMRC',
    'description': 'Module Odoo InfoSaône - Thème pour DMRC',
    'category': 'InfoSaône',
    'author'   : 'InfoSaône',
    'maintainer' : 'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'version': '1.0',
    'depends': [
        'website',
        'theme_bootswatch',
    ],
    'data': [
        'views/theme_bootswatch_templates.xml',
    ],
    'images': ['static/description/bootswatch.png'],
    'application': True,
}


# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Training_center',
    'version': '1.1',
    'author': 'Maamri Akram , Laroussi Med Aziz',
    'category': 'Human Resources/Training_center',
    'sequence': -100,
    'summary': 'Centralize training center information',
    'website': '',
    'depends': ['base', 'hr', 'hr_holidays', 'mail' ,'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/enseignant_process.xml',
        'views/etudiant_views.xml',
        'views/cours_views.xml',
        'security/hr_attendance_security.xml',
        'views/user_form_extension.xml',
        'views/training_center_view.xml',
        'reports/report.xml'
    ],
'qweb': [
        'reports/report.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
            'Training_center/static/src/enseignant.css'
        ]
    },

}

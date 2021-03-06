{ 
    'name': "HR Advanced Working Hours", 
    'summary': "This module enhanches woking hours management.", 
    'description': """This modules enhanches working hours management by adding automatic shifts and reports.""", 
    'author': "RDS Moulding Technology SpA", 
    'license': "AGPL-3", 
    'website': "http://rdsmoulding.com", 
    'category': 'hr', 
    'version': '11.0.1.0.0', 
    'depends': ['hr'], 
    'data': [
            'report/print_turns.xml',
            'views/hr_views.xml',
            'views/report_templates.xml',
            'wizard/turn_printer_view.xml',
            'cron/cron_rotate_shifts.xml',
    ],
    'application': False,
    'installable': True,
} 
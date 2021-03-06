{
    'name': "RDS Dia",
    'summary': "Modulo di integrazione a DIA.",
    'description': """Il modulo implementa integrazioni con il sistema DIA necessarie a RDS.""",
    'author': "RDS Moulding Technology S.p.A.",
    'license': "AGPL-3",
    'website': "http://rdsmoulding.com",
    'category': 'Integrations',
    'depends': ['sale', 'l10n_it_picking_ddt'],
    'data': [
            # data
            'data/cron.xml',
            'data/sequence.xml',
            'security/ir.model.access.csv',
            # view
            'views/dia_transfer.xml',
            'views/dia_fields_views.xml'
            ],
    'application': 'false',
    'installable': 'true',
}

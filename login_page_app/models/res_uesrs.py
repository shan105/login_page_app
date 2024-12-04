from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    is_redirected = fields.Boolean(
        string='Redirected',
        default=False,
        help='Flag to track if the user has been redirected after login.'
    )

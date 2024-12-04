from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo import fields, http, _
from odoo.http import request

class CustomLoginRedirect(AuthSignupHome):
    @http.route('/web/login', type='http', auth='none', website=True)
    def web_login(self, redirect=None, **kwargs):
        # Call the parent class's web_login method
        response = super(CustomLoginRedirect, self).web_login(redirect, **kwargs)

        # Redirect to the specified page if the login is successful
        if request.session.uid:
            user = request.env['res.users'].sudo().browse(request.session.uid)
            if not user.is_redirected:
                user.is_redirected = True

                pick_theme = request.env['ir.actions.actions'].sudo().search([('name', '=', 'Pick a Theme')], limit=1).id
        
                return request.redirect(f'/web#action={pick_theme}&model=ir.module.module&view_type=kanban')

        # Return the original response if the login failed
        return response

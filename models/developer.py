from odoo import models, fields, api


class developer(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"


    technologies_id = fields.Many2many("managedaniel.technology",
                                    relation="developer_technologies",
                                    column1="developer_id",
                                    column2="technologies_id")
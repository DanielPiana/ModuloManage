from odoo import models, fields, api


class technology(models.Model):
    _name = 'managedaniel.technology'
    _description = 'managedaniel.technology'

    name = fields.Char(string="Nombre", readonly=False, required=True, help="Introduzca el nombre")
    description = fields.Char(string ="Descripción")
    image = fields.Image(string="Imagen")

    task_id = fields.Many2many(
        comodel_name="managedaniel.technology",
        relation="technology_task",
        column1="technology_ids",
        column2="task_ids"
    )

    developer_id = fields.Many2many("res.partner",
                                    relation="developer_technologies",
                                    column1 ="technologies_id",
                                    column2 ="developer_id")
from odoo import models, fields, api


class history(models.Model):
    _name = 'managedaniel.history'
    _description = 'managedaniel.history'

    name = fields.Char(string="Nombre", readonly=False, required=True, help="Introduzca el nombre")
    description = fields.Char(string ="Descripción")

    project_id = fields.Many2one("managedaniel.project",
                                 string="Proyecto",
                                 required=True,
                                 ondelete="cascade")

    history_task_id = fields.One2many(comodel_name="managedaniel.task",
                                      inverse_name="task_history_id",
                                      string="Tarea ID")
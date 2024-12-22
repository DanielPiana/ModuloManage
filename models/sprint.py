

from odoo import models, fields, api


class sprint(models.Model):
    _name = 'managedaniel.sprint'
    _description = 'managedaniel.sprint'

    name = fields.Char(string="Nombre", readonly=False, required=True, help="Introduzca el nombre")
    description = fields.Char(string="Descripción")
    start_date = fields.Datetime(string="Fecha de inicio")
    end_date = fields.Datetime(string="Fecha de finalización")

    task_id = fields.One2many(
        string="Tasks",
        comodel_name="managedaniel.task",
        inverse_name="sprint_id")

    project_sprint_id = fields.Many2one(
        "managedaniel.project",
        ondelete="cascade",
        string="Projects")
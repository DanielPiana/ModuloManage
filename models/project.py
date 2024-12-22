from odoo import models, fields, api


class project(models.Model):
    _name = 'managedaniel.project'
    _description = 'managedaniel.project'

    name = fields.Char(string="Nombre", readonly=False, required=True, help="Introduzca el nombre")
    description = fields.Char(string ="Descripción")


    history_id = fields.One2many(
        comodel_name="managedaniel.history",
        inverse_name="project_id",
        string="Historial")

    sprint_project_id =fields.One2many(
        comodel_name="managedaniel.sprint",
        inverse_name="project_sprint_id",
        string="Sprint")
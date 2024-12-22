
import datetime
from odoo import models, fields, api


class task(models.Model):
    _name = 'managedaniel.task'
    _description = 'managedaniel.task'

    code = fields.Char(string="Código", compute ="_get_code")
    name = fields.Char(string="Nombre", readonly=False, required=True, help="Introduzca el nombre")
    description = fields.Char(string ="Descripción")
    start_date = fields.Datetime(string="Fecha de inicio")
    end_date = fields.Datetime(string="Fecha de finalización")
    is_paused = fields.Boolean(string="¿Está pausado?")


    sprint_id = fields.Many2one(
        "managedaniel.sprint",
        string="Sprint",
        ondelete="cascade",
        compute="_get_sprint",
        store=True
    )

    technology_id = fields.Many2many(
        comodel_name="managedaniel.technology",
        relation="technology_task",
        column1="task_ids",
        column2="technology_ids"
    )

    task_history_id = fields.Many2one(
        "managedaniel.history",
        ondelete="cascade",
        string="Historia relacionada")

    def _get_code(self):
        for task in self:
            if len(task.sprint_id) == 0:
                task.code = "FILM_"+str(task.id)
            else:
                task.code = str(task.sprint_id.name).upper()+ "_" +str(task.id)

    @api.depends("code")
    def _get_sprint(self):
        for task in self:
            sprints = self.env["managedaniel.sprint"].search([("project_sprint_id.id", "=", task.task_history_id.project_id.id)])
            found = False
            for sprint in sprints:
                if isinstance(sprint.end_date, datetime.datetime) and sprint.end_date > datetime.datetime.now():
                    task.sprint_id = sprint.id
                    found = True
            if not found:
                task.sprint_id = False
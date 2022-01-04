# -*- coding: utf-8 -*-
# © 2018 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models


class ProjectTodo(models.Model):
    _name = 'project.todo'
    _description = 'Todo Model'

    name = fields.Char()
    text_todo = fields.Text('Content of Todo')
    user = fields.Many2one('res.users', required=True)
    todo_type = fields.Many2one(
        string='type Of Todo', 
        comodel_name='project.todo.type')
    deadline = fields.Datetime(required=True , default=fields.Date.today())
    days_left = fields.Integer(
        compute='_compute_days_left',
        inverse='_inverse_days_left'
    )
    is_urgent = fields.Boolean(compute='_compute_is_urgent')
    todo_type_importance = fields.Integer(related='todo_type.importance',  readonly=True)

    @api.depends('deadline')
    def _compute_days_left(self):
        today = fields.Date.from_string(fields.Date.today())
        for this in self:
            td = today - fields.Date.from_string(this.deadline)
            #active record
            this.days_left = td.days


    #if I change days left, the deadline needs to move!!!!

    def _inverse_days_left(self):
        today = fields.Date.from_string(fields.Date.today())
        for this in self:
            d = today - timedelta(days=this.days_left)
            this.deadline = fields.Date.to_string(d)

    def _compute_is_urgent(self):
        for this in self:
            this.is_urgent = True if this.days_left < 3  else False 

    @api.multi
    def server_action_was_here(self):
        for this in self:
            this.write(
                {'text_todo': this.text_todo + 'A server Action Was here'})


    @api.model
    def get_all_urgent_coding_jobs(self):
        """
        returns a recordset of all urgent coding jobs
        """
        return self.env['project.todo'].search([
            ('name', 'like', 'coding'), ('todo_type.name', '=', 'urgent')])
    
        # example of a call for data: we can put in our data a todo_type with name 'urgent' in our data to be sure the user has it available.

    @api.model
    def get_all_important_jobs(self):
        """returns all todos with importance >10"""
        return self.env['project.todo'].search([
            ('todo_type.importance', '>', 10)])

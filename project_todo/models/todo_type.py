# -*- coding: utf-8 -*-
# © 2018 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models


class ProjectTodoType(models.Model):
    _name = 'project.todo.type'
    _description = 'Type of todo'


    name = fields.Char()
    importance = fields.Integer()

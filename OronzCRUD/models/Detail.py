# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class Details(models.Model):
    _name = "detail.detail"
    _description = 'Model To store update and delete some data'


    name = fields.Char('Name', required=True)
    description = fields.Char('Description')
    content = fields.Html('Content')


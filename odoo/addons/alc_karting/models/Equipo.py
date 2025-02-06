# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Equipo(models.Model):
    _name = 'alc_karting.equipo'
    _description = 'Equipo'    
    name = fields.Char(string='Nombre', required=True, help="Introduce el nombre del equipo")
    fecha_creacion = fields.Date(string='Fecha de creación', required=True, help="Introduce la fecha en la que se ha creado el equipo")
    num_victorias = fields.Integer(string='Número de victorias', help="Introduce el número de victorias que ha conseguido este equipo")
    competidores_ids = fields.One2many('alc_karting.competidor', 'equipo_id', string='Lista de competidores')
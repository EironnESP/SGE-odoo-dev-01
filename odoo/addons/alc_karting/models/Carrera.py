# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Carrera(models.Model):
    _name = 'alc_karting.carrera'
    _description = 'Carrera'
    
    name = fields.Char(string='Nombre', required=True, help="Introduce el nombre de la carrera (ej. 6ª de la tarde)")
    fecha = fields.Date(string='Fecha', required=True, help="Introduce la fecha en la que se realiza la carrera")
    num_competidores = fields.Integer(string='Número de competidores', help="Introduce el número de competidores que participan")
    karts_participando = fields.Many2many('alc_karting.kart', string='Karts participando en esta carrera')
    competidores_participando = fields.Many2many('alc_karting.competidor', string='Competidores participando en esta carrera')
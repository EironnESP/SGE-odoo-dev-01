# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Competidor(models.Model):
    _name = 'alc_karting.competidor'
    _description = 'Competidor'
    
    name = fields.Char(string='Nick', required=True, help="Introduce el nick del corredor")
    nombre = fields.Char(string='Nombre', required=True, help="Introduce el nombre del corredor")
    apellidos = fields.Char(string='Apellidos', required=True, help="Introduce los apellidos del corredor")
    numero = fields.Integer(string='Número único', required=True, help="Introduce el número único identificador del competidor")
    num_carreras = fields.Integer(string='Número de carreras', help="Introduce el número de carreras en las que ha participado")
    equipo_id = fields.Many2one('alc_karting.equipo', string='Equipo')
    carreras_ids = fields.Many2many('alc_karting.carrera', string='Carreras en las que ha participado o participará')
    numero_kart = fields.Char(string='Número del kart', help='Introduce el número del kart asignado')
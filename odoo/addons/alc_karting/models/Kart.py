# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Kart(models.Model):
    _name = 'alc_karting.kart'
    _description = 'Kart'
    
    name = fields.Char(string='Número', required=True, help="Introduce el número que el kart lleva inscrito, 0s incluidos")
    caballos = fields.Integer(string='Caballos', help='Introduce el número de caballos del motor')
    control_remoto = fields.Boolean(string='Control remoto', help="Indica si el kart permite ser controlado de forma remota")
    combustible_recomendado = fields.Selection([
        ('0', 'Diésel'),
        ('1', 'Gasolina 95'),
        ('2', 'Gasolina 98'),
        ('3', 'Eléctrico'),
    ], string='Combustible recomendado', default='1')
    carreras_ids = fields.Many2many('alc_karting.carrera', string='Carreras en las que este kart participa')
    nick_competidor = fields.Char(string='Nick del competidor', help='Introduce el nick del competidor asignado')
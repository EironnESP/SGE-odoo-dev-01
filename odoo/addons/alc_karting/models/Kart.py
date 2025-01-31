# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Kart(models.Model):
    _name = 'alc_karting.kart'
    _description = 'Kart'
    
    numero = fields.Integer(string='Número', required=True, help="Introduce el número del kart")
    caballos = fields.Integer('caballos')
    control_remoto = fields.Boolean('control_remoto')
    
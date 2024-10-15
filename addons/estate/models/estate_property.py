from odoo import fields, models
from datetime import date, timedelta


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    def _default_date_availability(self):
        return date.today() + timedelta(days=90)

    name = fields.Char(string='Property Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='PostCode')
    date_availability = fields.Date(
        copy=False,
        default=_default_date_availability
    )
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(
        string='Selling Price',
        readonly=True,
        copy=False
    )
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West'),
        ]
    )
    active=fields.Boolean(string='Active')

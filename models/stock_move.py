from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    x_internal_variant_id = fields.Many2one(
        "product.internal.variant",
        string="Variant",
    )

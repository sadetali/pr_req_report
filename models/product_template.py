from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    internal_variant_ids = fields.One2many(
        "product.internal.variant",
        "product_tmpl_id",
        string="Internal Variants",
    )

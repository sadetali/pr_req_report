from odoo import fields, models


class ProductInternalVariant(models.Model):
    _name = "product.internal.variant"
    _description = "Product Internal Variant"
    _order = "sequence, name"

    name = fields.Char(string="Variant Name", required=True)
    
    product_tmpl_id = fields.Many2one(
        "product.template",
        string="Product",
        required=True,
        ondelete="cascade"
    )

    sequence = fields.Integer(default=10)
    
    active = fields.Boolean(default=True)

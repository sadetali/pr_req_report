from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    x_internal_variant_id = fields.Many2one(
        "product.internal.variant",
        string="Variant",
    )

    @api.onchange("product_id")
    def _onchange_product_id_internal_variant(self):
        for line in self:
            if not line.product_id:
                line.x_internal_variant_id = False
                continue

            if (
                line.x_internal_variant_id
                and line.x_internal_variant_id.product_tmpl_id != line.product_id.product_tmpl_id
            ):
                line.x_internal_variant_id = False

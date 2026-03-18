from odoo import fields, models

class ProductRequestReport(models.AbstractModel):
    _name = 'report.pr_req_report.rpt'
    _description = 'Product Request Report'
    _auto = False
    _table = 'pr_req_rpt'

    def _get_report_values(self, docids, data=None):
        docs = self.env['stock.picking'].browse(docids)
        printed_dt = fields.Datetime.context_timestamp(self, fields.Datetime.now())
        printed_on = printed_dt.strftime('%d/%m/%Y %H:%M:%S') if printed_dt else ''
        return {
            'doc_ids': docids,
            'doc_model': 'stock.picking',
            'docs': docs,
            'printed_by': self.env.user.name or '',
            'printed_on': printed_on,
        }

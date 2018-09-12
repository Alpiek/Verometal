from odoo import api, models


class HazardousReport(models.AbstractModel):
    _name = 'adr_chemicals.hazardous_report'

    @api.model
    def render_html(self, docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('adr_chemicals.hazardous_report')

        # custom_data = self.env['model.name'].get_data()

        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': self,
            'hazardous_total': 100,
        }
        return report_obj.render('adr_chemicals.hazardous_report', docargs)

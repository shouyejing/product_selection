from openerp import models, fields, api, exceptions, _


class Product(models.Model):
    _inherit = 'product.product'

    category_id = fields.Many2one("product.category", related='product_tmpl_id.categ_id', store=True, readonly=True)


    # product_selection_ids = fields.Many2many("cate_test.cate_test")


class ProductSelection(models.Model):
    _name = 'cate_test.cate_sel'

    category_id = fields.Many2one("product.category")

    product_ids = fields.Many2many("product.product")

    product_id = fields.Many2one("product.product")

    @api.onchange('category_id')
    @api.multi
    def _onchange_category_id(self):
        domain = []
        for record in self:
            if record.category_id:
                domain = [("category_id", "child_of", record.category_id.id)]
                products = self.env["product.product"].search(domain)
                record.product_ids = products
            else:
                record.product_ids = {}

        return {"domain": {"product_id": domain}}
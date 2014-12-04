# -*- coding: utf-8 -*-
##############################################################################
#
#    Acespritech Solutions Pvt Ltd
#    Copyright (C) 2013-today
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import fields, osv
from openerp.tools.translate import _


class change_currency(osv.osv_memory):
    _name = "change.currency"
    _columns = {
        'currency_id': fields.many2one('res.currency', 'Currency',
                                        required=True),
        'change_option': fields.selection([('all', 'All Company'),
                                    ('selected', 'Selected Company')],
                                    string='Option', required=True),
    }

    def action_update_currency(self, cr, uid, ids, context={}):
        if context is None:
            context = {}
        if context.get('active_ids') and len(context.get('active_ids')) > 1:
            raise osv.except_osv(_('Error!'),
                                 _('Please select only one record'))
        record = self.browse(cr, uid, ids[0])
        currency = record.currency_id.id
        cr.execute("""SELECT m.model,mf.name \
                      FROM ir_model_fields mf \
                      LEFT JOIN ir_model m on mf.model_id=m.id \
                      WHERE mf.relation='res.currency' \
                      AND mf.ttype='many2one'""")
        for rec in  cr.fetchall():
            inst = self.pool.get(rec[0])
            table = inst._table
            cr.execute("""SELECT 1
                        FROM information_schema.tables
                        WHERE table_schema = 'public'
                        AND table_type='BASE TABLE'
                        AND table_name=%s""", (table,))
            base_table = cr.fetchone()
            if base_table and base_table[0]:
                cr.execute("""SELECT 1
                          FROM information_schema.columns
                          WHERE table_name=%s
                          AND column_name=%s""", (table, rec[1]))
                column = cr.fetchone()
                if column and column[0]:
                    if record.change_option == 'selected':
                        sql = """UPDATE %s SET %s=%s""" % (table, rec[1],
                                                           currency)
                        cr.execute("""SELECT 1
                          FROM information_schema.columns
                          WHERE table_name=%s
                          AND column_name='company_id'""", (table,))
                        company_col = cr.fetchone()
                        if company_col and company_col[0]:
                            sql += ' WHERE company_id=%s' % \
                                                context['active_id']
                        if table == 'res_company':
                            sql = """UPDATE %s SET %s=%s WHERE id=%s""" % \
                                (table, rec[1], currency, context['active_id'])
                    else:
                        sql = """UPDATE %s SET %s=%s""" % (table, rec[1],
                                                           currency)
                    cr.execute(sql)
        cr.commit()
        return True

change_currency()

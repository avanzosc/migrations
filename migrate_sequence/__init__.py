# -*- coding: utf-8 -*-
# © 2016 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html


def add_sequence(cr):
    cr.execute("""SELECT id, number_next, number_increment
               FROM ir_sequence ORDER BY id;""")

    for seq in cr.dictfetchall():
        sql = "DROP SEQUENCE IF EXISTS ir_sequence_%03d" % seq['id']
        cr.execute(sql)
        sql = "CREATE SEQUENCE ir_sequence_%03d INCREMENT BY %%s START WITH %%s" % seq['id']
        cr.execute(sql, (seq['number_increment'], seq['number_next']))

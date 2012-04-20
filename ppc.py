# -*- coding: utf-8 -*-

import os
import sys
from cmd2 import Cmd


ROOT = os.path.abspath(os.path.dirname(__file__))

class CmdHandler(Cmd, object):

    tables = {
        'cities': {'tblname': 'cities',
                   'cols': ['id', 'name', 'province_id']},
        'provinces': {'tblname': 'provinces',
                      'cols': ['id', 'name']}
    }

    def __init__(self):
        super(CmdHandler, self).__init__()
        print """
These are the default table definitions:
cities:id,name,province_id
provinces:id,name

use the `table` command and follow the same format to override
and use the `spit` command to generate the sql file.

i.e: to override the cities table, do:
table cities=citiesx:idx,namex,province_idx
table provinces=provincesx:idx,namex

"""
        self.prompt = ">>> "

    def do_table(self, arg):
        oldtblname, newtbl = arg.split("=")
        innertbls = dict([(v['tblname'], v['cols']) for v in self.tables.values()])

        if oldtblname not in innertbls:
            print "Table '%s' doesn't exist.\n" % oldtblname
            return

        tblname, cols = newtbl.split(":")
        cols = [col.strip() for col in cols.split(",")]

        if len(cols) != len(innertbls[oldtblname]):
            print "Column count for table '%s' doesn't match.\n" % oldtblname
            return

        for k, v in self.tables.items():
            if v['tblname'] == oldtblname:
                self.tables[k]['tblname'] = tblname
                self.tables[k]['cols'] = cols
                break

        print self.tables

    def do_spit(self, arg):
        middle = []
        for k, tbldef in self.tables.items():
            tpl = open(os.path.join(ROOT, 'templates', ('%s.tpl' % k))).read()
            tpl = tpl.replace('tblname', tbldef['tblname'])
            for i, col in enumerate(tbldef['cols']):
                tpl = tpl.replace(('col%s' % i), col)
            middle.append(tpl)

        out_sql = os.path.join(ROOT, 'ppc.sql')
        tpl = open(os.path.join(ROOT, 'templates', 'ppc.tpl')).read()
        tpl = tpl % ("\n".join(middle))
        out = open(out_sql, 'w')
        out.write(tpl)
        out.close()

        print out_sql

    def do_EOF(self, line):
        return True

if __name__ == "__main__":
    CmdHandler().cmdloop()

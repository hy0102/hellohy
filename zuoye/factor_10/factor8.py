# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 23:54:42 2018

@author: dream
"""


def run_formula(dv, param=None):
    defult_param = {'t': 60}
    if not param:
        param = defult_param

    factor8 = dv.add_formula("factor8", "(%s*ps)/Ts_Sum(ps,%s)-1"
                              %(param['t'],param['t']),
                        is_quarterly=False,
                        add_data=False)
    return factor8
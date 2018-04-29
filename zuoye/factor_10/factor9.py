# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 23:54:55 2018

@author: dream
"""


def run_formula(dv, param=None):
    defult_param = {'t': 60}
    if not param:
        param = defult_param

    factor9 = dv.add_formula("factor9", "(%s*float_mv)/Ts_Sum(float_mv,%s)"
                              %(param['t'],param['t']),
                        is_quarterly=False,
                        add_data=False)
    return factor9
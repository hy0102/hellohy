# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 23:54:20 2018

@author: dream
"""


def run_formula(dv, param=None):
    defult_param = {'t':20}
    if not param:
        param = defult_param

    factor7 = dv.add_formula("factor7", "(%s*pb)/(Ts_Sum(Delay(pb,%s),%s))-1"
                              %(param['t'],param['t'],param['t']),
                        is_quarterly=False,
                        add_data=False)
    return factor7
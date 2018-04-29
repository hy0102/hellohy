# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 00:07:50 2018

@author: dream
"""

def run_formula(dv, param=None):
    defult_param = {'t': 5}
    if not param:
        param = defult_param

    factor12 = dv.add_formula("factor12", "StdDev(open,%s)"
                              %(param['t']),
                        is_quarterly=False,
                        add_data=False)
    return factor12
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 23:49:56 2018

@author: dream
"""

def run_formula(dv, param=None):
    defult_param = {'t': 20,}
    if not param:
        param = defult_param

    factor6 = dv.add_formula("factor6", "Rank(Ts_Min(close*volume,%s))"
                              %(param['t']),
                        is_quarterly=False,
                        add_data=False)
    return factor6
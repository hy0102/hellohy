# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 23:35:32 2018

@author: dream
"""

def run_formula(dv, param=None):
    defult_param = {'t': 20}
    if not param:
        param = defult_param

    factor4 = dv.add_formula("factor4", "Rank(Corr(pb,pe,%s))"
                              %(param['t']),
                        is_quarterly=False,
                        add_data=False)
    return factor4
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 00:06:50 2018

@author: dream
"""

def run_formula(dv, param=None):
    defult_param = {'t': 20}
    if not param:
        param = defult_param

    factor11 = dv.add_formula("factor11", "StdDev((high+low)/2,%s)"
                              %(param['t']),
                        is_quarterly=False,
                        add_data=False)
    return factor11
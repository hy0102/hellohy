# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 00:05:08 2018

@author: dream
"""


def run_formula(dv, param=None):
    defult_param = {'t': 10}
    if not param:
        param = defult_param

    factor10 = dv.add_formula("factor10", "StdDev((close+open)/2,%s)"
                              %(param['t']),
                        is_quarterly=False,
                        add_data=False)
    return factor10
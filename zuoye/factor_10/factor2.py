# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 22:33:19 2018

@author: dream
"""

def run_formula(dv, param=None):
    defult_param = {'t1': 10,'t2':20}
    if not param:
        param = defult_param

    factor2 = dv.add_formula("factor2", "(close-Ts_Mean(close,%s))/(Ts_Max(close-Ts_Mean(close,%s),%s)-Ts_Min(close-Ts_Mean(close,%s),%s))"
                              %(param['t2'],param['t2'],param['t1'],param['t2'],param['t1']),
                        is_quarterly=False,
                        add_data=False)
    return factor2
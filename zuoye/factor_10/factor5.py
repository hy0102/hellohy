# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 23:44:36 2018

@author: dream
"""

def run_formula(dv):
    factor5 = dv.add_formula('factor5',
               "(((oper_rev/less_oper_cost-1)>=0.8) &&((net_profit/net_assets)>=0.2))"
               , is_quarterly=True)
    return factor5
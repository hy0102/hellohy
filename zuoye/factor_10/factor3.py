# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 22:39:34 2018

@author: dream
"""

def run_formula(dv):
    factor3 = dv.add_formula('factor3',
               "(TTM(net_cash_flows_oper_act)-TTM(net_profit))/(TTM(tot_assets)-TTM(total_liab))"
               , is_quarterly=True)
    return factor3

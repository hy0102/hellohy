def run_formula(dv, param=None):
    defult_param = {'t': 5}
    if not param:
        param = defult_param

    t = param['t']
    OperatingRevenueGrowRate5Y = dv.add_formula('OperatingRevenueGrowRate5Y',
               "(((oper_rev/Delay(oper_rev,%s))^1/5)-1)" % (t)
               , is_quarterly=False)
    return OperatingRevenueGrowRate5Y

def run_formula(dv):
    OperatingProfitPS = dv.add_formula('EOperatingProfitPS',
               "oper_profit/total_share"
               , is_quarterly=False)
    return OperatingProfitPS

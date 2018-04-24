def run_formula(dv, param=None):
    defult_param = {'t': 20}
    if not param:
        param = defult_param

    t = param['t']

    Price1M = dv.add_formula("Price1M", "(20*close_adj)/(Ts_Sum(Delay(close_adj,%s),%s))-1" % (t, t),
                        is_quarterly=False,
                        add_data=False)
    return Price1M

def run_formula(dv, param=None):
    defult_param = {'t1': 12,'t2':24}
    if not param:
        param = defult_param

    alpha183 = dv.add_formula("alpha183", "Ts_Max(Ts_Sum((close-Ts_Mean(close,%s)),%s),%s)-(Ts_Min(Ts_Sum((close-Ts_Mean(close,%s)),%s),%s)/StdDev(close,%s))"
                              %(param['t2'],param['t1'],param['t2'],param['t2'],param['t1'],param['t2'],param['t2']),
                        is_quarterly=False,
                        add_data=False)
    return alpha183
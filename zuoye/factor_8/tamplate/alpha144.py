def run_formula(dv, param=None):
    defult_param = {'t1': 1,'t2':20}
    if not param:
        param = defult_param

    alpha144 = dv.add_formula("alpha144", "Ts_Sum(If(((close<Delay(close,%s))/CountNans((close-Delay(close,%s))^0.5,%s)),Abs(close/Delay(close,%s)-1)/(close*volume),0),%s)"
                              %(param['t1'],param['t1'],param['t2'],param['t1'],param['t2']),
                        is_quarterly=False,
                        add_data=False)
    return alpha144
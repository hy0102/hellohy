def run_formula(dv, param=None):
    defult_param = {'t1': 1,'t2':12}
    if not param:
        param = defult_param

    alpha49 = dv.add_formula("alpha49", "Ts_Sum(If(((high+low)>=(Delay(high,%s)+Delay(low,%s))),0,Max(Abs(high-Delay(high,%s)),Abs(low-Delay(low,%s)))),%s)/(Ts_Sum(If(((high+low)>=(Delay(high,%s)+Delay(low,%s))),0,Max(Abs(high-Delay(high,%s)),Abs(low-Delay(low,%s)))),%s)+Ts_Sum(If(((high+low)<=(Delay(high,%s)+Delay(low,%s))),0,Max(Abs(high-Delay(high,%s)),Abs(low-Delay(low,%s)))),%s))"
                             %(param['t1'],param['t1'],param['t1'],param['t1'],param['t2'],param['t1'],param['t1'],param['t1'],param['t1'],param['t2'],param['t1'],param['t1'],param['t1'],param['t1'],param['t2']),
                        is_quarterly=False,
                        add_data=False)
    return alpha49
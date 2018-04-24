def run_formula(dv, param=None):
    defult_param = {'t1':0.9,'t2':0.1,'t3':30,'t4':10,'t5':4,'t6':7}
    if not param:
        param = defult_param

    alpha115 = dv.add_formula("alpha115", "(Rank(Corr(((high* %s)+(close* %s)),Ts_Mean(volume,%s),%s))^Rank(Corr(Ts_Rank(((high+low)/2),%s),Ts_Rank(volume,%s),%s)))"
                              %(param['t1'],param['t2'],param['t3'],param['t4'],param['t5'],param['t4'],param['t6']),
                        is_quarterly=False,
                        add_data=False)
    return alpha115
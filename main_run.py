import CuckooSearch
import numpy as np
if __name__ == '__main__':
    vardim=10
    popsize=20
    u=100
    l=-100

    bound=np.tile([[l],[u]],vardim)
    cs=CuckooSearch.CuckooSearch(popsize,vardim,bound,Maxgen=1000)
    cs.solve()

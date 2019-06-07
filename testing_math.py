import pytplot
import numpy as np

pytplot.store_data('a', data={'x':[0,4,8,12,16], 'y':[1,2,3,4,5]})
pytplot.store_data('b', data={'x':[2,5,8,11,14,17,20], 'y':[[1,1,1,1,1,1],[2,2,5,4,1,1],[100,100,3,50,1,1],[4,4,8,58,1,1],[5,5,9,21,1,1],[6,6,2,2,1,1],[7,7,1,6,1,1]]})
pytplot.store_data('c', data={'x':[0,4,8,12,16,19,21], 'y':[1,4,1,7,1,9,1]})
pytplot.store_data('d', data={'x':[2,5,8,11,14,17,21], 'y':[[1,1,50],[2,2,3],[100,4,47],[4,90,5],[5,5,99],[6,6,25],[7,7,-5]]})
pytplot.store_data('e', data={'x':[2,5,8,11,14,17,21], 'y':[[np.nan,1,1],[np.nan,2,3],[4,np.nan,47],[4,np.nan,5],[5,5,99],[6,6,25],[7,np.nan,-5]]})
pytplot.store_data('g', data={'x':[0,4,8,12,16,19,21], 'y':[[8,1,1],[100,2,3],[4,2,47],[4,39,5],[5,5,99],[6,6,25],[7,-2,-5]]})
pytplot.store_data('h', data={'x':[0,4,8,12,16,19,21], 'y':[[8,1,1],[100,2,3],[4,2,47],[4,39,5],[5,5,99],[6,6,25],[7,-2,-5]],'v':[[1,1,50],[2,2,3],[100,4,47],[4,90,5],[5,5,99],[6,6,25],[7,7,-5]]})



pytplot.spec_mult('h','h_specmult')
print(pytplot.data_quants['h_specmult'].data)
# Copyright 2018 Regents of the University of Colorado. All Rights Reserved.
# Released under the MIT license.
# This software was developed at the University of Colorado's Laboratory for Atmospheric and Space Physics.
# Verify current version before use at: https://github.com/MAVENSDC/Pytplot

import pytplot
import numpy as np
import pandas as pd
import copy
    
def degap(tvar,dt,margin,func='nan',new_tvar = None):
    '''
    Fills data within margin(s) where data may not be correct.

    Required Arguments:
        tvar : str
            Name of tvar to modify.
        dt : int/float
            Step size of the data in seconds
        margin : int/float
            The maximum deviation from the step size allowed before degapping occurs

    Optional Arguments:
        func : str
            Either 'nan' or 'ffill', which overrides normal interpolation with NaN
            substitution or forward-filled values.
    Returns:
        None
    '''

    gap_size = np.diff(pytplot.data_quants[tvar].coords['time'])
    gap_index_locations = np.where(gap_size > dt+margin)
    new_tvar_index = pytplot.data_quants[tvar].coords['time']
    values_to_add = np.array([])
    for i in gap_index_locations[0]:
        values_to_add = np.append(values_to_add, np.arange(new_tvar_index[i], new_tvar_index[i+1], dt))

    new_index = np.sort(np.unique(np.concatenate((values_to_add, new_tvar_index))))

    if func == 'nan':
        method = None
    if func == 'ffill':
        method = 'ffill'

    a = pytplot.data_quants[tvar].reindex({'time': new_index}, method=method)

    if new_tvar is None:
        pytplot.data_quants[tvar] = a
    else:
        if 'spec_bins' in a.coords:
            pytplot.store_data(new_tvar, data={'x': a.coords['time'], 'y': a.values, 'v': a.coords['spec_bins']})
        else:
            pytplot.store_data(new_tvar, data={'x': a.coords['time'], 'y': a.values})

    return
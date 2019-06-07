import pytplot
import os

current_directory = os.path.dirname(os.path.realpath(__file__))

def test_tplot_math():

    pytplot.cdf_to_tplot(os.path.dirname(os.path.realpath(__file__)) + "/testfiles/mvn_euv_l2_bands_20170619_v09_r03.cdf")
    pytplot.tplot_names()

    pytplot.tplot_math.split_vec('data')

    pytplot.tplot('data_0', testing=True)

    pytplot.tplot_math.subtract('data_0', 'data_1', new_tvar='s')

    pytplot.tplot('s', testing=True)

    pytplot.tplot_math.add('s', 'data_1', new_tvar='a')

    pytplot.tplot(['data_0', 'a'], testing=True)

    pytplot.tplot_math.subtract('data_0', 'data_2', new_tvar='m')

    pytplot.tplot('m', testing=True)

    pytplot.tplot_math.divide('m', 'data_2', new_tvar='d')

    pytplot.tplot('d', testing=True)

    pytplot.add_across('data')

    pytplot.tplot('data_summed', testing=True)

    pytplot.avg_res_data('data_summed', res=120)

    pytplot.tplot('data_summed', testing=True)

    pytplot.deflag('data', 0, new_tvar='deflagged')

    pytplot.tplot('deflagged', testing=True)

    pytplot.flatten('data')

    pytplot.tplot('data_flattened', testing=True)

    pytplot.join_vec(['data_0', 'data_1', 'data_2'], new_tvar='data2')

    pytplot.tplot('data2', testing=True)

    pytplot.pwr_spec('data_0')

    pytplot.tplot('data_0_pwrspec', testing=True)

    pytplot.derive('data_0')

    pytplot.store_data("data3", data=['data_0', 'data_1', 'data_2'])

    pytplot.tplot('data3', testing=True)

    pytplot.cdf_to_tplot(os.path.dirname(os.path.realpath(__file__))+ "/testfiles/mvn_swe_l2_svyspec_20170619_v04_r04.cdf")

    pytplot.resample('data_1', pytplot.data_quants['diff_en_fluxes'].coords['time'].values, new_tvar='data_3_resampled')

    pytplot.tplot('data_3_resampled', testing=True)

    pytplot.spec_mult('diff_en_fluxes')

    pytplot.add_across('diff_en_fluxes_specmult', new_tvar='tot_en_flux', column_range=[[0, 10], [10, 20], [20, 30]])
    pytplot.options('diff_en_fluxes', 'spec', 1)
    pytplot.options('diff_en_fluxes', 'ylog', 1)
    pytplot.options('diff_en_fluxes', 'zlog', 1)
    pytplot.options('tot_en_flux', 'ylog', 1)
    pytplot.ylim('tot_en_flux', 1, 100)
    pytplot.tplot(['diff_en_fluxes', 'tot_en_flux'], testing=True)

    pytplot.split_vec('tot_en_flux')

    pytplot.add('tot_en_flux_0', 'data_1', new_tvar='weird_data')

    pytplot.tplot('weird_data', testing=True)
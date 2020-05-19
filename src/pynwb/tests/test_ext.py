import os
from pynwb import NWBHDF5IO, NWBFile
from datetime import datetime
from ndx_survey_data import NRSDataTable, VASDataTable, MPQDataTable
from numpy.testing import assert_array_equal


def test_ext():
    nwbfile = NWBFile('description', 'id', datetime.now().astimezone())

    # NRS Survey

    nrs_data_table = NRSDataTable(name='nrs_data_table',
                                  description='desc',
                                  response_options=['0 = no pain, 10 = worst pain',
                                                    '0 = no paint relief, 10 = complete pain relief',
                                                    '0 = better, 5 = same, 10 = worse',
                                                    '0 = pleasant, 10 = unpleasant'])

    nrs_data_table.add_row(pain_intensity_rating='2',
                           pain_relief_rating='7',
                           relative_pain_intensity_rating='5',
                           pain_unpleasantness='9')
    nrs_data_table.add_row(pain_intensity_rating='1',
                           pain_relief_rating='2',
                           relative_pain_intensity_rating='4',
                           pain_unpleasantness='3')
    nrs_data_table.add_row(pain_intensity_rating='8',
                           pain_relief_rating='9',
                           relative_pain_intensity_rating='10',
                           pain_unpleasantness='7')

    # VAS Survey

    vas_data_table = VASDataTable(name='vas_data_table',
                                  description='desc',
                                  response_options=['‘No pain’ to ‘Worst pain possible’',
                                                    '‘No pain relief’ to ‘Complete pain relief’',
                                                    'Better – Same – Worse',
                                                    '‘Pleasant’ to ‘Unpleasant’'])

    vas_data_table.add_row(pain_intensity_rating='20/50',
                           pain_relief_rating='12/50',
                           relative_pain_intensity_rating='45/50',
                           pain_unpleasantness='9/50')
    vas_data_table.add_row(pain_intensity_rating='6/50',
                           pain_relief_rating='22/50',
                           relative_pain_intensity_rating='34/50',
                           pain_unpleasantness='3/50')
    vas_data_table.add_row(pain_intensity_rating='8/50',
                           pain_relief_rating='29/50',
                           relative_pain_intensity_rating='10/50',
                           pain_unpleasantness='37/50')

    # MPQ Survey

    mpq_data_table = MPQDataTable(name='mpq_data_table',
                                  description='desc',
                                  response_options=['Mild', 'Moderate', 'Severe'])

    mpq_data_table.add_row(throbbing='Mild', shooting='Severe', stabbing='Moderate',
                           sharp='Moderate', cramping='Severe', gnawing='Mild',
                           hot_burning='Mild', aching='Moderate', heavy='Mild',
                           tender='Moderate', splitting='Severe', tiring_exhausting='Severe',
                           sickening='Mild', fearful='Mild', cruel_punishing='Severe')
    mpq_data_table.add_row(throbbing='Severe', shooting='Severe', stabbing='Mild',
                           sharp='Moderate', cramping='Mild', gnawing='Mild',
                           hot_burning='Mild', aching='Severe', heavy='Moderate',
                           tender='Severe', splitting='Mild', tiring_exhausting='Mild',
                           sickening='Moderate', fearful='Mild', cruel_punishing='Moderate')
    mpq_data_table.add_row(throbbing='Moderate', shooting='Mild', stabbing='Severe',
                           sharp='Moderate', cramping='Severe', gnawing='Severe',
                           hot_burning='Severe', aching='Mild', heavy='Moderate',
                           tender='Mild', splitting='Mild', tiring_exhausting='Mild',
                           sickening='Mild', fearful='Severe', cruel_punishing='Moderate')

    nwbfile.create_processing_module(name='behavior', description='survey/behavioral data')

    nwbfile.processing['behavior'].add(nrs_data_table)
    nwbfile.processing['behavior'].add(vas_data_table)
    nwbfile.processing['behavior'].add(mpq_data_table)

    with NWBHDF5IO('test_nwb.nwb', 'w') as io:
        io.write(nwbfile)

    with NWBHDF5IO('test_nwb.nwb', 'r', load_namespaces=True) as io:
        nwbfile = io.read()
        assert_array_equal(nwbfile.processing['behavior'].data_interfaces['nrs_data_table']['pain_intensity_rating'],
                           '2')

    os.remove('test_nwb.nwb')

import os
from pynwb import NWBHDF5IO, NWBFile
from pynwb.file import DynamicTableRegion
from datetime import datetime
from ndx_survey_data import SurveyDataTable

import numpy as np
from numpy.testing import assert_array_equal


def test_ext():
    nwbfile = NWBFile('description', 'id', datetime.now().astimezone())

    survey_data_table = SurveyDataTable(name='survey_data_table',
                                              description='desc')

    survey_data_table.add_row(questions='question1', responses='response1')
    survey_data_table.add_row(questions='question2', responses='response2')
    survey_data_table.add_row(questions='question3', responses='response3')
    
    behavior_module = nwbfile.create_processing_module(name='behavior',
                                                   description='survey/behavioral data')
    
    nwbfile.processing['behavior'].add(survey_data_table)

    with NWBHDF5IO('test_nwb.nwb', 'w') as io:
        io.write(nwbfile)

    with NWBHDF5IO('test_nwb.nwb', 'r', load_namespaces=True) as io:
        nwbfile = io.read()
        assert_array_equal(nwbfile.processing['behavior'].data_interfaces['survey_data_table'][2]['questions'],'question3')

    os.remove('test_nwb.nwb')

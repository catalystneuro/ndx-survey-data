import os
from pynwb import NWBHDF5IO, NWBFile
from datetime import datetime
from ndx_survey_data.survey_data import SurveyTable, QuestionResponse
from ndx_survey_data.survey_definitions import nrs_survey_table


def nrs_test_ext():

    nwbfile = NWBFile('description', 'id', datetime.now().astimezone())

    nrs_survey_table.add_row(
        nrs_pain_intensity_rating=1,
        nrs_pain_relief_rating=5,
        nrs_relative_pain_intensity_rating=2,
        nrs_pain_unpleasantness=3,
        unix_timestamp=1588217283
    )

    nrs_survey_table.add_row(
        nrs_pain_intensity_rating=3,
        nrs_pain_relief_rating=1,
        nrs_relative_pain_intensity_rating=6,
        nrs_pain_unpleasantness=2,
        unix_timestamp=1588217283
    )

    nrs_survey_table.add_row(
        nrs_pain_intensity_rating=5,
        nrs_pain_relief_rating=2,
        nrs_relative_pain_intensity_rating=0,
        nrs_pain_unpleasantness=2,
        unix_timestamp=1588217283
    )

    nrs_survey_table.add_row(
        nrs_pain_intensity_rating=3,
        nrs_pain_relief_rating=1,
        nrs_relative_pain_intensity_rating=6,
        nrs_pain_unpleasantness=2,
        unix_timestamp=1588217283
    )

    nwbfile.create_processing_module(name='behavior', description='survey/behavioral data')

    nwbfile.processing['behavior'].add(nrs_survey_table)

    with NWBHDF5IO('test_nwb.nwb', 'w') as io:
        io.write(nwbfile)

    with NWBHDF5IO('test_nwb.nwb', 'r', load_namespaces=True) as io:
        nwbfile = io.read()

        read_table = nwbfile.processing['behavior'].data_interfaces['nrs_survey_table']

        assert(nrs_survey_table == read_table)


def custom_test_ext():

    nwbfile = NWBFile('description', 'id', datetime.now().astimezone())

    q1 = QuestionResponse(name='question 1',
                          description='desc',
                          options=['option 1', 'option 2', 'option 3'])

    q2 = QuestionResponse(name='question 2',
                          description='desc',
                          options=['option 1', 'option 2', 'option 3'])

    q3 = QuestionResponse(name='question 3',
                          description='desc',
                          options=['option 1', 'option 2', 'option 3'])

    custom_survey_table = SurveyTable(name='custom_survey_table',
                                      description='desc',
                                      columns=[q1, q2, q3])

    custom_survey_table.add_row(q1=1, q2=3, q3=0, unix_timestamp=1588217283)
    custom_survey_table.add_row(q1=3, q2=1, q3=0, unix_timestamp=1588217283)
    custom_survey_table.add_row(q1=2, q2=2, q3=2, unix_timestamp=1588217283)

    nwbfile.create_processing_module(name='behavior', description='survey/behavioral data')

    nwbfile.processing['behavior'].add(custom_survey_table)

    with NWBHDF5IO('test_nwb.nwb', 'w') as io:
        io.write(nwbfile)

    with NWBHDF5IO('test_nwb.nwb', 'r', load_namespaces=True) as io:
        nwbfile = io.read()

        read_table = nwbfile.processing['behavior'].data_interfaces['custom_survey_table']

        assert(custom_survey_table == read_table)

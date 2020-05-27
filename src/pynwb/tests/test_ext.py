import os
from pynwb import NWBHDF5IO, NWBFile
from datetime import datetime
from ndx_survey_data import SurveyTable, QuestionResponse
from numpy.testing import assert_array_equal


def test_ext():

    nwbfile = NWBFile('description', 'id', datetime.now().astimezone())

    pain_intensity_rating = QuestionResponse(name='pain_intensity_rating',
                                             description='desc',
                                             options=['no pain', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                                      'worst pain'])

    pain_relief_rating = QuestionResponse(name='pain_relief_rating',
                                          description='desc',
                                          options=['no pain relief', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                                   'complete pain relief'])

    relative_pain_intensity_rating = QuestionResponse(name='relative_pain_intensity_rating',
                                                      description='desc',
                                                      options=['better', '1', '2', '3', '4', 'same', '6', '7', '8', '9',
                                                               'worse'])

    pain_unpleasantness = QuestionResponse(name='pain_unpleasantness',
                                           description='desc',
                                           options=['pleasant', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                                    'unpleasant'])

    nrs_survey_table = SurveyTable(name='nrs_survey_table',
                                   description='desc',
                                   columns=[
                                       pain_intensity_rating,
                                       pain_relief_rating,
                                       relative_pain_intensity_rating,
                                       pain_unpleasantness
                                   ])

    nrs_survey_table.add_row(
        pain_intensity_rating=1,
        pain_relief_rating=5,
        relative_pain_intensity_rating=2,
        pain_unpleasantness=3,
        unix_timestamp=1588217283
    )

    nrs_survey_table.add_row(
        pain_intensity_rating=3,
        pain_relief_rating=1,
        relative_pain_intensity_rating=6,
        pain_unpleasantness=2,
        unix_timestamp=1588217283
    )

    nrs_survey_table.add_row(
        pain_intensity_rating=5,
        pain_relief_rating=2,
        relative_pain_intensity_rating=0,
        pain_unpleasantness=2,
        unix_timestamp=1588217283
    )

    nrs_survey_table.add_row(
        pain_intensity_rating=3,
        pain_relief_rating=1,
        relative_pain_intensity_rating=6,
        pain_unpleasantness=2,
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

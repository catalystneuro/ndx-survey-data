import os
from pynwb import NWBHDF5IO, NWBFile
from datetime import datetime
from ndx_survey_data import SurveyTable, QuestionResponse
from ndx_survey_data.survey_definitions import nrs_survey_table


def test_ext_nrs():

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



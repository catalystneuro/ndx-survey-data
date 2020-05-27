# -*- coding: utf-8 -*-

import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBDatasetSpec, NWBAttributeSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc='NWB extension for survey/behavioral data',
        name='ndx-survey-data',
        version='0.1.0',
        author=list(map(str.strip, 'Ben Dichter, Armin Najarpour Foroushani'.split(','))),
        contact=list(map(str.strip, 'ben.dichter@catalystneuro.com'.split(',')))
    )

    for type_name in ('DynamicTable', 'VectorData'):
        ns_builder.include_type(type_name, namespace='core')

    survey_data = NWBGroupSpec(
        doc='Table that holds information about the survey/behavior',
        neurodata_type_def='SurveyTable',
        neurodata_type_inc='DynamicTable',
        default_name='survey_data'
    )

    question_response = NWBDatasetSpec(
        doc='Column that holds information about a question',
        neurodata_type_def='QuestionResponse',
        neurodata_type_inc='VectorData',
        default_name='question_response',
        attributes=[NWBAttributeSpec(name='options',
                                     doc='Response Options',
                                     dtype='text',
                                     shape=(None,),
                                     dims=('num_options',))]
    )

    survey_data.add_dataset(
        neurodata_type_inc='VectorData',
        doc='UNIX time of survey response',
        name='unix_timestamp',
        dtype='int',
        shape=(None,),
        dims=('num_responses',)
    )

    new_data_types = [survey_data, question_response]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()

# -*- coding: utf-8 -*-

import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc='NWB extension for survey/ behavioral data',
        name='ndx-survey-data',
        version='0.1.0',
        author=list(map(str.strip, 'Ben Dichter, Armin Najarpour Foroushani'.split(','))),
        contact=list(map(str.strip, 'ben.dichter@catalystneuro.com'.split(',')))
    )

    
    for type_name in ('DynamicTableRegion', 'DynamicTable'):
        ns_builder.include_type(type_name, namespace='core')

    
    survey_data = NWBGroupSpec(
        doc='Table that holds information about the survey/behavior',
        neurodata_type_def='SurveyDataTable',
        neurodata_type_inc='DynamicTable',
        default_name='survey_data'
   )
    
    survey_data.add_dataset(
        name='survey_name',
        neurodata_type_inc='DynamicTableRegion',
        doc='Name of survey',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='question_text',
        neurodata_type_inc='DynamicTableRegion',
        doc='Text of survey question',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    survey_data.add_dataset(
        name='response_range',
        neurodata_type_inc='DynamicTableRegion',
        doc='Limits or range of survey response (e.g. 0 to 10; ‘no pain’ to ‘worst pain possible’)',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    survey_data.add_dataset(
        name='response',
        neurodata_type_inc='DynamicTableRegion',
        doc='Response to survey question',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    survey_data.add_dataset(
        name='response_timestamp',
        neurodata_type_inc='DynamicTableRegion',
        doc='Timestamp of survey response',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    survey_data.add_dataset(
        name='notes',
        neurodata_type_inc='DynamicTableRegion',
        doc='An indication of how to calculate subscore(s), if applicable',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    new_data_types = [survey_data]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()

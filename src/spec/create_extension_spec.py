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
        name='questions',
        neurodata_type_inc='DynamicTableRegion',
        doc='Survey questions',
        dims=('num_questions',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='responses',
        neurodata_type_inc='DynamicTableRegion',
        doc='Response to survey questions',
        dims=('num_questions',),
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

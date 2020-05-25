# -*- coding: utf-8 -*-

import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc='NWB extension for survey/ behavioral data',
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
        default_name='survey_data',
        groups=[NWBGroupSpec(
                name='question_response_col',
                neurodata_type_inc='QuestionResponse',
                doc='Question response column',
                quantity='?')]
    )

    question_response = NWBGroupSpec(
        doc='Column that holds information about a question',
        neurodata_type_def='QuestionResponse',
        neurodata_type_inc='VectorData',
        default_name='question_response',
        attributes=[NWBAttributeSpec(name='options',
                                     doc='Response Options',
                                     dtype='text')]
    )

    survey_data.add_dataset(
        name='nrs_pain_intensity_rating',
        neurodata_type_inc='QuestionResponse',
        doc='NRS Pain Intensity Rating',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='nrs_pain_relief_rating',
        neurodata_type_inc='QuestionResponse',
        doc='NRS Pain Relief Rating',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='nrs_relative_pain_intensity_rating',
        neurodata_type_inc='QuestionResponse',
        doc='NRS Relative Pain Intensity Rating',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='nrs_pain_unpleasantness',
        neurodata_type_inc='QuestionResponse',
        doc='NRS Pain Unpleasantness',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='vas_pain_intensity_rating',
        neurodata_type_inc='QuestionResponse',
        doc='VAS Pain Intensity Rating',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='vas_pain_relief_rating',
        neurodata_type_inc='QuestionResponse',
        doc='VAS Pain Relief Rating',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='vas_relative_pain_intensity_rating',
        neurodata_type_inc='QuestionResponse',
        doc='VAS Relative Pain Intensity Rating',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='vas_pain_unpleasantness',
        neurodata_type_inc='QuestionResponse',
        doc='VAS Pain Unpleasantness',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='throbbing',
        neurodata_type_inc='QuestionResponse',
        doc='Throbbing',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='shooting',
        neurodata_type_inc='QuestionResponse',
        doc='Shooting',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='stabbing',
        neurodata_type_inc='QuestionResponse',
        doc='Stabbing',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='sharp',
        neurodata_type_inc='QuestionResponse',
        doc='Sharp',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='cramping',
        neurodata_type_inc='QuestionResponse',
        doc='Cramping',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='gnawing',
        neurodata_type_inc='QuestionResponse',
        doc='Gnawing',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='hot_burning',
        neurodata_type_inc='QuestionResponse',
        doc='Hot-burning',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='aching',
        neurodata_type_inc='QuestionResponse',
        doc='Aching',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='heavy',
        neurodata_type_inc='QuestionResponse',
        doc='Heavy',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='tender',
        neurodata_type_inc='QuestionResponse',
        doc='Tender',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='splitting',
        neurodata_type_inc='QuestionResponse',
        doc='Splitting',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='tiring_exhausting',
        neurodata_type_inc='QuestionResponse',
        doc='Tiring-Exhausting',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='sickening',
        neurodata_type_inc='QuestionResponse',
        doc='Sickening',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='fearful',
        neurodata_type_inc='QuestionResponse',
        doc='Fearful',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='cruel_punishing',
        neurodata_type_inc='QuestionResponse',
        doc='Cruel-Punishing',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    new_data_types = [survey_data, question_response]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()

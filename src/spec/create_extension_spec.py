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
        neurodata_type_def='SurveyDataTable',
        neurodata_type_inc='DynamicTable',
        default_name='survey_data'
    )

    survey_data.add_dataset(
        name='nrs_pain_intensity_rating',
        neurodata_type_inc='VectorData',
        doc='NRS Pain Intensity Rating',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='nrs_pain_relief_rating',
        neurodata_type_inc='VectorData',
        doc='NRS Pain Relief Rating',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='nrs_relative_pain_intensity_rating',
        neurodata_type_inc='VectorData',
        doc='NRS Relative Pain Intensity Rating',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='nrs_pain_unpleasantness',
        neurodata_type_inc='VectorData',
        doc='NRS Pain Unpleasantness',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='vas_pain_intensity_rating',
        neurodata_type_inc='VectorData',
        doc='VAS Pain Intensity Rating',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='vas_pain_relief_rating',
        neurodata_type_inc='VectorData',
        doc='VAS Pain Relief Rating',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='vas_relative_pain_intensity_rating',
        neurodata_type_inc='VectorData',
        doc='VAS Relative Pain Intensity Rating',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='vas_pain_unpleasantness',
        neurodata_type_inc='VectorData',
        doc='VAS Pain Unpleasantness',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='throbbing',
        neurodata_type_inc='VectorData',
        doc='Throbbing',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='shooting',
        neurodata_type_inc='VectorData',
        doc='Shooting',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='stabbing',
        neurodata_type_inc='VectorData',
        doc='Stabbing',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='sharp',
        neurodata_type_inc='VectorData',
        doc='Sharp',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='cramping',
        neurodata_type_inc='VectorData',
        doc='Cramping',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='gnawing',
        neurodata_type_inc='VectorData',
        doc='Gnawing',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='hot_burning',
        neurodata_type_inc='VectorData',
        doc='Hot-burning',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='aching',
        neurodata_type_inc='VectorData',
        doc='Aching',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='heavy',
        neurodata_type_inc='VectorData',
        doc='Heavy',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='tender',
        neurodata_type_inc='VectorData',
        doc='Tender',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='splitting',
        neurodata_type_inc='VectorData',
        doc='Splitting',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='tiring_exhausting',
        neurodata_type_inc='VectorData',
        doc='Tiring-Exhausting',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='sickening',
        neurodata_type_inc='VectorData',
        doc='Sickening',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='fearful',
        neurodata_type_inc='VectorData',
        doc='Fearful',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    survey_data.add_dataset(
        name='cruel_punishing',
        neurodata_type_inc='VectorData',
        doc='Cruel-Punishing',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                     dtype='text')],
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

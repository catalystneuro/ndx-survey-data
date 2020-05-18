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

    
    for type_name in ('DynamicTableRegion', 'DynamicTable', 'VectorData'):
        ns_builder.include_type(type_name, namespace='core')

    
    nrs_survey = NWBGroupSpec(
        doc='Table that holds information about the NRS survey',
        neurodata_type_def='NRSDataTable',
        neurodata_type_inc='DynamicTable',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                    dtype='str')],
        default_name='nrs_survey'
   )
    
    nrs_survey.add_dataset(
        name='pain_intensity_rating',
        neurodata_type_inc='VectorData',
        doc='Pain Intensity Rating',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    nrs_survey.add_dataset(
        name='pain_relief_rating',
        neurodata_type_inc='VectorData',
        doc='Pain Relief Rating',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    nrs_survey.add_dataset(
        name='relative_pain_intensity_rating',
        neurodata_type_inc='VectorData',
        doc='Relative Pain Intensity Rating',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    nrs_survey.add_dataset(
        name='pain_unpleasantness',
        neurodata_type_inc='VectorData',
        doc='Pain Unpleasantness',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    
    
    
    
    vas_survey = NWBGroupSpec(
        doc='Table that holds information about the VAS survey',
        neurodata_type_def='VASDataTable',
        neurodata_type_inc='DynamicTable',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                    dtype='str')],
        default_name='vas_survey'
   )
    
    vas_survey.add_dataset(
        name='pain_intensity_rating',
        neurodata_type_inc='VectorData',
        doc='Pain Intensity Rating',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    vas_survey.add_dataset(
        name='pain_relief_rating',
        neurodata_type_inc='VectorData',
        doc='Pain Relief Rating',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    vas_survey.add_dataset(
        name='relative_pain_intensity_rating',
        neurodata_type_inc='VectorData',
        doc='Relative Pain Intensity Rating',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    vas_survey.add_dataset(
        name='pain_unpleasantness',
        neurodata_type_inc='VectorData',
        doc='Pain Unpleasantness',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    
    
    
    
    
    
    mpq_survey = NWBGroupSpec(
        doc='Table that holds information about the MPQ survey',
        neurodata_type_def='MPQDataTable',
        neurodata_type_inc='DynamicTable',
        attributes=[NWBAttributeSpec(name='response_options',
                                     doc='Response Options',
                                    dtype='str')],
        default_name='mpq_survey'
   )
    
    mpq_survey.add_dataset(
        name='throbbing',
        neurodata_type_inc='VectorData',
        doc='Throbbing',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )

    mpq_survey.add_dataset(
        name='shooting',
        neurodata_type_inc='VectorData',
        doc='Shooting',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    mpq_survey.add_dataset(
        name='stabbing',
        neurodata_type_inc='VectorData',
        doc='Stabbing',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    mpq_survey.add_dataset(
        name='sharp',
        neurodata_type_inc='VectorData',
        doc='Sharp',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    mpq_survey.add_dataset(
        name='cramping',
        neurodata_type_inc='VectorData',
        doc='Cramping',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    mpq_survey.add_dataset(
        name='gnawing',
        neurodata_type_inc='VectorData',
        doc='Gnawing',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    mpq_survey.add_dataset(
        name='hot_burning',
        neurodata_type_inc='VectorData',
        doc='Hot-burning',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    mpq_survey.add_dataset(
        name='aching',
        neurodata_type_inc='VectorData',
        doc='Aching',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    mpq_survey.add_dataset(
        name='heavy',
        neurodata_type_inc='VectorData',
        doc='Heavy',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    mpq_survey.add_dataset(
        name='tender',
        neurodata_type_inc='VectorData',
        doc='Tender',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    mpq_survey.add_dataset(
        name='splitting',
        neurodata_type_inc='VectorData',
        doc='Splitting',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    mpq_survey.add_dataset(
        name='tiring_exhausting',
        neurodata_type_inc='VectorData',
        doc='Tiring-Exhausting',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    mpq_survey.add_dataset(
        name='sickening',
        neurodata_type_inc='VectorData',
        doc='Sickening',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    mpq_survey.add_dataset(
        name='fearful',
        neurodata_type_inc='VectorData',
        doc='Fearful',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    mpq_survey.add_dataset(
        name='cruel_punishing',
        neurodata_type_inc='VectorData',
        doc='Cruel-Punishing',
        dims=('num_samples',),
        shape=(None,),
        dtype='text'
    )
    
    

    new_data_types = [nrs_survey, vas_survey, mpq_survey]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()

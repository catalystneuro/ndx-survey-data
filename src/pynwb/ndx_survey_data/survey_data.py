from pynwb import register_class
from pynwb.file import DynamicTable
from hdmf.utils import docval, call_docval_func, get_docval, getargs



@register_class('NRSDataTable', 'ndx-survey-data')
class NRSDataTable(DynamicTable):
    """
    Table for storing NRS survey data
    """
    __nwbfields__ = ('response_options',)

    __columns__ = (
        {'name': 'pain_intensity_rating', 'description': 'Pain Intensity Rating', 'required': True, 'index': False},
        {'name': 'pain_relief_rating', 'description': 'Pain Relief Rating', 'required': True, 'index': False},
        {'name': 'relative_pain_intensity_rating', 'description': 'Relative Pain Intensity Rating', 'required': True, 'index': False},
        {'name': 'pain_unpleasantness', 'description': 'Pain Unpleasantness', 'required': True, 'index': False}
    )

    @docval(dict(name='name', type=str, doc='name of this NRSDataTable',
                 default='NRSDataTable'),  # required
            dict(name='response_options', type=list, doc='Response Options'),
            dict(name='description', type=str, doc='Description of this VectorData',
                 default='references the NRS survey table'),
            *get_docval(DynamicTable.__init__, 'id', 'columns', 'colnames'))
    def __init__(self, **kwargs):
        call_docval_func(super(NRSDataTable, self).__init__, kwargs)
        self.response_options = getargs('response_options', kwargs)



@register_class('VASDataTable', 'ndx-survey-data')
class VASDataTable(DynamicTable):
    """
    Table for storing VAS survey data
    """
    __nwbfields__ = ('response_options',)

    __columns__ = (
        {'name': 'pain_intensity_rating', 'description': 'Pain Intensity Rating', 'required': True, 'index': False},
        {'name': 'pain_relief_rating', 'description': 'Pain Relief Rating', 'required': True, 'index': False},
        {'name': 'relative_pain_intensity_rating', 'description': 'Relative Pain Intensity Rating', 'required': True, 'index': False},
        {'name': 'pain_unpleasantness', 'description': 'Pain Unpleasantness', 'required': True, 'index': False}
    )

    @docval(dict(name='name', type=str, doc='name of this VASDataTable',
                 default='VASDataTable'),  # required
            dict(name='response_options', type=list, doc='Response Options'),
            dict(name='description', type=str, doc='Description of this VectorData',
                 default='references the VAS survey table'),
            *get_docval(DynamicTable.__init__, 'id', 'columns', 'colnames'))
    def __init__(self, **kwargs):
        call_docval_func(super(VASDataTable, self).__init__, kwargs)
        self.response_options = getargs('response_options', kwargs)
        



@register_class('MPQDataTable', 'ndx-survey-data')
class MPQDataTable(DynamicTable):
    """
    Table for storing MPQ survey data
    """
    __nwbfields__ = ('response_options',)

    __columns__ = (
        {'name': 'throbbing', 'description': 'Throbbing', 'required': False, 'index': False},
        {'name': 'shooting', 'description': 'Shooting', 'required': False, 'index': False},
        {'name': 'stabbing', 'description': 'Stabbing', 'required': False, 'index': False},
        {'name': 'sharp', 'description': 'Sharp', 'required': False, 'index': False},
        {'name': 'cramping', 'description': 'Cramping', 'required': False, 'index': False},
        {'name': 'gnawing', 'description': 'Gnawing', 'required': False, 'index': False},
        {'name': 'hot_burning', 'description': 'Hot-burning', 'required': False, 'index': False},
        {'name': 'aching', 'description': 'Aching', 'required': False, 'index': False},
        {'name': 'heavy', 'description': 'Heavy', 'required': False, 'index': False},
        {'name': 'tender', 'description': 'Tender', 'required': False, 'index': False},
        {'name': 'splitting', 'description': 'Splitting', 'required': False, 'index': False},
        {'name': 'tiring_exhausting', 'description': 'Tiring-Exhausting', 'required': False, 'index': False},
        {'name': 'sickening', 'description': 'Sickening', 'required': False, 'index': False},
        {'name': 'fearful', 'description': 'Fearful', 'required': False, 'index': False},
        {'name': 'cruel_punishing', 'description': 'Cruel-Punishing', 'required': False, 'index': False}
    )

    @docval(dict(name='name', type=str, doc='name of this MPQDataTable',
                 default='MPQDataTable'),  # required
            dict(name='response_options', type=list, doc='Response Options'),
            dict(name='description', type=str, doc='Description of this VectorData',
                 default='references the MPQ survey table'),
            *get_docval(DynamicTable.__init__, 'id', 'columns', 'colnames'))
    def __init__(self, **kwargs):
        call_docval_func(super(MPQDataTable, self).__init__, kwargs)
        self.response_options = getargs('response_options', kwargs)

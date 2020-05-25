from pynwb import register_class
from pynwb.file import DynamicTable
from hdmf.utils import docval, call_docval_func, get_docval


@register_class('SurveyDataTable', 'ndx-survey-data')
class SurveyDataTable(DynamicTable):
    """
    Table for storing survey data
    """

    __columns__ = (
        {'name': 'nrs_pain_intensity_rating', 'description': 'NRS Pain Intensity Rating', 'required': True, 'index': False},
        {'name': 'nrs_pain_relief_rating', 'description': 'NRS Pain Relief Rating', 'required': True, 'index': False},
        {'name': 'nrs_relative_pain_intensity_rating', 'description': 'NRS Relative Pain Intensity Rating', 'required': True, 'index': False},
        {'name': 'nrs_pain_unpleasantness', 'description': 'NRS Pain Unpleasantness', 'required': True, 'index': False},
        {'name': 'vas_pain_intensity_rating', 'description': 'VAS Pain Intensity Rating', 'required': True, 'index': False},
        {'name': 'vas_pain_relief_rating', 'description': 'VAS Pain Relief Rating', 'required': True, 'index': False},
        {'name': 'vas_relative_pain_intensity_rating', 'description': 'VAS Relative Pain Intensity Rating', 'required': True, 'index': False},
        {'name': 'vas_pain_unpleasantness', 'description': 'VAS Pain Unpleasantness', 'required': True, 'index': False},
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

    @docval(dict(name='name', type=str, doc='name of this SurveyDataTable',
                 default='SurveyDataTable'),  # required
            dict(name='description', type=str, doc='Description of this VectorData',
                 default='references the survey table'),
            *get_docval(DynamicTable.__init__, 'id', 'columns', 'colnames'))
    def __init__(self, **kwargs):
        call_docval_func(super(SurveyDataTable, self).__init__, kwargs)

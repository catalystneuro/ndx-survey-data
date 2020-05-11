from pynwb import register_class
from pynwb.file import LabMetaData, DynamicTable
from hdmf.utils import docval, call_docval_func, get_docval


@register_class('SurveyDataTable', 'ndx-survey-data')
class SurveyDataTable(DynamicTable):
    """
    Table for storing survey/behavioral data
    """

    __columns__ = (
        {'name': 'questions', 'description': 'Survey questions', 'required': True, 'index': False},
        {'name': 'responses', 'description': 'Response to survey questions', 'required': True, 'index': False}
    )

    @docval(dict(name='name', type=str, doc='name of this SurveyDataTable',
                 default='SurveyDataTable'),  # required
            dict(name='description', type=str, doc='Description of this DynamicTableRegion',
                 default='references the survey table'),
            *get_docval(DynamicTable.__init__, 'id', 'columns', 'colnames'))
    def __init__(self, **kwargs):
        call_docval_func(super(SurveyDataTable, self).__init__, kwargs)

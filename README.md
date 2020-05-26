# ndx-survey-data Extension for NWB

Structure for storing the survey data in a NWB file.

![schema schema](https://github.com/Armin12/ndx-survey-data/blob/match_data/docs/media/survey_data.png?raw=true)


## Installation
```bash
$ pip install ndx-survey-data
```

## Usage

```python
from pynwb import NWBHDF5IO, NWBFile
from datetime import datetime
from ndx_survey_data import SurveyTable, QuestionResponse

nwbfile = NWBFile('description', 'id', datetime.now().astimezone())

nrs_survey_table = SurveyTable(name='nrs_survey_table', description='desc')

pain_intensity_rating = QuestionResponse(name='pain_intensity_rating', 
                                         description='desc',
                                         options='0 = no pain, 10 = worst pain')
pain_intensity_rating.add_row('2')
pain_intensity_rating.add_row('1')
pain_intensity_rating.add_row('8')

pain_relief_rating = QuestionResponse(name='pain_relief_rating', 
                                             description='desc',
                                             options='0 = no paint relief, 10 = complete pain relief')
pain_relief_rating.add_row('7')
pain_relief_rating.add_row('2')
pain_relief_rating.add_row('9')

relative_pain_intensity_rating = QuestionResponse(name='relative_pain_intensity_rating', 
                                             description='desc',
                                             options='0 = better, 5 = same, 10 = worse')
relative_pain_intensity_rating.add_row('5')
relative_pain_intensity_rating.add_row('4')
relative_pain_intensity_rating.add_row('10')

pain_unpleasantness = QuestionResponse(name='pain_unpleasantness', 
                                             description='desc',
                                             options='0 = pleasant, 10 = unpleasant')
pain_unpleasantness.add_row('9')
pain_unpleasantness.add_row('3')
pain_unpleasantness.add_row('7')

nrs_survey_table.nrs_pain_intensity_rating = pain_intensity_rating
nrs_survey_table.nrs_pain_relief_rating = pain_relief_rating
nrs_survey_table.nrs_relative_pain_intensity_rating = relative_pain_intensity_rating
nrs_survey_table.nrs_pain_unpleasantness = pain_unpleasantness


nwbfile.create_processing_module(name='behavior', description='survey/behavioral data')

nwbfile.processing['behavior'].add(nrs_survey_table)

with NWBHDF5IO('test_nwb.nwb', 'w') as io:
    io.write(nwbfile)

with NWBHDF5IO('test_nwb.nwb', 'r', load_namespaces=True) as io:
    nwbfile = io.read()
    print(nwbfile.processing['behavior'].data_interfaces['nrs_survey_table'].nrs_pain_intensity_rating[0])
```

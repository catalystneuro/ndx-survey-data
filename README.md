# ndx-survey-data Extension for NWB

Structure for storing the survey data in a NWB file.

![schema schema](https://github.com/Armin12/ndx-survey-data/blob/master/docs/media/survey_data.png)


## Installation
```bash
$ pip install git+https://github.com/catalystneuro/ndx-survey-data.git
```

## Usage

```python
from pynwb import NWBHDF5IO, NWBFile
from datetime import datetime
from ndx_survey_data import SurveyTable, QuestionResponse

nwbfile = NWBFile('description', 'id', datetime.now().astimezone())


pain_intensity_rating = QuestionResponse(name='pain_intensity_rating', 
                                         description='desc',
                                         options='0 = no pain, 10 = worst pain')

pain_relief_rating = QuestionResponse(name='pain_relief_rating', 
                                      description='desc',
                                      options='0 = no paint relief, 10 = complete pain relief')

relative_pain_intensity_rating = QuestionResponse(name='relative_pain_intensity_rating', 
                                                  description='desc',
                                                  options='0 = better, 5 = same, 10 = worse')

pain_unpleasantness = QuestionResponse(name='pain_unpleasantness', 
                                       description='desc',
                                       options='0 = pleasant, 10 = unpleasant')

nrs_survey_table = SurveyTable(name='nrs_survey_table',
                               description='desc', 
                               columns=[
                                   pain_intensity_rating,
                                   pain_relief_rating,
                                   relative_pain_intensity_rating,
                                   pain_unpleasantness
                               ])

nrs_survey_table.add_row(
    pain_intensity_rating=1,
    pain_relief_rating=5,
    relative_pain_intensity_rating=2,
    pain_unpleasantness=3
)

nrs_survey_table.add_row(
    pain_intensity_rating=3,
    pain_relief_rating=1,
    relative_pain_intensity_rating=6,
    pain_unpleasantness=2
)

nwbfile.create_processing_module(name='behavior', description='survey/behavioral data')

nwbfile.processing['behavior'].add(nrs_survey_table)

with NWBHDF5IO('test_nwb.nwb', 'w') as io:
    io.write(nwbfile)

with NWBHDF5IO('test_nwb.nwb', 'r', load_namespaces=True) as io:
    nwbfile = io.read()
    print(nwbfile.processing['behavior'].data_interfaces['nrs_survey_table']['pain_intensity_rating'][0])
```

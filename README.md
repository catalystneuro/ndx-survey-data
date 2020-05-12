# ndx-survey-data Extension for NWB

Structure for storing the bipolar schema of a recording in an NWB file.

![schema schema](https://github.com/Armin12/ndx-survey-data/blob/match_data/docs/media/survey_data.png?raw=true)


## Installation
```bash
$ pip install ndx-survey-data
```

## Usage

```python
from pynwb import NWBHDF5IO, NWBFile
from datetime import datetime
from ndx_survey_data import SurveyDataTable


nwbfile = NWBFile('description', 'id', datetime.now().astimezone())

survey_data_table = SurveyDataTable(name='survey_data_table',
                                          description='desc')

survey_data_table.add_row(questions='question1', responses='response1')
survey_data_table.add_row(questions='question2', responses='response2')
survey_data_table.add_row(questions='question3', responses='response3')

behavior_module = nwbfile.create_processing_module(name='behavior',
                                               description='survey/behavioral data')

nwbfile.processing['behavior'].add(survey_data_table)

with NWBHDF5IO('test_nwb.nwb', 'w') as io:
    io.write(nwbfile)

with NWBHDF5IO('test_nwb.nwb', 'r', load_namespaces=True) as io:
    nwbfile = io.read()
    print(nwbfile.processing['behavior'].data_interfaces['survey_data_table'][2]['questions'])
```

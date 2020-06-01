# ndx-survey-data Extension for NWB

Structure for storing the survey data in a NWB file.

[![codecov](https://codecov.io/gh/catalystneuro/ndx-survey-data/branch/master/graph/badge.svg)](https://codecov.io/gh/catalystneuro/ndx-survey-data)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

![schema schema](https://github.com/catalystneuro/ndx-survey-data/blob/master/docs/media/survey_data.png?raw=true)


## Installation
```bash
$ pip install git+https://github.com/catalystneuro/ndx-survey-data.git
```

## Usage

```python
from pynwb import NWBHDF5IO, NWBFile
import datetime
from ndx_survey_data.survey_definitions import nrs_survey_table


nrs_survey_table.add_row(
    pain_intensity_rating=1,
    pain_relief_rating=5,
    relative_pain_intensity_rating=2,
    pain_unpleasantness=3,
    unix_timestamp=1588217283
)

nrs_survey_table.add_row(
    pain_intensity_rating=3,
    pain_relief_rating=1,
    relative_pain_intensity_rating=6,
    pain_unpleasantness=2,
    unix_timestamp=1588217283
)

nrs_survey_table.add_row(
    pain_intensity_rating=5,
    pain_relief_rating=2,
    relative_pain_intensity_rating=0,
    pain_unpleasantness=2,
    unix_timestamp=1588217283
)

nrs_survey_table.add_row(
    pain_intensity_rating=3,
    pain_relief_rating=1,
    relative_pain_intensity_rating=6,
    pain_unpleasantness=2,
    unix_timestamp=1588217283
)
nwbfile = NWBFile('description', 'id', datetime.now().astimezone())

nwbfile.create_processing_module(name='behavior', description='survey/behavioral data')

nwbfile.processing['behavior'].add(nrs_survey_table)

with NWBHDF5IO('test_nwb.nwb', 'w') as io:
    io.write(nwbfile)

with NWBHDF5IO('test_nwb.nwb', 'r', load_namespaces=True) as io:
    nwbfile = io.read()
    print(nwbfile.processing['behavior'].data_interfaces['nrs_survey_table'].to_dataframe().to_html())
```
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pain_intensity_rating</th>
      <th>pain_relief_rating</th>
      <th>relative_pain_intensity_rating</th>
      <th>pain_unpleasantness</th>
      <th>unix_timestamp</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>5</td>
      <td>2</td>
      <td>3</td>
      <td>1588217283</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>1</td>
      <td>6</td>
      <td>2</td>
      <td>1588217283</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
      <td>1588217283</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>1</td>
      <td>6</td>
      <td>2</td>
      <td>1588217283</td>
    </tr>
  </tbody>
</table>

To add a custom survey:

```python

from ndx_survey_data import QuestionResponse, SurveyTable

q1 = QuestionResponse(name='question 1',
                      description='desc',
                      options=['option 1', 'option 2', 'option 3'])

q2 = QuestionResponse(name='question 2', 
                      description='desc',
                      options=['option 1', 'option 2', 'option 3'])

q3 = QuestionResponse(name='question 3', 
                      description='desc',
                      options=['option 1', 'option 2', 'option 3'])


custom_survey_table = SurveyTable(name='custom_survey_table',
                               description='desc', 
                               columns=[q1, q2, q3])

custom_survey_table.add_row(q1=1, q2=3, q3=0, unix_timestamp=1588217283)
custom_survey_table.add_row(q1=3, q2=1, q3=0, unix_timestamp=1588217283)
custom_survey_table.add_row(q1=2, q2=2, q3=2, unix_timestamp=1588217283)

```
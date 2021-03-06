# ndx-survey-data Extension for NWB

Structure for storing the survey data in a NWB file.

[![PyPI version](https://badge.fury.io/py/ndx-survey-data.svg)](https://badge.fury.io/py/ndx-survey-data)
[![codecov](https://codecov.io/gh/catalystneuro/ndx-survey-data/branch/master/graph/badge.svg)](https://codecov.io/gh/catalystneuro/ndx-survey-data)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

![schema schema](https://github.com/catalystneuro/ndx-survey-data/blob/master/docs/media/survey_data.png?raw=true)


## Installation
```bash
$ pip install ndx-survey-data
```

## Usage

```python
from pynwb import NWBHDF5IO, NWBFile
from datetime import datetime
from ndx_survey_data.survey_definitions import nrs_survey_table
import numpy as np


nrs_survey_table.add_row(
    pain_intensity_rating=1.1,
    pain_relief_rating=5.5,
    relative_pain_intensity_rating=np.nan,
    pain_unpleasantness=np.nan,
    unix_timestamp=1588217283
)

nrs_survey_table.add_row(
    pain_intensity_rating=np.nan,
    pain_relief_rating=1,
    relative_pain_intensity_rating=6,
    pain_unpleasantness=2.7,
    unix_timestamp=1588217283
)

nrs_survey_table.add_row(
    pain_intensity_rating=5.3,
    pain_relief_rating=np.nan,
    relative_pain_intensity_rating=0.8,
    pain_unpleasantness=2.1,
    unix_timestamp=1588217283
)

nrs_survey_table.add_row(
    pain_intensity_rating=3.7,
    pain_relief_rating=np.nan,
    relative_pain_intensity_rating=6,
    pain_unpleasantness=np.nan,
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
      <td>1.1</td>
      <td>5.5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1588217283</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>1.0</td>
      <td>6.0</td>
      <td>2.7</td>
      <td>1588217283</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5.3</td>
      <td>NaN</td>
      <td>0.8</td>
      <td>2.1</td>
      <td>1588217283</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.7</td>
      <td>NaN</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>1588217283</td>
    </tr>
  </tbody>
</table>

To add a custom survey:

```python

from ndx_survey_data import QuestionResponse, SurveyTable

q1 = QuestionResponse(name='question1',
                      description='desc',
                      options=['option 1', 'option 2', 'option 3'])

q2 = QuestionResponse(name='question2', 
                      description='desc',
                      options=['option 1', 'option 2', 'option 3'])

q3 = QuestionResponse(name='question3', 
                      description='desc',
                      options=['option 1', 'option 2', 'option 3'])


custom_survey_table = SurveyTable(name='custom_survey_table',
                               description='desc', 
                               columns=[q1, q2, q3])

custom_survey_table.add_row(question1=1.3, question2=3.9, question3=0.2, unix_timestamp=1588217283)
custom_survey_table.add_row(question1=3.3, question2=1.4, question3=0.6, unix_timestamp=1588217283)
custom_survey_table.add_row(question1=2.5, question2=2.1, question3=2.8, unix_timestamp=1588217283)

```

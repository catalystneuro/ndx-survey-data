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


# create custom survey
pain_intensity_rating = QuestionResponse(name='pain_intensity_rating', 
                                         description='desc',
                                         options=['no pain', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'worst pain'])

pain_relief_rating = QuestionResponse(name='pain_relief_rating', 
                                      description='desc',
                                      options=['no pain relief', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'complete pain relief'])

relative_pain_intensity_rating = QuestionResponse(name='relative_pain_intensity_rating', 
                                                  description='desc',
                                                  options=['better', '1', '2', '3', '4', 'same', '6', '7', '8', '9', 'worse'])

pain_unpleasantness = QuestionResponse(name='pain_unpleasantness', 
                                       description='desc',
                                       options=['pleasant', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'unpleasant'])

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

nrs_survey_table.add_row(
    pain_intensity_rating=5,
    pain_relief_rating=2,
    relative_pain_intensity_rating=0,
    pain_unpleasantness=2
)

nrs_survey_table.add_row(
    pain_intensity_rating=3,
    pain_relief_rating=1,
    relative_pain_intensity_rating=6,
    pain_unpleasantness=2
)
 # add survey to NWB file in "behavior" processing module
nwbfile = NWBFile('description', 'id', datetime.now().astimezone())
nwbfile.create_processing_module(name='behavior', description='survey/behavioral data')
nwbfile.processing['behavior'].add(nrs_survey_table)

# write NWB file
with NWBHDF5IO('test_nwb.nwb', 'w') as io:
    io.write(nwbfile)

# read NWB file and print survey
with NWBHDF5IO('test_nwb.nwb', 'r', load_namespaces=True) as io:
    nwbfile = io.read()
    print(nwbfile.processing['behavior'].data_interfaces['nrs_survey_table'].to_dataframe().to_html())
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pain_intensity_rating</th>
      <th>pain_relief_rating</th>
      <th>relative_pain_intensity_rating</th>
      <th>pain_unpleasantness</th>
    </tr>
    <tr>
      <th>id</th>
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
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>1</td>
      <td>6</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>1</td>
      <td>6</td>
      <td>2</td>
    </tr>
  </tbody>
</table>

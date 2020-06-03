from .survey_data import QuestionResponse, SurveyTable

# define NRS table
nrs_pain_intensity_rating = QuestionResponse(name='nrs_pain_intensity_rating',
                                             description='desc',
                                             options=['0 (no pain)', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                                      '10 (worst pain)',
                                                      'no answer'])

nrs_pain_relief_rating = QuestionResponse(name='nrs_pain_relief_rating',
                                          description='desc',
                                          options=['0 (no pain relief)', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                                   ' 10 (complete pain relief)', 'no answer'])

nrs_relative_pain_intensity_rating = QuestionResponse(name='nrs_relative_pain_intensity_rating',
                                                      description='desc',
                                                      options=['0 (better)', '1', '2', '3', '4', '5 (same)', '6', '7', '8', '9',
                                                               '10 (worse)', 'no answer'])

nrs_pain_unpleasantness = QuestionResponse(name='nrs_pain_unpleasantness',
                                           description='desc',
                                           options=['0 (pleasant)', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                                    '10 (unpleasant)',
                                                    'no answer'])

nrs_survey_table = SurveyTable(name='nrs_survey_table',
                               description='desc',
                               columns=[
                                   nrs_pain_intensity_rating,
                                   nrs_pain_relief_rating,
                                   nrs_relative_pain_intensity_rating,
                                   nrs_pain_unpleasantness
                               ])

# define VAS table

vas_pain_intensity_rating = QuestionResponse(name='vas_pain_intensity_rating',
                                             description='desc',
                                             options=['0 (No pain)'] + [str(i) for i in range(2, 100)] + ['100 (Worst pain possible)', 'no answer'])

vas_pain_relief_rating = QuestionResponse(name='vas_pain_relief_rating',
                                          description='desc',
                                          options=['0 (no pain relief)'] + [str(i) for i in range(2, 100)] + ['100 (complete pain relief)', 'no answer'])

vas_relative_pain_intensity_rating = QuestionResponse(name='vas_relative_pain_intensity_rating',
                                                      description='desc',
                                                      options=['0 (better)'] + [str(i) for i in range(2, 100)] + ['100 (worse)', 'no answer'])

vas_pain_unpleasantness = QuestionResponse(name='vas_pain_unpleasantness',
                                           description='desc',
                                           options=['0 (pleasant)'] + [str(i) for i in range(2, 100)] + ['100 (unpleasant)', 'no answer'])

vas_survey_table = SurveyTable(name='vas_survey_table',
                               description='desc',
                               columns=[
                                   vas_pain_intensity_rating,
                                   vas_pain_relief_rating,
                                   vas_relative_pain_intensity_rating,
                                   vas_pain_unpleasantness
                               ])

# define MPQ table

throbbing = QuestionResponse(name='throbbing',
                             description='desc',
                             options=['Mild', 'Moderate', 'Severe', 'no answer'])

shooting = QuestionResponse(name='shooting',
                            description='desc',
                            options=['Mild', 'Moderate', 'Severe', 'no answer'])

stabbing = QuestionResponse(name='stabbing',
                            description='desc',
                            options=['Mild', 'Moderate', 'Severe', 'no answer'])

sharp = QuestionResponse(name='sharp',
                         description='desc',
                         options=['Mild', 'Moderate', 'Severe', 'no answer'])

cramping = QuestionResponse(name='cramping',
                            description='desc',
                            options=['Mild', 'Moderate', 'Severe', 'no answer'])

gnawing = QuestionResponse(name='gnawing',
                           description='desc',
                           options=['Mild', 'Moderate', 'Severe', 'no answer'])

hot_burning = QuestionResponse(name='hot_burning',
                               description='desc',
                               options=['Mild', 'Moderate', 'Severe', 'no answer'])

aching = QuestionResponse(name='aching',
                          description='desc',
                          options=['Mild', 'Moderate', 'Severe', 'no answer'])

heavy = QuestionResponse(name='heavy',
                         description='desc',
                         options=['Mild', 'Moderate', 'Severe', 'no answer'])

tender = QuestionResponse(name='tender',
                          description='desc',
                          options=['Mild', 'Moderate', 'Severe', 'no answer'])

splitting = QuestionResponse(name='splitting',
                             description='desc',
                             options=['Mild', 'Moderate', 'Severe', 'no answer'])

tiring_exhausting = QuestionResponse(name='tiring_exhausting',
                                     description='desc',
                                     options=['Mild', 'Moderate', 'Severe', 'no answer'])

sickening = QuestionResponse(name='sickening',
                             description='desc',
                             options=['Mild', 'Moderate', 'Severe', 'no answer'])

fearful = QuestionResponse(name='fearful',
                           description='desc',
                           options=['Mild', 'Moderate', 'Severe', 'no answer'])

cruel_punishing = QuestionResponse(name='cruel_punishing',
                                   description='desc',
                                   options=['Mild', 'Moderate', 'Severe', 'no answer'])

mpq_survey_table = SurveyTable(name='mpq_survey_table',
                               description='desc',
                               columns=[
                                   throbbing,
                                   shooting,
                                   stabbing,
                                   sharp,
                                   cramping,
                                   gnawing,
                                   hot_burning,
                                   aching,
                                   heavy,
                                   tender,
                                   splitting,
                                   tiring_exhausting,
                                   sickening,
                                   fearful,
                                   cruel_punishing
                               ])

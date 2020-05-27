from .survey_data import QuestionResponse, SurveyTable


# define NRS table
pain_intensity_rating = QuestionResponse(name='pain_intensity_rating',
                                         description='desc',
                                         options=['no pain', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'worst pain', 'no answer'])

pain_relief_rating = QuestionResponse(name='pain_relief_rating',
                                      description='desc',
                                      options=['no pain relief', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'complete pain relief', 'no answer'])

relative_pain_intensity_rating = QuestionResponse(name='relative_pain_intensity_rating',
                                                  description='desc',
                                                  options=['better', '1', '2', '3', '4', 'same', '6', '7', '8', '9', 'worse', 'no answer'])

pain_unpleasantness = QuestionResponse(name='pain_unpleasantness',
                                       description='desc',
                                       options=['pleasant', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'unpleasant', 'no answer'])

nrs_survey_table = SurveyTable(name='nrs_survey_table',
                               description='desc',
                               columns=[
                                   pain_intensity_rating,
                                   pain_relief_rating,
                                   relative_pain_intensity_rating,
                                   pain_unpleasantness
                               ])

# define VAS table

vas_survey_table = SurveyTable(name='vas_survey_table',
                               description='desc',
                               columns=[
                                   # fill me
                               ])

# define MPQ table


mpq_survey_table = SurveyTable(name='mpq_survey_table',
                               description='desc',
                               columns=[
                                   # fill me
                               ])
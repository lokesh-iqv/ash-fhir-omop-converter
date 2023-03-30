# %%
import json
import pandas as pd
import glob

# %%
iterateItem = []
patient_data = []

# %%
# Please change the path as per files location
%cd "C:\Users\u1151468\Downloads\synthea_sample_data_fhir_r4_sep2019\fhir\"

# %%
all_files = glob.glob("*.json")

# %%
json_data = pd.DataFrame()
for count,ele in enumerate(all_files,len(all_files)):
    json_data = pd.concat([json_data, pd.read_json(ele)])

# %%
for item in json_data["entry"]:
    if item['resource']['resourceType'] == 'Patient':
        iterateItem.append(item['resource'])

# %%
df_concept = pd.read_csv('concept.csv')
df_location = pd.read_csv('fhir_omop_location.csv')
df_location = df_location.astype(str)

# %%
for item in iterateItem:
    if 'postalCode' in item['address'][0]:
        value = item['address'][0]['postalCode']
    else:
        value = 'NA'
    patient_data.append({'person_id' : item['id'],
	'gender_concept_id' : item['gender'],
    'year_of_birth' : item['birthDate'].split('-')[0],
    'month_of_birth' : item['birthDate'].split('-')[1],
    'day_of_birth' : item['birthDate'].split('-')[2],
    'city' : item['address'][0]['city'],
    'state' : item['address'][0]['state'],
    'postalCode' : value,
    'country' : item['address'][0]['country'],
    'race_source_value' : item['extension'][0]['extension'][0]['valueCoding']['display'],
    'race_source_concept_id' : item['extension'][0]['extension'][0]['valueCoding']['code'],
    'ethnicity_source_value' : item['extension'][1]['extension'][0]['valueCoding']['display'],
    'ethnicity_source_concept_id' : item['extension'][1]['extension'][0]['valueCoding']['code']
    })


# %%
df = pd.DataFrame(patient_data)

# %%
df = pd.merge(df, df_location, how='left', left_on=['city','state','postalCode','country'], right_on=['city','state','zip','county'])

# %%
df = df[['person_id', 'gender_concept_id','year_of_birth','month_of_birth','day_of_birth','location_id','race_source_value','race_source_concept_id','ethnicity_source_value','ethnicity_source_concept_id']]

# %%
df



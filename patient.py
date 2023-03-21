# %%
import json
import pandas as pd

# %%
iterateItem = []
patient_data = []

# %%
# Please change the path as per files location
%cd "C:\Users\u1151468\Downloads\synthea_sample_data_fhir_r4_sep2019\fhir\"

# %%
json_data = pd.read_json("Aaron697_Brekke496_2fa15bc7-8866-461a-9000-f739e425860a.json")
df_concept = pd.read_csv('concept.csv')
df_location = pd.read_csv('location.csv')
df_location = df_location.astype(str)

# %%
for item in iterateItem:
    print(item)

# %%
for item in json_data["entry"]:
    if item['resource']['resourceType'] == 'Patient':
        iterateItem.append(item['resource'])

# %%

for item in iterateItem:
    patient_data.append({'person_id' : item['id'],
	'gender_concept_id' : item['gender'],
    'year_of_birth' : item['birthDate'].split('-')[0],
    'month_of_birth' : item['birthDate'].split('-')[1],
    'day_of_birth' : item['birthDate'].split('-')[2],
    'city' : item['address'][0]['city'],
    'state' : item['address'][0]['state'],
    'postalCode' : item['address'][0]['postalCode'],
    'country' : item['address'][0]['country'],
    'race_source_value' : item['extension'][0]['extension'][0]['valueCoding']['display'],
    'race_source_concept_id' : item['extension'][0]['extension'][0]['valueCoding']['code'],
    'ethnicity_source_value' : item['extension'][1]['extension'][0]['valueCoding']['display'],
    'ethnicity_source_concept_id' : item['extension'][1]['extension'][0]['valueCoding']['code']
    })

df = pd.DataFrame(patient_data)



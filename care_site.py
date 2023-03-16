# %%
import json
import pandas as pd

# %%
iterateItem = []
care_site_data = []

# %%
# Please change the path as per files location
%cd "C:\Users\u1151468\Downloads\synthea_sample_data_fhir_r4_sep2019\fhir\"

# %%
json_data = pd.read_json("Aaron697_Brekke496_2fa15bc7-8866-461a-9000-f739e425860a.json")
df_concept = pd.read_csv('concept.csv')
df_location = pd.read_csv('location.csv')
df_location = df_location.astype(str)

# %%
for item in json_data["entry"]:
    if item['resource']['resourceType'] == 'Organization':
        iterateItem.append(item['resource'])

# %%

for item in iterateItem:
    care_site_data.append({'care_site_id' : item['id'],
	'care_site_name' : item['name'],
    'place_of_service_concept_type' : item['type'][0]['coding'][0]['code'],
    'city' : item['address'][0]['city'],
    'state' : item['address'][0]['state'],
    'postalCode' : item['address'][0]['postalCode'],
    'country' : item['address'][0]['country']})

df = pd.DataFrame(care_site_data)

# %%
df = pd.merge(df, df_concept[['concept_code', 'concept_id']], how='left', left_on=['place_of_service_concept_type'], right_on=['concept_code'])
df['place_of_service_concept_id'] = df['concept_id']

# %%
df = pd.merge(df, df_location, how='left', left_on=['city','state','postalCode','country'], right_on=['city','state','zip','county'])
df['place_of_service_concept_id'] = df['concept_id']

# %%
df = df[['care_site_id', 'care_site_name','place_of_service_concept_id','location_id']]

# %%
df



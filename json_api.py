import requests
import time
import json
import pandas as pd
url ="https://formulae.brew.sh/api/formula.json"
data= requests.get(url)
# convert the response to json format
data=data.json()
list1=[]
for package in data:
	df={}
	package_name = package['name']
	package_url =f'https://formulae.brew.sh/api/formula/{package_name}.json'
	package_data=requests.get(package_url)
	pkg=package_data.json()
	json_data=json.dumps(pkg,indent=2)
	df['package_name']=package_name
	df['install_30']=pkg['analytics']['install']['30d'][package_name]
	df['install_90']=pkg['analytics']['install']['90d'][package_name]
	df['install_365']=pkg['analytics']['install']['365d'][package_name]
	df['description'] =pkg['desc']
	list1.append(df)
	print(f'Fineshed {package_name} in {package_data.elapsed.total_seconds()} seconds')
# Create a dataframe from the list data
frame=pd.DataFrame(list1)
# Save to excel on the local computer
frame.to_excel("C:\\Users\\marti\\Desktop\\Data_analysis_thesis\\Code\\homebrew_libraries_data.excel")
#InnovationChallenge Project
import requests
import json
import time

while(1):
    with open('input.txt', 'r') as file:
        data = file.read().split('/', 13)
        #List of the Symptoms is always - data[12]
        print(data)
    if(len(data)>2):
        Symptoms = ((data[12].replace(" ,", ",")).replace(", ", ",")).replace(' ', '_')
        URL = "http://localhost:5000/?symptoms="+Symptoms
        response = requests.get(URL)
    print(URL)

    if response.status_code == 200:
        Output = json.loads(response.text)
        print(Output.get('data'))
        outFile = open("Output.txt", "w")
        stringOutput = Output.get('data')
        text = "First Name: " + data[0] + "\n" + "Last Name: " + data[1] + "\n" + "AGE: " + data[2] + "\n" + "Predicted prognosis: " + stringOutput
        write = outFile.write(text)
        outFile.close()
    elif response.status_code == 500:
        print("Unsuffice Data Provided")
    else:
        print("Error. Check Server")
	
    time.sleep(2)

## Imports
import sys
import os
import json
sys.path.insert(1, 'src')  # update import path for my custom stuff

import generateJSON

if __name__ == '__main__':

    # # make sure user is inputting number of training epochs
    # try:
    #     num_epochs = int(sys.argv[1])
    # except:
    #     print('\n\n\nEnter number of training epochs\n\n\n')
    #     raise UserWarning


    # Generate JSON data - edit the src/generateJSON.py for different data
    generateJSON.GenerateRFP()
    generateJSON.GenerateTruth()

    # Load JSON data
    json_data = {}
    for cnt, file in enumerate(os.listdir('data')):
        if file != 'truth.json':
            with open('data/'+file) as json_file:
                json_data[cnt] = json.load(json_file)

    epoch = 0
    num_epochs = 2
    while(epoch < num_epochs):
        epoch += 1

        # user select RFP to fill out
        print('\n Available RFPs to fill out')
        for key in json_data.keys():
            json = json_data[key]
            print(f'{key}) ',json['client'])
        RFP_select = input('Select RFP by selecting number: ')

        # loop through RFP requirements
        print('\n\n')
        selected_JSON = json_data[int(RFP_select)]
        service_type = selected_JSON['content']['Type']
        for request in selected_JSON['content']['Requests']:
            print(f'Select response to RFP item {service_type} {request}')







## Classes
class Document():
    def __init__(self, title):
        self.docID = title



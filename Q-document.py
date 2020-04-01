## Imports
import sys
import os
import json
sys.path.insert(1, 'src')  # update import path for my custom stuff

import generateJSON
import Qbrain

if __name__ == '__main__':

    # TODO: uncomment this unless you're debugging
    # # make sure user is inputting number of training epochs
    # try:
    #     num_epochs = int(sys.argv[1])
    # except:
    #     print('\n\n\nEnter number of training epochs\n\n\n')
    #     raise UserWarning


    # Generate JSON data - edit the src/generateJSON.py for different data
    generateJSON.GenerateRFP()
    responses = generateJSON.GenerateResponses()

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

            for key in responses.keys():
                print(f'{key})', responses[key])

            response_select = input('Select response by selecting number: ')
            print('\n\n')

            #TODO:
            # 1) write a class that handles the Q table
            # 2) have some sort of thing that culls Q(s,a) positions if they fall below a certain reward threshold
            #   a) rewards should be like +1 if selected, -0.5 for all others not selected. Use threshold reward as tuning knob


## Imports
import sys
import os
import json
sys.path.insert(1, 'src')  # update import path for my custom stuff

import generateJSON
import Qbrain

if __name__ == '__main__':

    # make sure user is inputting number of training epochs
    try:
        num_epochs = int(sys.argv[1])
    except:
        print('\n\n\nEnter number of training epochs\n\n\n')
        raise UserWarning


    # Generate JSON data - edit the src/generateJSON.py for different data
    generateJSON.GenerateRFP()

    # Load JSON data
    json_data = {}
    for cnt, file in enumerate(os.listdir('data')):
        if file != 'truth.json':
            with open('data/'+file) as json_file:
                json_data[cnt] = json.load(json_file)


    # instantiate organization specific object to handle Q matrix
    OrgQBrain = Qbrain.Qtable(json_data, generateJSON.GenerateResponses())

    # train model using user input as reward function
    epoch = 0
    while(epoch < num_epochs):
        epoch += 1

        # user select RFP to fill out
        print('\n Available RFPs to fill out')
        for key in json_data.keys():
            json = json_data[key]
            print(f'{key}) ',json['client'])
        RFP_select = input('Select RFP by selecting number: ')
        print('\n\n')

        # loop through RFP requirements
        selected_JSON = json_data[int(RFP_select)]
        service_type = selected_JSON['content']['Type']
        for request in selected_JSON['content']['Requests']:
            print(f'Select response to RFP item {service_type} {request}')

            # generate acceptable responses from trained Q matrix
            state = [service_type, request]
            responses = OrgQBrain.ReturnResponses(state)
            for response in responses:
                print(f'{response[0]})', response[1])

            # update Q matrix based on user input
            response_select = input('Select response by selecting number: ')
            OrgQBrain.UpdateResponses(state, int(response_select))
            print('\n\n')




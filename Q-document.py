## Imports
import sys
import os
import json

sys.path.insert(1, 'src')  # update import path for my custom stuff

import generateJSON
import Qbrain

def ClearScreen():
    # clear terminal screen, inspired by https://stackoverflow.com/a/2084628
    os.system('cls' if os.name == 'nt' else 'clear')

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


    # provide user instructions
    ClearScreen()
    print('Q-document is an interactive simulation for filling out Request for Proposals (RFP).\n'
          'You are a user at a company filling out RFP\'s for prospective clients.\n\n'
          
          'Each client needs a different service (RFP Type).\n'
          'Each RFP Type has different field you need to fill out (Request Type).\n'
          'As you fill out the RFP fields, Q-document will recommend responses for you to choose.\n\n'
          
          '---------------------------------------------------------------------------------------------\n'
          'Fill out the same client RFP a few times with similar responses to see how Q-document learns.\n'
          '---------------------------------------------------------------------------------------------\n\n'
          
          'As you do this, Q-document will associate your responses with RFP Type/Request Type and give you better recommendations.\n'
          'See the "Guided Example" in the README for a walkthrough with commentary.\n\n')


    RFP_select = input('Press Any Key to Continue...')
    ClearScreen()

    # train model using user input as reward function
    epoch = 0
    while(epoch < num_epochs):
        epoch += 1

        # user select RFP to fill out
        print('Available Client RFPs to fill out\n')
        for key in json_data.keys():
            json = json_data[key]
            print(f'{key}) ',json['client'])
        RFP_select = input('\nSelect RFP by selecting number: ')
        ClearScreen()

        # loop through RFP requirements
        selected_JSON = json_data[int(RFP_select)]
        service_type = selected_JSON['content']['Type']
        selected_client = selected_JSON['client']
        for request in selected_JSON['content']['Requests']:
            print(f'{selected_client}\n\n'
                  f'RFP Type: {service_type}\n'
                  f'RFP Field (Request Type): {request}\n')

            # generate acceptable responses from trained Q matrix
            state = [service_type, request]
            responses = OrgQBrain.ReturnResponses(state)

            print('Q-document response recommendations:')
            for response in responses:
                print(f'{response[0]})', response[1])

            # update Q matrix based on user input
            response_select = input('\nSelect response by selecting number: ')
            OrgQBrain.UpdateResponses(state, int(response_select))
            ClearScreen()




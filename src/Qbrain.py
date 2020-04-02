## Imports
import numpy as np


class Qtable():
    def __init__(self, json_data, responses):
        '''
        generate Q-matrix formulated with:
          State Space: RFP type, request type
          Action Space: list of all possible responses
        :param json_data: dictionary of processed RFPs
        :param responses: dictionary of possible responses
        '''

        # Create associative dictionary between RFP type, request type, and response
        self.assocRFPDict = {}
        self.assocRequestDict = {}
        self.assocResponseDict = {}

        # create dictionary for RFP
        for RFP in json_data:

            # verify if dictionary contains element
            if json_data[RFP]['content']['Type'] not in self.assocRFPDict.values():

                # check if dictionary is empty, if not increment key up by one
                if len(self.assocRFPDict.keys()) == 0:
                    self.assocRFPDict[0] = json_data[RFP]['content']['Type']
                else:
                    self.assocRFPDict[max(self.assocRFPDict.keys())+1] = json_data[RFP]['content']['Type']

            # create dictionary for Requests
            for request in json_data[RFP]['content']['Requests']:
                if request not in self.assocRequestDict.values():
                    if len(self.assocRequestDict.keys()) == 0:
                        self.assocRequestDict[0] = request
                    else:
                        self.assocRequestDict[max(self.assocRequestDict.keys())+1] = request

        # create dictionary for responses
        for key in responses.keys():
            if len(self.assocResponseDict.keys()) == 0:
                self.assocResponseDict[0] = responses[key]
            else:
                self.assocResponseDict[max(self.assocResponseDict.keys())+1] = responses[key]

        # create numpy array
        self.qmatrix = np.zeros((len(self.assocResponseDict.keys()),
                                len(self.assocRFPDict.keys()),
                                len(self.assocRequestDict.keys())))


    def ReturnResponses(self, state):
        '''
        accepts state and returns responses within some range of max value
        :param state: list (RFP Type, Request Type) --> future versions will be extensible to n-dimensional state spaces
        :return: list of acceptable responses and response IDs
        '''
        percent_threshold = 0.4  # percent of max

        j, i = self.GetState(state)

        # return indices of responses that are within threshold percentage of response with max expected reward
        responseList = self.qmatrix[:, j, i]
        responseThreshold = np.where(responseList >= percent_threshold*np.max(responseList))[0]

        return [(k,v[0]) for k,v in self.assocResponseDict.items() if k in responseThreshold]

    def UpdateResponses(self, state, selectID):
        '''
        updates Q(s, a) based on reward (user selection)
        :param state: list (RFP Type, Request Type) --> future versions will be extensible to n-dimensional state spaces
        :param selectID: user selected response ID
        :return: None
        '''

        j, i = self.GetState(state)
        # add reward to selected action and associated actions, subtract reward from not selected actions
        # generate scale factor based on number of values with positive reward


        selectReward = 2*np.max(self.qmatrix[:,j,i])+1 # this is fudged a bit for proof of concept, future version obviously need to refine this
        groupReward = 0.5
        nonselectPenalty = -0.1

        # loop through actions for given Q(s, :)
        duck = self.qmatrix[:, j, i]
        for k in np.arange(0, self.qmatrix[:, j, i].shape[0]):
            # add reward to selected action
            if k == selectID:
                self.qmatrix[k, j, i] += selectReward

            # add reward to associated actions
            elif self.assocResponseDict[selectID][1] == self.assocResponseDict[k][1]:
                self.qmatrix[k, j, i] += groupReward

            # subtract reward from non-selected, non-associated actions
            else:
                self.qmatrix[k, j, i] += nonselectPenalty


    def GetState(self, state):
        '''
        helper function to translate RFP type and Request type to j, i coords for q-matrix
        :param state: tuple (RFP Type, Request Type) --> future versions will be extensible to n-dimensional state spaces
        :return: j,i coordinates within Q-matrix
        '''

        # compute coords in Q matrix [j, i]
        # match value, return key per https://stackoverflow.com/questions/16588328/return-key-by-value-in-dictionary
        j = next(k for k, v in self.assocRFPDict.items() if v == state[0])
        i = next(k for k, v in self.assocRequestDict.items() if v == state[1])

        return j, i


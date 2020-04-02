## imports
import json


def GenerateRFP():
    '''
    Quick utility function to generate the RFP JSON files in the root folder.
    :return: writes RFP JSON files to root folder
    '''

    # create dummy data
    doc1 = {'client': 'Product RFP: Super Best Friends Inc',
            'content':{'Type': 'Product',
            'Requests':
                ['Service',
                 'Description',
                 'Price']
                        }
            }
    doc2 = {'client': 'Engineering RFP: Mr Hankey\'s Christmas Emporium',
            'content':{'Type': 'Engineering',
            'Requests':
                ['Service',
                 'Description',
                 'Price']
                        }
            }
    doc3 = {'client': 'Sales RFP: Shakey\'s Pizza',
            'content':{'Type': 'Sales',
            'Requests':
                ['Service',
                 'Description',
                 'Price']
                        }
            }

    # generate json documents and write to file
    docs = [doc1, doc2, doc3]

    for cnt, doc in enumerate(docs):
        with open(f'data/RFP{cnt+1}.json', 'w') as outfile:
            json.dump(doc, outfile)

def GenerateResponses():

    # generate dummy responses based on model trained by previous client RFPs
    responses = {1: ['Our provided SERVICE is ENGINEERING','engineering'],
                 2: ['Our DESCRIPTION of service is that we are good ENGINEERS','engineering'],
                 3: ['The PRICE of our ENGINEERING services is an arm','engineering'],
                 4: ['Our provided SERVICE is SALES','sales'],
                 5: ['Our DESCRIPTION of service is that we have SOLD XYZ','sales'],
                 6: ['The PRICE of SELLING your stuff will cost you a leg','sales'],
                 7: ['Our provided SERVICE is to develop this PRODUCT for you','sales'],
                 8: ['Our DESCRIPTION of service is that we have developed PRODUCT XYZ','product'],
                 9: ['The PRICE of PRODUCT development costs your first born','product']}

    return responses





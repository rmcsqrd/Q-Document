## imports
import json

def GenerateRFP():
    '''
    Quick utility function to generate the RFP JSON files in the root folder.
    :return: writes RFP JSON files to root folder
    '''

    # create dummy data
    doc1 = {'client': 'Super Best Friends Inc',
            'content':{'Type': 'Product',
            'Requests':
                ['Service',
                 'Description',
                 'Price']
                        }
            }
    doc2 = {'client': 'Mr Hankey\'s Christmas Emporium',
            'content':{'Type': 'Engineering',
            'Requests':
                ['Service',
                 'Description',
                 'Price']
                        }
            }
    doc3 = {'client': 'Shakey\'s Pizza',
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
    responses = {1: ['Let us engineer stuff for you','engineering'],
                 2: ['we have engineered XYZ','engineering'],
                 3: ['engineering services cost an arm','engineering'],
                 4: ['let us sell stuff for you','sales'],
                 5: ['we have sold XYZ','sales'],
                 6: ['selling your stuff will cost you a leg','sales'],
                 7: ['let us develop this product for you','sales'],
                 8: ['we have developed product XYZ','product'],
                 9: ['product development costs your first born','product']}

    return responses





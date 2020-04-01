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

def GenerateTruth():
    truth = {'Product':[{'Service': 'We are good at making stuff',
                         'Description': 'We will make you stuff',
                         'Price': 100}],

            'Engineering':[{'Service': 'We are engineers',
                             'Description': 'We will engineer your stuff',
                             'Price': 1000}],

            'Sales':[{'Service': 'We are great at selling stuff',
                      'Description': 'We will sell your stuff',
                      'Price': 4000}]
             }

    with open('data/truth.json', 'w') as outfile:
        json.dump(truth, outfile)


## imports
import json
import sys

def GenerateJSON():
    '''
    Quick utility function to generate the JSON files in the root folder.
    :return: writes JSON files to root folder
    '''

    # create dummy data
    doc1 = {'client': 'Super Best Friends Inc',
            'content':[{'Request Type': 'Product Request',
            'Requests':
                ['Product Type',
                 'References',
                 'Price']
                        }]
            }
    doc2 = {'client': 'Mr Hankey\'s Christmas Emporium',
            'content':[{'Request Type': 'Engineering Request',
            'Requests':
                ['Services Type',
                 'References',
                 'Price']
                        }]
            }
    doc3 = {'client': 'Shakey\'s Pizza',
            'content':[{'Request Type': 'Sales Request',
            'Requests':
                ['Services Type',
                 'References',
                 'Price']
                        }]
            }

    # generate json documents and write to file
    docs = [doc1, doc2, doc3]
    docName = ['doc1', 'doc2', 'doc3']

    for cnt, doc in enumerate(docs):
        with open(f'../data/{docName[cnt]}data.json', 'w') as outfile:
            json.dump(doc, outfile)

# uncomment and run if you want to generate new data
# GenerateJSON()



# Q-Document
Q-document is a proof of concept implementation of Q-learning within a mock request for proposal (RFP) task. As users
fill out an RFP, Q-document categorizes and tracks user input to provide better response recommendations.

[Setup/Usage](#Setup)  
[Theory](#Theory)  
[Future Expansion](#Future)  
[Guided Example](#Example)


## Setup/Usage<a name="Setup"></a>
#### Dependencies
Python version = 3.7.7  
See specific package requirements in `requirements.txt`  

#### Usage
1. Clone the repository  
    
        $ git clone https://github.com/rmcsqrd/Q-Document.git
      
    
2. Run the program for some number of training simulations  
    
        $ python3 /path/to/cloned/repository/Q-document.py [number of training simulations]
    
      
3. Provide user input as prompted.

#### What is going on?<a name="TLDR"></a> 
Q-document is a mock simulation of a user filling out RFP's. There are several different types of RFP's to choose from (engineering, sales, etc) and Q-document suggests 
possible responses for each portion of the RFP.
Unless imparted with expert knowledge, Q-document begins in a totally naive state with regards to what is an appropriate 
response to an appropriate RFP section. Over time, as the user fills out more RFP's, Q-document learns what an 
appropriate response is and narrows down its recommendations.

#### Modifying the Simulation Data  
Simulation data can be modified in the `src/generateJSON.py` file by modifying the dummy data dictionaries.  
Reward function/response threshold can be modified in `src/Qbrain.py`  


## Theory<a name="Theory"></a>
Q-document is a modified implementation of the reinforcement learning technique called Q-learning. Q-learning is a technique
wherein an agent runs multiple simulations through some sort of process to determine an optimal policy. A typical simulation
involves
 1. observing a state
 2. determining the action with the maximum reward at that state from previous observations
 3. taking that action
 4. observing the reward from the selected action at that state
 5. backpropogating the expected reward
 
Q-document is a modification of this because there is no backpropogation - action at a current state doesn't impact future
states (at least in this current iteration, this is definitely something to explore in the future). Additionally, Q-document
treats the user as the reward function. When the user selects a suggestion, Q-document updates the state/action pair based on 
that selected action (and associated actions). 

At the core of Q-learning is a matrix `Q(s,a)` which is an n-dimensional matrix that stores all possible state/action pairings.
The typical Q-learning algorithm is (from Reinforcement Learning, 2nd ed, Sutton and Barto):

![alt text](https://github.com/rmcsqrd/Q-Document/tree/master/aux/qlearn.png "Q Learn Algorithm")





## Future Expansions<a name="Future"></a>
The modified Future expansions that I'd like to explore are:

 * __Response Dictionary__: I think it would be prudent to use some sort of neural network to generate and characterize
 the response dictionary based on previous RFP's.
 * __Reward Function__: I would like to explore using some sort of neural network to update the reward function.
 * __Expert Knowledge__: In order to ensure user confidence in Q-document, it is important that patently wrong suggestions
 are not provided. Imparting expert knowledge to parse out any bad recommendations prior to user deployment can aid in this.
 * __Natural Language Processing__: Q-document relies heavily on a discretized state/action space which in turn relies on 
 discretized data. Natural language processing is one option for generating the response/RFP inputs. 
 


## Guided Example<a name="Example"></a>
Start the simulation and run for 3 simulations

    
    $ python3 Q-document.py 3
    
    
Follow the prompt and fill out the RFP for Shakey's Pizza
  
    
         Available RFPs to fill out
    0)  Super Best Friends Inc
    1)  Shakey's Pizza
    2)  Mr Hankey's Christmas Emporium
    Select RFP by selecting number: 1
      

RFP type is "Sales" and the request type is "Services". We select option 3 accordingly.

There are currently lots of response recommendations because we have not initialized Q-document with any 
expert knowledge. Without expert knowledge, it trains based purely to user input.  
 
    
        Select response to RFP item 
    RFP Type: Sales
    Request Type: Service
    0) Let us engineer stuff for you
    1) we have engineered XYZ
    2) engineering services cost an arm
    3) let us sell stuff for you
    4) we have sold XYZ
    5) selling your stuff will cost you a leg
    6) let us develop this product for you
    7) we have developed product XYZ
    8) product development costs an arm and a leg
    Select response by selecting number: 3
    
    
The RFP wants a description of sales services so we select option 4
    
    
    Select response to RFP item 
    RFP Type: Sales
    Request Type: Description
    0) Let us engineer stuff for you
    1) we have engineered XYZ
    2) engineering services cost an arm
    3) let us sell stuff for you
    4) we have sold XYZ
    5) selling your stuff will cost you a leg
    6) let us develop this product for you
    7) we have developed product XYZ
    8) product development costs an arm and a leg
    Select response by selecting number: 4
    
    
Finally, the RFP wants a price so we select option 5

    
    Select response to RFP item 
    RFP Type: Sales
    Request Type: Price
    0) Let us engineer stuff for you
    1) we have engineered XYZ
    2) engineering services cost an arm
    3) let us sell stuff for you
    4) we have sold XYZ
    5) selling your stuff will cost you a leg
    6) let us develop this product for you
    7) we have developed product XYZ
    8) product development costs an arm and a leg
    Select response by selecting number: 5
    
    
At this point we begin another training epoch. We want to keep training within the sales state
space so again we decide to request to build another Shakey's Pizza.

    
     Available RFPs to fill out
    0)  Super Best Friends Inc
    1)  Shakey's Pizza
    2)  Mr Hankey's Christmas Emporium
    Select RFP by selecting number: 1
    
    
This time we note that Q-document has learned from our previous inputs. We again select option 3 and note:  

1. Last time around, the user selected option 3 so this is the current best recommendation.
2. Options 4 and 5 are related to sales RFP's (this comes from the response data set) and thus are potentially
acceptable recommendations as well. 


    
    Select response to RFP item 
    RFP Type: Sales
    Request Type: Service
    3) let us sell stuff for you
    4) we have sold XYZ
    5) selling your stuff will cost you a leg
    Select response by selecting number: 3
    

We notice similar phenomena for the description and price portions of the RFP. We input similar responses to last time.
    
    
    Select response to RFP item 
    RFP Type: Sales
    Request Type: Description
    3) let us sell stuff for you
    4) we have sold XYZ
    5) selling your stuff will cost you a leg
    Select response by selecting number: 4
    
    
    
    Select response to RFP item 
    RFP Type: Sales
    Request Type: Price
    3) let us sell stuff for you
    4) we have sold XYZ
    5) selling your stuff will cost you a leg
    Select response by selecting number: 5
    
    
For our third and final training epoch, we note that Q-document has been trained enough that it knows a single, correct
response for each RFP type/request pair:
    
    
     Available RFPs to fill out
    0)  Super Best Friends Inc
    1)  Shakey's Pizza
    2)  Mr Hankey's Christmas Emporium
    Select RFP by selecting number: 1
    
    
    Select response to RFP item 
    RFP Type: Sales
    Request Type: Service
    3) let us sell stuff for you
    Select response by selecting number: 3
    
    
    Select response to RFP item 
    RFP Type: Sales
    Request Type: Description
    4) we have sold XYZ
    Select response by selecting number: 4
    
    
    Select response to RFP item 
    RFP Type: Sales
    Request Type: Price
    5) selling your stuff will cost you a leg
    Select response by selecting number: 5

If we were to run a fourth training epoch but instead chose a different RFP, we would notice that
all responses are suggested. This is because Q-document has not received enough user input to threshold
out response suggestions for that portion of the state space. 



    



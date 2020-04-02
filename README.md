#### TL;DR

Q-document is an interactive simulation for filling out Request for Proposals (RFP).  
You are a user at a company filling out RFP\'s for prospective clients.  

Each client needs a different service (RFP Type).  
Each RFP Type has different field you need to fill out (Request Type).  
As you fill out the RFP fields, Q-document will recommend responses for you to choose.  

As you do this, Q-document will associate your responses with RFP Type/Request Type and give you better recommendations.  
See the "Guided Example" in the README for a walkthrough with commentary.


___
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
        
2. Install Dependencies  

        $ sudo pip3 install -r requirements.txt
      
2. Run the program for some number of training simulations  
    
        $ python3 /path/to/cloned/repository/Q-document.py [number of training simulations]
    


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

![alt text](https://github.com/rmcsqrd/Q-Document/raw/master/aux/qlearn.png "Q Learn Algorithm")

For this implementation of Q-document, I basically reduced the `Q(s,a)` update step down to just looking for the recommendation
with the maximum recorded reward. I did not feel that it was prudent to include a lookahead/discount factor given
that the state transitions are in a vacuum - eg the action space for the 'service' request category does
not necessarily impact the action space/reward for the 'price' category in this prototype formulation.

As such, I formulated the underlying MDP as 
* __State Space__: (RFP type, request type)
* __Action Space__: ([all possible recommendations sans expert knowledge])
* __Transition Dynamics__: Deterministic/arbitrary (we assume that the order of filling out the RFP is not important)
* __Gamma__: Arbitrary (this proof of concept assumes actions for some state don't impact the actions of another)
* __Reward__: User selection = large reward, related selections = small reward, unrelated/not selected = negative reward.

The `Q(s,a)` matrix can be visualized as:
![alt text](https://github.com/rmcsqrd/Q-Document/raw/master/aux/Qmat.png "Q Matrix")

The big feature for Q-document is that is uses the user input as the reward function. When a user enters a new portion of
the RFP filling task, Q-document makes a bunch of recommendations from the `Q(s,a)`. When the user selects one of its actions
(or doesn't) it updates the expected reward at that `Q(s,a)` pair that will inform future recommendation decisions. 

The main limitation with using a Q-learning approach is its heavy reliance on a uniform and discretized state space. This is inherently tricky with document parsing tasks.
The JSON file structure that Q-document uses for generating its `Q(s,a)` matrix are highly standardized, whereas most communication
between a client and a customer are not. Future explorations to resolve this issue are discussed in the "Future Expansions" section


## Future Expansions<a name="Future"></a>
The modified Future expansions that I'd like to explore are:

 * __Cross State Implications__: I think it would be worth exploring what happens if a user takes an action in one state and
 how that might impact that same action choice in another state. For example, if a user chooses a certain
 overall price in one RFP request category, an optimal policy would know to use a smaller price for a sub-category. This relies
 heavily on the discretization of the state space and lots of training data. 
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
    
    
Follow the prompt and fill out the RFP for Mr Hankey's Christmas Emporium
  
    
    Available RFPs to fill out
    
    0)  Super Best Friends Inc
    1)  Shakey's Pizza
    2)  Mr Hankey's Christmas Emporium
    
    Select RFP by selecting number: 2
      

RFP type is "Engineering" and the request type is "Services". We select option 3 accordingly.

There are currently lots of response recommendations because we have not initialized Q-document with any 
expert knowledge. Without expert knowledge, it trains based purely to user input.  
 
    
        Engineering RFP: Mr Hankey's Christmas Emporium
        
        RFP Type: Engineering
        RFP Field (Request Type): Service
        
        Q-document response recommendations:
        0) Our provided SERVICE is ENGINEERING
        1) Our DESCRIPTION of service is that we are good ENGINEERS
        2) The PRICE of our ENGINEERING services is an arm
        3) Our provided SERVICE is SALES
        4) Our DESCRIPTION of service is that we have SOLD XYZ
        5) The PRICE of SELLING your stuff will cost you a leg
        6) Our provided SERVICE is to develop this PRODUCT for you
        7) Our DESCRIPTION of service is that we have developed PRODUCT XYZ
        8) The PRICE of PRODUCT development costs your first born
        
        Select response by selecting number: 0
    
    
The RFP wants a description of engineering services so we select option 1
    
        Engineering RFP: Mr Hankey's Christmas Emporium
        
        RFP Type: Engineering
        RFP Field (Request Type): Description
        
        Q-document response recommendations:
        0) Our provided SERVICE is ENGINEERING
        1) Our DESCRIPTION of service is that we are good ENGINEERS
        2) The PRICE of our ENGINEERING services is an arm
        3) Our provided SERVICE is SALES
        4) Our DESCRIPTION of service is that we have SOLD XYZ
        5) The PRICE of SELLING your stuff will cost you a leg
        6) Our provided SERVICE is to develop this PRODUCT for you
        7) Our DESCRIPTION of service is that we have developed PRODUCT XYZ
        8) The PRICE of PRODUCT development costs your first born
        
        Select response by selecting number: 1
    
    
Finally, the RFP wants a price so we select option 2

        Engineering RFP: Mr Hankey's Christmas Emporium
        
        RFP Type: Engineering
        RFP Field (Request Type): Price
        
        Q-document response recommendations:
        0) Our provided SERVICE is ENGINEERING
        1) Our DESCRIPTION of service is that we are good ENGINEERS
        2) The PRICE of our ENGINEERING services is an arm
        3) Our provided SERVICE is SALES
        4) Our DESCRIPTION of service is that we have SOLD XYZ
        5) The PRICE of SELLING your stuff will cost you a leg
        6) Our provided SERVICE is to develop this PRODUCT for you
        7) Our DESCRIPTION of service is that we have developed PRODUCT XYZ
        8) The PRICE of PRODUCT development costs your first born
        
        Select response by selecting number: 2

At this point we begin another training epoch. We want to keep training within the sales state
space so again we decide to fill out another RFP for Mr. Hankey.

        Available RFPs to fill out
        
        0)  Super Best Friends Inc
        1)  Shakey's Pizza
        2)  Mr Hankey's Christmas Emporium
        
        Select RFP by selecting number: 2
    
This time we note that Q-document has learned from our previous inputs. We again select option 0 and note:  

1. Last time around, the user selected option 0 so this is the current best recommendation.
2. Options 1 and 2 are related to sales RFP's (this comes from the response data set) and thus are potentially
acceptable recommendations as well. 


        Engineering RFP: Mr Hankey's Christmas Emporium
        
        RFP Type: Engineering
        RFP Field (Request Type): Service
        
        Q-document response recommendations:
        0) Our provided SERVICE is ENGINEERING
        1) Our DESCRIPTION of service is that we are good ENGINEERS
        2) The PRICE of our ENGINEERING services is an arm
        
        Select response by selecting number: 0

We notice similar phenomena for the description and price portions of the RFP. We input similar responses to last time.
    
        Engineering RFP: Mr Hankey's Christmas Emporium
        
        RFP Type: Engineering
        RFP Field (Request Type): Description
        
        Q-document response recommendations:
        0) Our provided SERVICE is ENGINEERING
        1) Our DESCRIPTION of service is that we are good ENGINEERS
        2) The PRICE of our ENGINEERING services is an arm
        
        Select response by selecting number: 1
        
        _____
        
        Engineering RFP: Mr Hankey's Christmas Emporium

        RFP Type: Engineering
        RFP Field (Request Type): Price
        
        Q-document response recommendations:
        0) Our provided SERVICE is ENGINEERING
        1) Our DESCRIPTION of service is that we are good ENGINEERS
        2) The PRICE of our ENGINEERING services is an arm
        
        Select response by selecting number: 2
    
    
For our third and final training epoch, we note that Q-document has been trained enough that it knows a single, correct
response for each RFP type/request pair:
    
    
        Available Client RFPs to fill out
        
        0)  Product RFP: Super Best Friends Inc
        1)  Sales RFP: Shakey's Pizza
        2)  Engineering RFP: Mr Hankey's Christmas Emporium
        
        Select RFP by selecting number: 2
        
        _____
        
        Engineering RFP: Mr Hankey's Christmas Emporium

        RFP Type: Engineering
        RFP Field (Request Type): Service
        
        Q-document response recommendations:
        0) Our provided SERVICE is ENGINEERING
        
        Select response by selecting number: 0
        
        _____
        
        Engineering RFP: Mr Hankey's Christmas Emporium

        RFP Type: Engineering
        RFP Field (Request Type): Description
        
        Q-document response recommendations:
        1) Our DESCRIPTION of service is that we are good ENGINEERS
        
        Select response by selecting number: 1
        
        _____
        
        Engineering RFP: Mr Hankey's Christmas Emporium

        RFP Type: Engineering
        RFP Field (Request Type): Price
        
        Q-document response recommendations:
        2) The PRICE of our ENGINEERING services is an arm
        
        Select response by selecting number: 2

If we were to run a fourth training epoch but instead chose a different RFP, we would notice that
all responses are suggested. This is because Q-document has not received enough user input to threshold
out response suggestions for that portion of the state space. 



    



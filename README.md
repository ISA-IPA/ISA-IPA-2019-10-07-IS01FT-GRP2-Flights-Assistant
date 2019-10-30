# SECTION 1 : PROJECT TITLE
### Flights Assistant
![logo](Miscellaneous/Airplane.jpg)

# SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT
According to IATA, in 2017 airlines carried 4.1 billion passengers by air. Before booking a flight, passengers would have to spend time searching through various platforms to find the best flight deals. That is a lot of time spent searching for flight deals. The search for flight becomes a repetitive task that a passenger would need to perform over a period of time before they find the flight they want.

With the above, we see a potential to develop a service that helps passenger monitors the flight deals on their behalf and send them updates on deals, until the request ended.

Flight Assistant Chatbot (via WeChat app) is developed to help monitor flight deal based on users' request and send daily updates on flight deals they are looking for to their WeChat account. User can click on the hyperlink associated to the deal to access the deal and make the booking.

The decision to use WeChat is driven by the number of WeChat users worldwide and the exposure to both Android and iOS users, as compared to Google assistant.

Users can either send us a voice recording with the type flight request or they text us with the details of their flight request. Users can also specified the number of days that they would like us to monitor the request for.

With the above, our system will perform daily search and send the results to the users’ WeChat account. Users can also request to extend the monitoring for additional days. 


# SECTION 3 : CREDITS / PROJECT CONTRIBUTION
| Official Full Name | Student ID (MTech Applicable)| Work Items (Who Did What) | Email (Optional) |
| :---: | :---: | :---: | :---: |
| GONG YIFEI | A0198495E  | WeChat Bot (Receive Request, Send Result), Speech-to-Text | e0402036@u.nus.edu |
| JIANG YANNI | A0201097M  | RPA (Extract Flight Deals, Compare and generate final deals) | e0409752@u.nus.edu |
| NG SIEW PHENG | A0198525R  | RPA (Search Flight Deals, Export Search Result), Database functions | e0402066@u.nus.edu |


# SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO


# SECTION 5 : USER GUIDE
## Database
Install Mongo DB by following the instruction here https://docs.mongodb.com/manual/administration/install-community/

## Conda Environment
To set up the environment
1. git clone https://github.com/gabyngsp/IPA-CA1-FlightsAssistant/
2. cd IPA-CA1-FlightsAssistant
3. conda env create --file environment.yaml
4. conda activate FlightsAssistant
5. conda install -c conda-forge ffmpeg
6. python -m spacy download en_core_web_sm

## Start WeChat Bot
1. python thread.py
2. Open WeChat app and scan QR code generated

## Start request for new flight deals
1. add chatbot as your wechat friend
2. send a flight searching request, can use both text message and audio message

Some examples of request:
- I want to book a flight from Dalian to Shanghai on January 3rd and returning on January 5th for 1 adult and 2 children age 2 and 3
- I would like to book a flight from singapore to beijing on November 1st for 2 adults.
- Book a flight from Edinburgh to Dalian on December 10th, Dalian to Tokyo on December 15th, Tokyo to Osaka on December 20th








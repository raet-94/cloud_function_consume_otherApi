# Requirements

Install pip , python 3.7  in a virtual enviroment ( I used conda for this example)


## Testing

Install functions-framework using pip 
pip install functions-framework


after installing use 
functions-framework --target requesttoapi

This will create a flask server that will receive petitions on 

http://localhost:8080/

Open a second terminal and using curl send the info 


 curl --header "Content-Type: application/json" \             
                                    --request POST \
                                    --data '{"headers":{
                                      "Accept": "application/json",
                                      "Content-Type": "application/json"}
                                  , "url":"www.google.com", "querystring": "somequerystring", "data":{"1":2, "2":1}}' \
                                    http://localhost:8080/


 


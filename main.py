import requests
from flask import jsonify 

url = "https://someapi.com/"
querystring = {"somequerystring":"Date:[2020-01-01T02:00:00.000Z TO 2020-02-01T01:59:59.999Z]"}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}
def requesttoapi(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    #response = requests.request("GET", url, headers=headers, params=querystring)
    #respuesta = str(response.text)
    request_json = request.get_json()
    print(request_json)
    if request.args and 'message' in request.args:
        return request.args.get('message')
    #elif request_json and 'message' in request_json:
    #    print(request_json['url'])

    #    return request_json['url'] +  request_json['message'] 
    #    #return respuesta
    elif request_json:
        if 'url' in request_json and 'headers' in request_json and 'querystring' in request_json and 'data' in request_json:
            url= request_json['url']
            headers = request_json['headers']
            querystring = request_json["querystring"]
            data = request_json['data']
            petition = jsonify({'headers': str(headers), "url" : url, "querystring" : str(querystring), "data" : str(data)}) 
            response = requests.request("GET", url, headers=headers, params=querystring)
            petition_text= petition.get_data(as_text=True)
            received_response = str(response.text)
            respuesta= jsonify({'petition': petition_text, 'received_response': received_response})
            print(str(response.text))
            return respuesta 
        elif 'url' in request_json and 'headers' in request_json and 'querystring' in request_json:
            url= request_json['url']
            headers = request_json['headers']
            querystring = request_json["querystring"]            
            response = requests.request("GET", url, headers=headers, params=querystring)
            petition = jsonify({'headers': str(headers), "url" : url, "querystring" : str(querystring)}) 
            #print(response.text)
            petition_text= petition.get_data(as_text=True)
            received_response = str(response.text)
            respuesta= jsonify({'petition': petition_text, 'received_response': received_response})
            return respuesta 
        elif 'url' in request_json and 'headers' in request_json :
            url= request_json['url']
            headers = request_json['headers']
            respuesta = jsonify({'headers': str(headers), "url" : url}) 
            return respuesta        
        elif 'url' in request_json and 'message' in request_json:
            respuesta = jsonify({'message': str(request_json['message']), "url" : url}) 
            return respuesta   
    else:
        return f'Hello World!'

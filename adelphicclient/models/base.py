import logging
import json
import requests
import datetime

class Base:
    object = None

    def __init__(self, connection=None):
        self.connection = connection

    def get_by_id(self, endpoint):
        url = "{0}/{1}/{2}".format(self.connection.url, self.object, endpoint)
        response = self.make_request("GET", url)

        return self.get_response_object(response)

    def list_objects(self, url_params):
        url = "{0}/{1}/{2}".format(self.connection.url, self.object, url_params)
        response = self.make_request("GET", url)

        return self.get_response_list(response)

    def make_request(self, method, url, data=None):
        headers = self.connection.authenticate()

        if method == "GET":
            self.curl = "curl -H 'Content-Type: application/json' -H 'Authorization:Basic {0}' '{1}'".format(
                headers,
                url
            )
            response = requests.get(
                url,
                auth=headers,
                verify=False
            )

        if method == "POST":
            self.curl = "curl -H 'Content-Type: application/json' -H 'Authorization:Basic {0}' --data '{1}' '{2}'".format(
                headers,
                data,
                url
            )
            response = requests.post(
                url,
                auth=headers,
                headers={"Content-Type": "application/json"},
                data=data,
                verify=False
            )

        return response

    def get_response_list(self, response):
        data = json.loads(response.text)

        rval = {}
        rval["response_code"] = response.status_code
        rval["request_body"] = self.curl
        if response.status_code == 200:
            rval["msg_type"] = "success"
            rval["msg"] = "Success"
            rval["data"] = data.get('entity')
        else:
            rval["msg_type"] = "error"
            rval["msg"] = data.get('message')
            rval["data"] = data.get('errors')

        return json.dumps(rval)

    def get_response_object(self, response):
        data = json.loads(response.text)

        rval = {}
        rval["response_code"] = response.status_code
        rval["request_body"] = self.curl
        if response.status_code == 200:
            rval["msg_type"] = "success"
            rval["msg"] = "Success"
            rval["data"] = data.get('entity')
        else:
            rval["msg_type"] = "error"
            rval["msg"] = data.get('message')
            rval["data"] = data.get('errors')

        return json.dumps(rval)

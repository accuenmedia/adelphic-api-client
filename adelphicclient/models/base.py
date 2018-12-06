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
        response = requests.get(
            url,
            auth=self.connection.authenticate(),
            verify=False
        )

        return self.get_response_object(response)

    def list_objects(self, url_params):
        url = "{0}/{1}/{2}".format(self.connection.url, self.object, url_params)
        response = requests.get(
            url,
            auth=self.connection.authenticate(),
            verify=False
        )

        return self.get_response_list(response)

    def get_response_list(self, response):
        data = json.loads(response.text)

        rval = {}
        rval["response_code"] = response.status_code
        if response.status_code == 200:
            rval["msg_type"] = "success"
            rval["msg"] = ""
            rval["data"] = data.get('entity')
            rval["request_body"] = ""
        else:
            rval["msg_type"] = "error"
            rval["msg"] = data.get('message')
            rval["data"] = data.get('errors')
            rval["request_body"] = ""

        return json.dumps(rval)

    def get_response_object(self, response):
        data = json.loads(response.text)

        rval = {}
        rval["response_code"] = response.status_code
        if response.status_code == 200:
            rval["msg_type"] = "success"
            rval["msg"] = ""
            rval["data"] = data.get('entity')
            rval["request_body"] = ""
        else:
            rval["msg_type"] = "error"
            rval["msg"] = data.get('message')
            rval["data"] = data.get('errors')
            rval["request_body"] = ""

        return json.dumps(rval)

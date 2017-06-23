import requests
import json
import sys
import urllib

class InvalidAuth(Exception):
    def __init__(self, message, status=0):
        super(InvalidAuth, self).__init__(message, status)


class api(object):

    def __init__(self, host, port = 3000):
        self.grafana_host = host
        self.grafana_port = port
        self.api_url = 'http://{host}:{port}/api'.format(host=self.grafana_host, port=self.grafana_port)
        self.request_headers = dict()
        self.auth = tuple()
        

    def authBasic(self, username, password):
        self.auth = tuple([username, password])
        if 'Authorization' in self.request_headers.keys():
            del self.request_headers['Authorization']


    def authKey(self, key):
        self.api_key = key
        self.request_headers['Authorization'] = 'Bearer {api_key}'.format(api_key=self.api_key)


    def gen_url(self, endpoint, options=False):
        ret_val = '{base}/{endpoint}'.format(base=self.api_url, endpoint=endpoint)
        if options:
            ret_val = '{0}/{option}'.format(ret_val, option=options)
        return ret_val


    def check_response(self, response):
        response_json = response.json()
        if type(response_json) == dict and 'message' in response_json.keys() and (response_json['message'] == 'Invalid API key' or response_json['message'] == 'Invalid username or password'):
            raise InvalidAuth(message=response_json['message'], status=2)
            return False
        return True

    def datasources_get(self):
        """
        Queryies the existing datasources from grafana instance.
        
        :param genrow: row object
        :type genrow: grafanalib.dashboard.row
        
        :return: list of existing datasources.
        :rtyp: list
        """
        url = self.gen_url(endpoint='datasources')
        response = requests.get(url, headers=self.request_headers, auth=self.auth)

        if self.check_response(response):
            return response.json()
        else:
            return dict()

    def datasource_update(self, ident, data):
        """
        Udates a specific datasource.
        
        :param ident: id of datasource
        :type ident: int
        :param data: Full datasource definition
        :type data: dict
        
        :return: list of existing datasources.
        :rtyp: list
        """
        url = self.gen_url(endpoint='datasources', options=ident)
        response = requests.put(url, json=data, headers=self.request_headers, auth=self.auth)

        if self.check_response(response):
            return response
        else:
            return False

  
    def datasource_delete(self, ident):
        """
        Deletes a specific datasource.
        
        :param ident: id of datasource
        :type ident: int
        
        :return: requests respons.
        :rtyp: list
        """
        url = self.gen_url(endpoint='datasources', options=ident)
        response = requests.delete(url, headers=self.request_headers, auth=self.auth)

        if self.check_response(response):
            return response
        else:
            return False

  
    def datasource_create(self, data):
        """
        creates a specific datasource.
        
        :param data: the definition of the datasource
        :type data: dict
        
        :return: requests respons.
        :rtyp: list
        """
        url = self.gen_url(endpoint='datasources')
        response = requests.post(url, json=data, headers=self.request_headers, auth=self.auth)

        if self.check_response(response):
            return response
        else:
            return False


    def dashboards_get(self):
        url = self.gen_url(endpoint='search')
        response = requests.get(url, headers=self.request_headers, auth=self.auth)

        if self.check_response(response):
            return response.json()
        else:
            return False

  
    def dashboard_delete(self, ident):
        url = self.gen_url(endpoint='dashboards', options=ident)
        response = requests.delete(url, headers=self.request_headers, auth=self.auth)

        if self.check_response(response):
            return response
        else:
            return False

  
    def dashboard_create(self, data):
        transmit_data = {'dashboard': data, 'overwrite': True}
        url = self.gen_url(endpoint='dashboards/db')
        response = requests.post(url, json=transmit_data, headers=self.request_headers, auth=self.auth)

        if self.check_response(response):
            return response
        else:
            return False

    

  




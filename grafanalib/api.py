import requests
import json
import sys
import urllib

import click

class api(object):

    def __init__(self, key, host, port = 3000):
        self.api_key = key
        self.grafana_host = host
        self.grafana_port = port
        self.api_url = 'http://{host}:{port}/api'.format(host=self.grafana_host, port=self.grafana_port)

        self.request_headers = {'Authorization': 'Bearer {api_key}'.format(api_key=self.api_key)}

    def gen_url(self, endpoint, options=False):



        ret_val = '{base}/{endpoint}'.format(base=self.api_url, endpoint=endpoint)

        if options:
            ret_val = '{0}/{option}'.format(ret_val, option=options)
        # print ret_val
        return ret_val


    def check_response(self, response):
        response_json = response.json()
        if type(response_json) == dict and 'message' in response_json.keys() and response_json['message'] == 'Invalid API key':
            click.echo(click.style('Invalid API Key, set an new with --apikey', fg='red'))
            sys.exit(2)
            return False
        return True


    def datasources_get(self):
        url = self.gen_url(endpoint='datasources')
        response = requests.get(url, headers=self.request_headers)

        if self.check_response(response):
            return response.json()
        else:
            return False

    def datasource_update(self, ident, data):
        url = self.gen_url(endpoint='datasources', options=ident)
        response = requests.put(url, json=data, headers=self.request_headers)

        if self.check_response(response):
            return response
        else:
            return False

  
    def datasource_delete(self, ident):
        url = self.gen_url(endpoint='datasources', options=ident)
        response = requests.delete(url, headers=self.request_headers)

        if self.check_response(response):
            return response
        else:
            return False

  
    def datasource_create(self, data):
        url = self.gen_url(endpoint='datasources')
        response = requests.post(url, json=data, headers=self.request_headers)

        if self.check_response(response):
            return response
        else:
            return False


    def dashboards_get(self):
        url = self.gen_url(endpoint='search')
        response = requests.get(url, headers=self.request_headers)

        if self.check_response(response):
            return response.json()
        else:
            return False

  
    def dashboard_delete(self, ident):
        url = self.gen_url(endpoint='dashboards', options=ident)
        response = requests.delete(url, headers=self.request_headers)

        if self.check_response(response):
            return response
        else:
            return False

  
    def dashboard_create(self, data):
        transmit_data = {'dashboard': data, 'overwrite': True}
        url = self.gen_url(endpoint='dashboards/db')
        response = requests.post(url, json=transmit_data, headers=self.request_headers)

        if self.check_response(response):
            return response
        else:
            return False

    

  




class datasource(object):

    def __init__(self, name):
        self.defaultport = 80
        self.struct = {
                        "orgId": 1,
                        "name": name,
                        "type": "",
                        "typeLogoUrl": "",
                        "access": "proxy",
                        "url": "",
                        "password": "",
                        "user": "",
                        "database": "",
                        "basicAuth": False,
                        "basicAuthUser": "",
                        "basicAuthPassword": "",
                        "withCredentials": False,
                        "isDefault": True,
                        "jsonData": dict(),
                        "secureJsonFields": None
                      }

    def get(self):
        return self.struct

    def get_name(self):
        return self.struct['name']

    def set_url(self, url):
        self.struct['url'] = url
        return True

    def get_url(self):
        return self.struct['url']

    def set_host(self, host, port=None):
        if not port:
            port = self.defaultport

        self.set_url('http://{host}:{port}'.format(host=host, port=port))
        return True

    def overwrite_external(self, external_datasource):
        copy_of_external = dict(external_datasource)
        for key in self.struct.keys():
            copy_of_external[key] = self.struct[key]

        return copy_of_external


class graphite(datasource):

    def __init__(self, name='graphite'):
        super(graphite, self).__init__(name)
        self.struct['type'] = "graphite"
        self.struct['typeLogoUrl'] = "public/app/plugins/datasource/graphite/img/graphite_logo.png"
        self.defaultport = 8080
 

class influxdb(datasource):

    def __init__(self, name='influxdb'):
        super(influxdb, self).__init__(name)
        self.struct['type'] = "influxdb"
        self.struct['typeLogoUrl'] = "public/app/plugins/datasource/influxdb/img/influxdb_logo.svg"
        self.defaultport = 8086
 

    def set_db(self, db):
        self.struct['database'] = db
        return True

    def get_db(self):
        return self.struct['database']
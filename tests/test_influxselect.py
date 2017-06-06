import unittest2
import grafanalib



class influxselect_tests(unittest2.TestCase):

    def setUp(self):
        self.influx_select = grafanalib.dashboard.influx_select('test1')


    def tearDown(self):
        del self.influx_select


    def test_influxselect_blank(self):
        alltypes = [i['type'] for i in self.influx_select.struct]
        self.assertEqual(alltypes.count('field'), 1)

        for b in self.influx_select.struct:
            if b['type'] == 'field':
                self.assertEqual(b['params'][0], 'test1')

        self.assertEqual(alltypes.count('mean'), 1)


    def test_influxselect_alterField(self):
        self.influx_select.add_func('field', ['test2'])
        
        alltypes = [i['type'] for i in self.influx_select.struct]
        self.assertEqual(alltypes.count('field'), 1)

        for b in self.influx_select.struct:
            if b['type'] == 'field':
                self.assertEqual(b['params'][0], 'test2')
        

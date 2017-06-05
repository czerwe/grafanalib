import unittest2
import grafanalib



class dashboard_tests(unittest2.TestCase):

    def setUp(self):
        self.dashboard = grafanalib.dashboard.dashboard()


    def tearDown(self):
        del self.dashboard


    def test_dashboard_blank(self):
        # self.assertEqual(len(self.dashboard.struct['rows']), 0)
        self.assertEqual(len(self.dashboard.get()['rows']), 0)


    def test_dashboard_1row(self):
        row1 = grafanalib.dashboard.row()
        self.dashboard.add_row(row1)
        self.assertEqual(len(self.dashboard.get()['rows']), 1)


    def test_dashboard_2row(self):
        row1 = grafanalib.dashboard.row()
        row2 = grafanalib.dashboard.row()
        self.dashboard.add_row(row1)
        self.dashboard.add_row(row2)
        self.assertEqual(len(self.dashboard.get()['rows']), 2)



    def test_dashboard_2row(self):
        row1 = grafanalib.dashboard.row()
        row2 = grafanalib.dashboard.row()
        row3 = grafanalib.dashboard.row()
        row4 = grafanalib.dashboard.row()
        row5 = grafanalib.dashboard.row()
        self.dashboard.add_row(row1)
        self.dashboard.add_row(row2)
        self.dashboard.add_row(row3)
        self.dashboard.add_row(row4)
        self.dashboard.add_row(row5)
        self.assertEqual(len(self.dashboard.get()['rows']), 5)

        graph1 = grafanalib.dashboard.graph()
        graph2 = grafanalib.dashboard.graph()
        graph3 = grafanalib.dashboard.graph()

        row1.add_panel(graph1)
        row2.add_panel(graph2)
        row5.add_panel(graph3)

        self.assertEqual(self.dashboard.get()['rows'][0]['panels'][0]['id'], 1)
        self.assertEqual(self.dashboard.get()['rows'][1]['panels'][0]['id'], 2)
        self.assertEqual(self.dashboard.get()['rows'][4]['panels'][0]['id'], 3)

        # self.assertEqual(self.dashboard.get()['rows']['panels'][0]['index'], 5)




class row_tests(unittest2.TestCase):

    def setUp(self):
        self.row = grafanalib.dashboard.row()


    def tearDown(self):
        del self.row


    def test_dashboard_blank(self):
        # self.assertEqual(len(self.dashboard.struct['rows']), 0)
        self.assertEqual(len(self.row.get()['panels']), 0)


    def test_dashboard_1row(self):
        panel1 = grafanalib.dashboard.panel()
        self.row.add_panel(panel1)
        self.assertEqual(len(self.row.get()['panels']), 1)



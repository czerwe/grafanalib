
class dashboard(object):

    def __init__(self):
        self.struct = {
            "id": None,
            "title": "",
            "originalTitle": "",
            "tags": ['dpfprofiles'],
            "style": "dark",
            "timezone": "browser",
            "editable": True,
            "hideControls": False,
            "sharedCrosshair": False,
            "rows": [],
            "time": {"from": "now-3h", "to": "now"},
            "timepicker": {
                "refresh_intervals": ["5s", "10s", "30s", "1m", "5m", "15m", "30m", "1h", "2h", "1d"],
                "time_options": [ "5m", "15m", "1h", "6h", "12h", "24h", "2d", "7d", "30d"]
            },
            "templating": {"list": []},
            "annotations": {"list": []},
            "schemaVersion": 8,
            "version": 0,
            "links": []
        }

        self.rows = list()
        self.templates  = list()


    def add_row(self, genrow):
        self.rows.append(genrow)


    def set_title(self, title):
        for i in ['title', 'originalTitle']:
            self.struct[i] = title
        return False

    def add_template(self, template):
        self.templates.append(template)

    def get(self):
        ret_val = dict(self.struct)
        ret_val['rows'] = [i.get() for i in self.rows]
        ret_val['templating']['list'] = [i.get() for i in self.templates]
        return ret_val



class template(object):
    def __init__(self, querytype='query'):
        self.struct = {
              "type": querytype,
              "datasource": None,
              "refresh": 1,
              "name": "unnamed_template",
              "hide": 0,
              "options": [],
              "includeAll": False,
              "multi": True,
              "label": "Unlabeld Template",
              "query": "",
              "current": {
                "text": "All",
                "value": [
                  "$__all"
                ],
                "tags": []
              }
            }


    def set_refresh(self, value):
        self.struct['refresh'] = value

    def set_option(self, key, value):
        if key == 'includeAll':
            if value:
                self.struct['includeAll'] = True

                include_all_option = {
                                  "text": "All",
                                  "value": "$__all",
                                  "selected": True
                                }
                self.struct['current'] = {
                                  "text": "All",
                                  "value": [
                                    "$__all"
                                  ],
                                  "tags": []
                                }
                self.struct['options'].insert(0, include_all_option)
            else:
                self.struct['includeAll'] = False

        if key == 'multi' and type(value) == bool:
            self.struct['multi'] = value


    def set_query(self, query):
        self.struct['query'] = query

    def set_name(self, name, label=False):
        if not label:
            label = name

        self.struct['label'] = label
        self.struct['name'] = name


    def add_choiceOption(self, name, selected=False):
        option = {
              "text": name,
              "value": name,
              "selected": selected
            }

        self.struct['options'].append(option)

    def get(self):
        ret_val = dict(self.struct)
        return ret_val




class row(object):
    def __init__(self, indexStart = 1, title = 'Row', height="250px", max_span=12):
        self.struct = {
            "collapse": False,
            "editable": True,
            "height": height,
            "panels": [],
            "title": title
        }
        self.indexStart = indexStart
        self.panels = list()

        self.max_span = max_span


    def getNextIndex(self):
        return int(self.indexStart + len(self.panels))

    def add_panel(self, genpanel):
        if len(self.panels) == 12:
            print "Can't take any more panels"
            return False

        self.panels.append(genpanel)


    def get(self):
        ret_val = dict(self.struct)
        ret_val['panels'] = self.recaluclate_span([i.get() for i in self.panels])
        return ret_val

    def recaluclate_span(self, panels):
        amount_of_panels = len(panels)
        if not len(panels) == 0:
            remains = 12 % amount_of_panels
            span_per_panel = int(12 / amount_of_panels)

            for ipanel in panels:
                if span_per_panel <= self.max_span:
                    ipanel['span'] = span_per_panel
                else:
                    ipanel['span'] = self.max_span

                ipanel['id'] = self.indexStart + panels.index(ipanel)
            panels[0]['span'] += remains

        return panels



class panel(object):

    def __init__(self):
        self.struct = dict()
        self.manually_spaned = False

    def get(self):
        ret_val = dict(self.struct)

        return ret_val

    def set_span(self, span):
        self.struct['span'] = span
        self.manually_spaned = True

    def is_spanned(self):
        return self.manually_spaned

class text(panel):

    def __init__(self, title=''):
        super(text, self).__init__()
        self.struct = {
              "title": title,
              "error": False,
              "span": 12,
              "editable": True,
              "type": "text",
              "isNew": True,
              "id": None,
              "mode": "html",
              "content": "",
              "links": [],
              "transparent": True
            }


    def set_html(self, text):
        self.struct['mode'] = "html"
        self.struct['content'] = text



class graph(panel):

    def __init__(self):
        super(graph, self).__init__()
        self.struct = {
            "aliasColors": {},
            "bars": False,
            "datasource": None,
            "editable": True,
            "error": False,
            "fill": 1,
            "grid": {
              "threshold1": None,
              "threshold1Color": "rgba(216, 200, 27, 0.27)",
              "threshold2": None,
              "threshold2Color": "rgba(234, 112, 112, 0.22)"
            },
            "id": None,
            "isNew": True,
            "legend": { "avg": False, "current": False, "max": False, "min": False, "show": True, "total": False, "values": False},
            "lines": True,
            "linewidth": 2,
            "links": [],
            "nullPointMode": "connected",
            "percentage": False,
            "pointradius": 5,
            "points": False,
            "renderer": "flot",
            "seriesOverrides": [],
            "span": 12,
            "stack": False,
            "steppedLine": False,
            "targets": [
                # {
                #     "refId": "A",
                #     "target": "alias(dockerimages.cassandra-1.mem, 'cassandra 1')"
                # },
            ],
            "timeFrom": None,
            "timeShift": None,
            "title": "Container MEM Consumption (%)",
            "tooltip": { "shared": True, "value_type": "cumulative"},
            "type": "graph",
            "xaxis": {
              "show": True
            },
            "yaxes": [
              {
                "format": "short",
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True
              },
              {
                "format": "short",
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True
              }
            ]
        }

        self.refidCounter = 65
        self.targets = list()

    def add_target(self, gentarget, yaxis=0):
        if self.refidCounter >= 90:
            print 'noRefNumbersLeft'
            return False

        target = {'refId': chr(self.refidCounter), "target": gentarget}
        self.targets.append(target)

        self.refidCounter += 1


    def set_title(self, title):
        self.struct['title'] = title


    def get(self):
        ret_val = dict(self.struct)
        ret_val['targets'] = self.targets

        return ret_val

    def alter_grid(self, key, value):
        self.struct['grid'][key] = value




    def display_y_as(self, display_type='short', yaxis=0):
        # print yaxis
        self.struct['yaxes'][yaxis]['format'] = display_type

    def display_percent(self, infitive_max=True, yaxis=0):
        self.struct['yaxes'][yaxis]['format'] = 'percent'
        self.struct['yaxes'][yaxis]['min'] = 0
        if infitive_max:
            maxval = None
        else:
            maxval = 100
        self.struct['yaxes'][yaxis]['max'] = maxval

    def min_max(self, min=None, max=None, yaxis=0):
        self.struct['yaxes'][yaxis]['min'] = min
        self.struct['yaxes'][yaxis]['max'] = max



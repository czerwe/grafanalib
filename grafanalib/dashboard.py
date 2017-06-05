import json

class ApiNotUnique(Exception):
    def __init__(self, message, status=0):
        super(ApiNotUnique, self).__init__(message, status)


GRAPHTOOTIP_DEFAULT = 0
GRAPHTOOTIP_SHAREDCROSSHAIR = 1
GRAPHTOOTIP_SHAREDTOOTIP = 2


class dashboard(object):
    """
    Dashboard object
    
    :rtype: grafanalib.dashboard.dashboard
    """
    def __init__(self):
        self.struct = {
            "annotations": {"list": []},
            "editable": True,
            "gnetId": None,
            "graphTooltip": GRAPHTOOTIP_DEFAULT,
            "hideControls": False,
            "id": None,
            "links": [],
            "rows": [],
            "schemaVersion": 14,
            "style": 'dark',
            "tags": [''],
            "templating": {"list": []},
            "time": {"from": "now-3h", "to": "now"},
            "timepicker": {
                "refresh_intervals": ["10s", "30s", "1m", "5m", "15m", "30m", "1h", "2h", "1d"],
                "time_options": [ "5m", "15m", "1h", "6h", "12h", "24h", "2d", "7d", "30d"]
            },
            "timezone": "browser",
            "title": "",
            "version": 0,
        }

        self.rows = list()
        self.templates  = list()


    def __enter__(self):
        return self


    def __exit__(self, *args):
        pass


    def add_row(self, genrow):
        """
        Add an row to the dashboard.
        
        :param genrow: row object
        :type genrow: grafanalib.dashboard.row
        
        :return: None
        :rtype: None
        """
        self.rows.append(genrow)


    def set_title(self, title):
        """
        Alter the title of the Dashboard.
        
        :param title: New title
        :type title: str
        
        :return: None
        :rtype: None
        """
        for i in ['title', 'originalTitle']:
            self.struct[i] = title
        # return False

    def set_tooltip(self, tooltipnum):
        """
        Set the Dashboard shared Tooltip setting.
        0 = default; 1 = shared crosshair; 2 = shared tooltip
        
        :param title: Value for the tooltip.
        :type title: int
        
        :return: success bool
        :rtype: bool
        """
        if tooltipnum in [0, 1, 2]:
            self.struct['graphTooltip'] = tooltipnum
            return True
        else:
            return False


    def add_template(self, template):
        """
        Add a template to the Dashboard.
        
        :param template: template object
        :type template: grafanalib.dashboard.row
        
        :return: None
        :rtype: None
        """
        self.templates.append(template)

    def get(self):
        """
        Returns the constructed dashboard as dictionary.
        
        :return: Generated Dashboard dictionary
        :rtype: dict
        """
        ret_val = dict(self.struct)
        ret_val['rows'] = [i.get() for i in  self.rows]
        ret_val['templating']['list'] = [i.get() for i in self.templates]
        return ret_val

    def get_json(self):
        return json.dumps(self.get(), sort_keys=True, indent=4)

    def set_refresh(self, rate):
        available_intervals = self.struct['timepicker'].get('refresh_intervals', list())
        if rate in available_intervals:
            self.struct['refresh'] = rate
            #TODO make a proper exception
            return True
        else:
            return False





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
    """
    row object
    
    :param indexStart: index of the first panel of the row
    :type indexStart: int
    :param title: Title of the row
    :type title: str
    :param height: Height in pixel (250px)
    :type height: str
    :param max_span: Maximum span of the row, needs for autocalculate the span of each panel
    :type max_span: int
        
    :rtype: grafanalib.dashboard.row
    """

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
        """
        Returns and index that is calulated by the startIndex and amount of panels
        
        :return: New index number
        :rtype: int
        """
        return int(self.indexStart + len(self.panels))


    def add_panel(self, genpanel):
        """
        Add an panel

        :param genpanel: The Panel or an child instance
        :type genpanel: grafanalib.dashboard.panel

        """
        if len(self.panels) == 12:
            print "Can't take any more panels"
            return False

        self.panels.append(genpanel)


    def get(self):
        """
        Returns the constructed dashboard as dictionary.
        
        :return: Generated Dashboard dictionary
        :rtype: dict
        """
        ret_val = dict(self.struct)
        ret_val['panels'] = self.recaluclate_span([i.get() for i in self.panels])
        return ret_val


    def recaluclate_span(self, panels):
        """
        The span for each panel will be recaculated if not stated otherwise. The span will be entered into the panel objects
        
        :param panels: list of panels
        :type panels: grafanalib.dashboard.panel

        """
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

        # target = {'refId': chr(self.refidCounter), "target": gentarget}
        # self.targets.append(target)
        self.targets.append(gentarget)

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



class target(object):
    def __init__(self, refId='A'):
        self.refId = refId




class tgt_infux(target):
    def __init__(self, measurement, refId='A'):
        super(tgt_infux, self).__init__(refId)
        
        self.struct = {
            'dsType': 'influxdb',
            'measurement': measurement,
            'policy': 'default',
            'refId': self.refId,
            'resultFormat': "time_series",
            'groupBy': list(),
            'select': list(),
            'tags': list(),
            'alias': ''
        }
        self.selects = list()

        self.add_groupby(grouptype='time', parameter=['$__interval'])
        self.add_groupby(grouptype='fill', parameter=['linear'])


    def add_tag(self, key, value, operator = '='):
        self.struct['tags'].append({'key': key, 'operator': operator, 'value': value})

    def add_groupby(self, grouptype, parameter = []):
        res = self.mod_groupby(grouptype, parameter)
        if not res:
            self.struct['groupBy'].append({'type': grouptype, 'params': parameter})
    
    def mod_groupby(self, grouptype, parameter = []):
        for extype in self.struct['groupBy']:
            if extype['type'] == grouptype:
                extype['type']['params'] = parameter
                return True
        return False

    def add_select(self, select):
        self.selects.append(select)

    def get(self):
        self.struct['select'] = list()

        for i in self.selects:
            self.struct['select'].append(i.get())
        return self.struct



class influx_select(object):
    def __init__(self, field):
        self.struct = list()
        self.struct.append({'type': "field", 'params': [field]})
        self.struct.append({'type': "mean", 'params': []})

    def get(self):
        return self.struct


    def add_func(self, funcname, parameter=[]):
        res = self.mod_func(funcname, parameter)
        if not res:
            self.struct.append({'type': funcname, 'params': parameter})
    
    def mod_func(self, funcname, parameter = []):
        for extype in self.struct:
            if extype['type'] == funcname:
                extype['type']['params'] = parameter
                return True
        return False


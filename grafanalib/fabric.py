import dashboard

global THRESHOLD
THRESHOLD = ['rgba(216, 200, 27, 0.27)', 'rgba(234, 112, 112, 0.22)']


def normal_graph(title, targets, minimum_y_value=0, thresholds=[]):
    return_value = dashboard.graph()
    return_value.set_title(title)
    return_value.min_max(min=minimum_y_value)
    for target in targets:
        return_value.add_target(target)

    for threshold in thresholds:
        threshold_index = thresholds.index(threshold)

        if threshold_index > 1:
            break
        name = 'threshold{0}'.format(str(threshold_index + 1))
        return_value.alter_grid( key=name, value=threshold[0])
        try:
           return_value.alter_grid( key='{0}Color'.format(name), value=threshold[1])
        except:
            return_value.alter_grid( key='{0}Color'.format(name), value=THRESHOLD[threshold_index])

    return return_value

def data_graph(title, targets, minimum_y_value=0, datasize='bytes', thresholds=[]):
    return_value = dashboard.graph()
    return_value.set_title(title)
    return_value.min_max(min=minimum_y_value)
    return_value.display_y_as(datasize)
    for target in targets:
        return_value.add_target(target)

    for threshold in thresholds:
        threshold_index = thresholds.index(threshold)

        if threshold_index > 1:
            break
        name = 'threshold{0}'.format(str(threshold_index + 1))
        return_value.alter_grid( key=name, value=threshold[0])
        try:
           return_value.alter_grid( key='{0}Color'.format(name), value=threshold[1])
        except:
            return_value.alter_grid( key='{0}Color'.format(name), value=THRESHOLD[threshold_index])

    return return_value

def percent_graph(title, targets, infitive_max=True, thresholds=[]):
    return_value = dashboard.graph()
    return_value.set_title(title)

    return_value.display_percent(infitive_max=infitive_max)

    for threshold in thresholds:
        threshold_index = thresholds.index(threshold)

        if threshold_index > 1:
            break
        name = 'threshold{0}'.format(str(threshold_index + 1))
        return_value.alter_grid( key=name, value=threshold[0])
        try:
           return_value.alter_grid( key='{0}Color'.format(name), value=threshold[1])
        except:
            return_value.alter_grid( key='{0}Color'.format(name), value=THRESHOLD[threshold_index])

    for target in targets:
        return_value.add_target(target)

    return return_value
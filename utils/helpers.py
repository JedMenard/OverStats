## Extracts a specified hero's metrics from the supplied data
def get_hero(data, hero):
    mode = 'competitive' if 'competitive' in \
           data['stats'].keys() else 'quickplay'
    return data['stats'][mode][hero]

def get_support(data):
    # TODO: Return a dict of all healers

def get_tanks(data):
    # TODO: Return a dict of all tanks

def get_dps(data):
    # TODO: Return a dict of all dps

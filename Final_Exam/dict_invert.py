def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    invert = {}
    for k, v in d.items():
        keys = invert.setdefault(v, [])
        keys.append(k)
        keys.sort()
    return invert
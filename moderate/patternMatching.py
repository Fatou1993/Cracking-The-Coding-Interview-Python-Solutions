def patternMatching(value, pattern):
    """
    :param value:
    :param pattern:
    :return:
    """
    str_length = len(value)
    pattern_length = len(pattern)
    if pattern_length == 1 : return str_length != 0
    if pattern_length == 0 : return str_length == 0
    

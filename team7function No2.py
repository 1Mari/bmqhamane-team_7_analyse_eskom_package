
# Function 2:

def five_num_summary(items):

     """Return dict of five number summery:
            max, median, min, q1, and q3.
    
    Args: 
        items (list): A list containing float values.
    
    Return:
        dict: dict of 7 key, value:
            {'name of number summery': value rounded to 2 decimals, etc}.
    
    Example:
        Input: five_num_summary([5,10,15,20,25,30])
        Output: {'max': 30, 'median': 17.5, 'min': 5, 'q1': 11.25, 'q3': 23.75}
    """


def five_num_summary(items):
    dictionary = {'max':0, 'median':0, 'min':0, 'q1':0, 'q3':0}
    dictionary['max'] = np.max(items).round(2)
    dictionary['median'] = np.median(items).round(2)
    dictionary['min'] = np.min(items).round(2)
    dictionary['q1'] = np.percentile(items, 25).round(2)
    dictionary['q3'] = np.percentile(items, 75).round(2)
    return dictionary

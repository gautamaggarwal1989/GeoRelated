''' Range to precision converter. It takes the range
from the settings and convert it into the precision.'''
from django.conf import settings


def geosearch_precision(range_in_kms=settings.GEOSEARCH_RANGE):
    
    if range_in_kms >= 2 and range_in_kms <= 5:
        return 5
    
    elif range_in_kms > 5 and range_in_kms <= 29:
        return 4
    
    else:
        raise Exception('Range not supported!')

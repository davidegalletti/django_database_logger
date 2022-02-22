from django.http import HttpResponse
import logging
from database_logger.models import LogEntry

test1_logger = logging.getLogger('test1')

def test1(request):
    kwargs = LogEntry.kwargs_from_request(request)
    kwargs["action_performed"] = 'Test 1'
    kwargs["some_extra_data"] = [{
        'key1': 'This is a dictionary',
        'key2': 'Still a dictionary',
    }]
    test1_logger.info(kwargs["action_performed"], kwargs)


    return HttpResponse("DEBUG")

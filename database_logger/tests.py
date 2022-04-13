import datetime

from django.db.models import Model
from django.test import TestCase
import logging
from .models import LogEntry
from .logger import DatabaseLogHandler
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class DBLoggerModelTests(TestCase):
    def __init__(self, *args, **kwargs):
        super(DBLoggerModelTests, self).__init__(*args, **kwargs)
        self.logger = self.init_logger()
        self.user = self.init_user()


    def init_logger(self):
        logger = logging.getLogger('db_logger')
        logger.setLevel(logging.DEBUG)
        dbh = DatabaseLogHandler()
        dbh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        dbh.setFormatter(formatter)
        logger.addHandler(dbh)
        return logger

    def init_user(self):
        try:
            usr = User.objects.get(username='pippo')
        except Model.DoesNotExists:
            usr = User(username='pippo', last_name='Gota', first_name='Filippo', password='lapassword')
            usr.save()
        authenticate(username='pippo', password='lapassword')
        return usr


    def test_is_writing(self):
        """verifica se trova il messaggio nel database"""
        db_logger = self.logger
        usr = self.user
        rf = RequestFactory()
        kwargs = {
                'action_peformed': 'test_is_writing'
        }
        request = rf.post('/pippo/', data=kwargs, HTTP_USER_AGENT='Mozilla/5.0')
        request.user = usr
        kwargs = LogEntry.kwargs_from_request(request)
        msg = "un messaggio di test"
        db_logger.info(msg, kwargs)
        logentry = LogEntry.objects.filter().order_by('-creation_time').first()
        testvar = msg in logentry.message
        self.assertIs(testvar, True)

    def test_user(self):
        """verifica se il log è associato all'utente"""
        db_logger = self.logger
        usr = self.user
        rf = RequestFactory()
        request = rf.post('/pippo/', HTTP_USER_AGENT='Mozilla/5.0')
        request.user = usr
        kwargs = LogEntry.kwargs_from_request(request)
        kwargs['action_performed'] = 'test_user'
        msg = "verifica utente"
        db_logger.info(msg, kwargs)
        logentry = LogEntry.objects.filter().order_by('-creation_time').first()
        self.assertIs(usr.id, logentry.auth_user_object_id)

    def test_extra_info(self):
        """verifica se l'extra_info è associato correttamente"""
        db_logger = self.logger
        usr = self.user
        rf = RequestFactory()
        request = rf.post('/pippo/', HTTP_USER_AGENT='Mozilla/5.0')
        request.user = usr
        kwargs = LogEntry.kwargs_from_request(request)
        kwargs['action_performed'] = 'test_extra_info'
        now = datetime.datetime.now()
        my_extra_info = f'timed extra info {now}'
        kwargs['my_extra_info'] = my_extra_info
        msg = "verifica extra_info"
        db_logger.info(msg, kwargs)
        last_logentry = LogEntry.objects.all().order_by('-creation_time').first()
        ei_logentry = LogEntry.objects.filter(extra_info_json__my_extra_info=my_extra_info).order_by('-creation_time').first()
        self.assertEquals(last_logentry.pk, ei_logentry.pk)



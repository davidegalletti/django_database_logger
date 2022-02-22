#!/bin/bash
date >> /tmp/peace_database_logger_notify.log
printf "INIZIO database_logger_notify\n"  >> /tmp/peace_database_logger_notify.log
cd /var/www/peace
source /home/admin/.virtualenvs/rdp/bin/activate
python manage.py database_logger_notify  --settings rdp.settings_peace   >> /tmp/peace_database_logger_notify.log
date >> /tmp/peace_database_logger_notify.log
printf "FINE database_logger_notify\n"  >> /tmp/peace_database_logger_notify.log

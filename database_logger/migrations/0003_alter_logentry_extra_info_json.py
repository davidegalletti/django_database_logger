# Generated by Django 4.0.3 on 2022-04-12 14:49

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_logger', '0002_alter_logentry_level_name_alter_logentry_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logentry',
            name='extra_info_json',
            field=models.JSONField(default='{}', encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
    ]

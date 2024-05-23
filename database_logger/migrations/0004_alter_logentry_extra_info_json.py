# Generated by Django 4.0.4 on 2022-04-22 12:32

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_logger', '0003_alter_logentry_extra_info_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logentry',
            name='extra_info_json',
            field=models.JSONField(default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
    ]
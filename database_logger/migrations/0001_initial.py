# Generated by Django 4.0.2 on 2022-02-22 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('message', models.TextField()),
                ('level_no', models.SmallIntegerField()),
                ('level_name', models.CharField(max_length=50)),
                ('func_name', models.CharField(max_length=255)),
                ('module', models.CharField(max_length=255)),
                ('path_name', models.CharField(max_length=255)),
                ('file_name', models.CharField(max_length=255)),
                ('line_no', models.BigIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('process', models.BigIntegerField()),
                ('process_name', models.CharField(max_length=255)),
                ('thread', models.BigIntegerField()),
                ('thread_name', models.CharField(max_length=255)),
                ('main_instance_object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('main_instance_role', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('secondary_instance_object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('secondary_instance_role', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('action_performed', models.CharField(db_index=True, max_length=100)),
                ('extra_info_json', models.JSONField(default='{}')),
                ('auth_user_object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('auth_user_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.contenttype')),
                ('main_instance_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.contenttype')),
                ('secondary_instance_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LogUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('involved_user_object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('role', models.CharField(db_index=True, max_length=255)),
                ('involved_user_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.contenttype')),
                ('log_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='involved_users', to='database_logger.logentry')),
            ],
        ),
        migrations.CreateModel(
            name='LogEntities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('role', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.contenttype')),
                ('log_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='involved_entities', to='database_logger.logentry')),
            ],
        ),
    ]

# Generated by Django 2.2.6 on 2019-11-23 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CampusModel', '0009_auto_20191118_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_select',
            name='teacher',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.1.5 on 2019-04-15 03:36

from django.db import migrations
from django.db import connection
from ..SQL_Create_Table import *

def make_trigger(apps,schema_editor):

   with connection.cursor() as cursor:
      cursor.execute(create_employee_table)


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0003_clock_table'),
    ]

    operations = [
        migrations.RunPython(make_trigger)
    ]
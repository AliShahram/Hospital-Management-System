# Generated by Django 2.1.5 on 2019-04-20 00:24

from django.db import migrations
from ..SQL_Create_Table import *
from django.db import connection

def make_trigger(apps,schema_editor):

   with connection.cursor() as cursor:
      cursor.execute(CREATE_EMP_DOC_ADMIN_RECEP)

class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0006_auto_20190420_0013'),
    ]

    operations = [
        migrations.RunPython(make_trigger)
    ]

# Generated by Django 2.0.6 on 2018-09-06 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20180906_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='senddata',
            old_name='age',
            new_name='years_of_Experience',
        ),
    ]

# Generated by Django 2.0.6 on 2018-09-07 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20180906_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senddata',
            name='years_of_Experience',
            field=models.CharField(max_length=2),
        ),
    ]

# Generated by Django 2.1.4 on 2018-12-17 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trailerapp', '0005_auto_20181217_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='language',
            field=models.CharField(max_length=8, null=True),
        ),
    ]

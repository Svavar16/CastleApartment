# Generated by Django 2.2.1 on 2019-05-16 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Apartments', '0004_auto_20190516_1119'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='searchhistory',
            unique_together=set(),
        ),
    ]

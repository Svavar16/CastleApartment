# Generated by Django 2.2.1 on 2019-05-14 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_profileimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carddetails',
            old_name='save',
            new_name='saved',
        ),
    ]
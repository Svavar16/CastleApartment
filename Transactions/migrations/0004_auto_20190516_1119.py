# Generated by Django 2.2.1 on 2019-05-16 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Transactions', '0003_auto_20190515_1059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transactions',
            options={'permissions': (('can_view_transactions', 'Can View Transactions'),)},
        ),
    ]
# Generated by Django 2.2.1 on 2019-05-09 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streetName', models.CharField(max_length=255)),
                ('houseNumber', models.IntegerField()),
                ('city', models.CharField(max_length=255)),
                ('postalCode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Apartments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('size', models.FloatField()),
                ('rooms', models.IntegerField()),
                ('privateEntrance', models.BooleanField()),
                ('animalsAllowed', models.BooleanField()),
                ('garage', models.BooleanField()),
                ('yearBuild', models.IntegerField()),
                ('description', models.CharField(max_length=999)),
                ('locationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apartments.Location')),
                ('sellerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('can change_price', 'Can change price'),),
            },
        ),
        migrations.CreateModel(
            name='ApartmentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=999)),
                ('apartmentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apartments.Apartments')),
            ],
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-12 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_building_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=45)),
                ('building_name', models.CharField(max_length=45)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
    ]

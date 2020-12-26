# Generated by Django 3.1 on 2020-09-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('local_phone_number', models.IntegerField()),
                ('position', models.CharField(max_length=150)),
                ('room_location', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'کارکنان',
                'verbose_name_plural': 'کارکنان',
            },
        ),
    ]
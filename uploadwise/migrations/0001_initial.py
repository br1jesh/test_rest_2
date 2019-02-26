# Generated by Django 2.1.5 on 2019-02-19 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='upobsid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.IntegerField()),
                ('OBSID', models.CharField(max_length=500)),
                ('Datetime', models.CharField(max_length=50)),
                ('r1', models.CharField(max_length=500)),
                ('r1size', models.CharField(max_length=50)),
                ('r1date', models.CharField(max_length=50)),
                ('r2', models.CharField(max_length=500)),
                ('r2size', models.CharField(max_length=50)),
                ('r2date', models.CharField(max_length=50)),
                ('r3', models.CharField(max_length=500)),
                ('r3size', models.CharField(max_length=50)),
                ('r3date', models.CharField(max_length=50)),
            ],
        ),
    ]
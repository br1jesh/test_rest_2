# Generated by Django 2.1.5 on 2019-06-02 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dqrreport', '0017_auto_20190602_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QC1_CNT',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QC1_DID',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QC1_PID',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QC1_SG',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QC2_CNT',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QC2_DID',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QC2_PID',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QC2_SG',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QC3_CNT',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QC3_DID',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QC3_PID',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QC3_SG',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.5 on 2021-02-01 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210126_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anopublicacao',
            name='ano',
            field=models.CharField(max_length=4, unique=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='file',
            field=models.FileField(upload_to='documentos/pdfs/'),
        ),
    ]

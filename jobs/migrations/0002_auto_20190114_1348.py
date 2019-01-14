# Generated by Django 2.1.5 on 2019-01-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='fulltext',
            field=models.TextField(default='My full text'),
        ),
        migrations.AddField(
            model_name='job',
            name='show',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='My title', max_length=50),
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-10 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='curso',
            field=models.CharField(default='TDS', max_length=100),
            preserve_default=False,
        ),
    ]
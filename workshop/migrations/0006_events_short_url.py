# Generated by Django 2.0.6 on 2019-09-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0005_auto_20190911_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='short_url',
            field=models.CharField(default=2, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
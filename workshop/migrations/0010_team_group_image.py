# Generated by Django 2.0.6 on 2019-09-17 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0009_team_images_person_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='team_group_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, default='', upload_to='teams/images/')),
                ('team_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.teams')),
            ],
        ),
    ]

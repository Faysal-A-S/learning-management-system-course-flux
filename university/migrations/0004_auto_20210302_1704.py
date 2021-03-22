# Generated by Django 3.1.6 on 2021-03-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_auto_20210227_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='notes',
            field=models.FileField(blank=True, default='default.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='video',
            field=models.FileField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]
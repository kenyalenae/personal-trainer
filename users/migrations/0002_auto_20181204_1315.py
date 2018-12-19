# Generated by Django 2.1.2 on 2018-12-04 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=18),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='height',
            field=models.IntegerField(default=60),
        ),
        migrations.AddField(
            model_name='profile',
            name='membership',
            field=models.CharField(choices=[('BAS', 'Basic'), ('PRO', 'Pro'), ('PRE', 'Premium')], default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='weight',
            field=models.IntegerField(default=70),
        ),
    ]
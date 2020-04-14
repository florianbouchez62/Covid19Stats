# Generated by Django 3.0.5 on 2020-04-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='active_cases',
            field=models.IntegerField(null=True, verbose_name='active_cases'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='critical_cases',
            field=models.IntegerField(null=True, verbose_name='critical_cases'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='new_cases',
            field=models.TextField(null=True, verbose_name='new_cases'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='new_deaths',
            field=models.TextField(null=True, verbose_name='new_deaths'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='recovered_cases',
            field=models.IntegerField(null=True, verbose_name='recovered_cases'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='total_cases',
            field=models.IntegerField(null=True, verbose_name='total_cases'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='total_deaths',
            field=models.IntegerField(null=True, verbose_name='total_deaths'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='total_tests',
            field=models.IntegerField(null=True, verbose_name='total_tests'),
        ),
    ]

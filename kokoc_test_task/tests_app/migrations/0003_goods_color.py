# Generated by Django 4.1.1 on 2022-09-26 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests_app', '0002_userspoints_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='color',
            field=models.CharField(default=0, max_length=50, verbose_name='Значение цвета'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.1.10 on 2019-07-21 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minutes', '0011_auto_20180825_1121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='minutesdocument',
            options={'base_manager_name': 'objects', 'permissions': (('show_minutesdocument', 'User/Group is allowed to view those minutes'),), 'verbose_name': 'Minutes', 'verbose_name_plural': 'Minutes'},
        ),
    ]
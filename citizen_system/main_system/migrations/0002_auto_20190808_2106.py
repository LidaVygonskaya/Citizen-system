# Generated by Django 2.2.4 on 2019-08-08 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='citizen',
            unique_together={('import_group', 'citizen_id')},
        ),
        migrations.DeleteModel(
            name='RelativesRelationship',
        ),
    ]

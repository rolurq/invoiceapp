# Generated by Django 2.1.14 on 2020-02-01 10:08

from django.db import migrations, models

def forwards(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    db_alias = schema_editor.connection.alias
    permissions = Permission.objects.using(db_alias).filter(
        models.Q(codename='view_client') | models.Q(codename='view_invoice') |
        models.Q(codename='view_product') |
        models.Q(codename='view_productinvoice') |
        models.Q(codename='view_user'))

    group = Group.objects.using(db_alias).create(name='public-staff')
    group.permissions.set(permissions)
    group.save()

def backwards(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    db_alias = schema_editor.connection.alias
    Group.objects.using(db_alias).filter(name='public-staff').delete()

class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200209_2213'),
        ('invoice', '0003_auto_20200201_0948')
    ]

    operations = [
        migrations.RunPython(forwards, backwards)
    ]

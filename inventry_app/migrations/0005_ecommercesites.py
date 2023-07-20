# Generated by Django 4.2.1 on 2023-06-01 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventry_app', '0004_alter_category_createdon_alter_category_modifiedon_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ecommerceSites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('createdBy', models.CharField(default='admin', max_length=100, null=True)),
                ('createdOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('modifiedBy', models.CharField(default='admin', max_length=100, null=True)),
                ('modifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('isActive', models.IntegerField(default=1)),
            ],
        ),
    ]

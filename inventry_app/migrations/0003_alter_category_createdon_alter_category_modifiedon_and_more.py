# Generated by Django 4.2.1 on 2023-05-29 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventry_app', '0002_category_remove_product1_other_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='createdOn',
            field=models.DateTimeField(default='2023-05-29 20:14:26.068', null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='modifiedOn',
            field=models.DateTimeField(default='2023-05-29 20:14:26.068', null=True),
        ),
        migrations.AlterField(
            model_name='image1',
            name='createdOn',
            field=models.DateTimeField(default='2023-05-29 20:14:26.068', null=True),
        ),
        migrations.AlterField(
            model_name='image1',
            name='modifiedOn',
            field=models.DateTimeField(default='2023-05-29 20:14:26.076', null=True),
        ),
        migrations.AlterField(
            model_name='product1',
            name='createdOn',
            field=models.DateTimeField(default='2023-05-29 20:14:26.068', null=True),
        ),
        migrations.AlterField(
            model_name='product1',
            name='modifiedOn',
            field=models.DateTimeField(default='2023-05-29 20:14:26.068', null=True),
        ),
    ]

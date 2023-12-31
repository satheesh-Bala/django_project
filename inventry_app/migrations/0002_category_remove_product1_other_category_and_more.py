# Generated by Django 4.2.1 on 2023-05-29 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventry_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('createdBy', models.CharField(default='admin', max_length=100, null=True)),
                ('createdOn', models.DateTimeField(default='2023-05-29 19:09:30.552', null=True)),
                ('modifiedBy', models.CharField(default='admin', max_length=100, null=True)),
                ('modifiedOn', models.DateTimeField(default='2023-05-29 19:09:30.552', null=True)),
                ('isActive', models.IntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='product1',
            name='other_category',
        ),
        migrations.AddField(
            model_name='image1',
            name='createdBy',
            field=models.CharField(default='admin', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='image1',
            name='createdOn',
            field=models.DateTimeField(default='2023-05-29 19:09:30.552', null=True),
        ),
        migrations.AddField(
            model_name='image1',
            name='isActive',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='image1',
            name='modifiedBy',
            field=models.CharField(default='admin', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='image1',
            name='modifiedOn',
            field=models.DateTimeField(default='2023-05-29 19:09:30.552', null=True),
        ),
        migrations.AddField(
            model_name='product1',
            name='createdBy',
            field=models.CharField(default='admin', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product1',
            name='createdOn',
            field=models.DateTimeField(default='2023-05-29 19:09:30.552', null=True),
        ),
        migrations.AddField(
            model_name='product1',
            name='isActive',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product1',
            name='modifiedBy',
            field=models.CharField(default='admin', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product1',
            name='modifiedOn',
            field=models.DateTimeField(default='2023-05-29 19:09:30.552', null=True),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventry_app.category'),
        ),
    ]

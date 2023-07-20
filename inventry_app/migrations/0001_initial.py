# Generated by Django 4.2.1 on 2023-05-28 14:54

from django.db import migrations, models
import django.db.models.deletion
import inventry_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('other_category', models.CharField(blank=True, max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('vendor', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Image1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=inventry_app.models.get_upload_path)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='inventry_app.product1')),
            ],
        ),
    ]

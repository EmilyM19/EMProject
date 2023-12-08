# Generated by Django 5.0 on 2023-12-08 01:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catentry', '0009_alter_cat_adoption_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='previous_status',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='cat',
            name='cat_surgery_status',
            field=models.CharField(choices=[('Spayed', 'Spayed'), ('Neutered', 'Neutered'), ('Unknown Surgery Status', 'Unknown Surgery Status'), ('Needs Surgery', 'Needs Surgery')], default='Unknown Surgery Status', max_length=25),
        ),
        migrations.CreateModel(
            name='Adopter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adopter_name', models.CharField(max_length=50)),
                ('adopter_phone', models.CharField(max_length=15)),
                ('adopter_street_address', models.TextField(max_length=50)),
                ('adopter_city', models.TextField(max_length=50)),
                ('adopter_state', models.TextField(max_length=2)),
                ('adopter_zip', models.TextField(max_length=10)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catentry.cat')),
            ],
        ),
    ]
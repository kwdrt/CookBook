# Generated by Django 3.0.5 on 2021-05-26 17:36

import RestApi.models
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('RestApi', '0005_delete_dish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=40)),
                ('types', djongo.models.fields.ArrayField(model_container=RestApi.models.TextElement, model_form_class=RestApi.models.TextForm)),
                ('recipeID', models.IntegerField()),
                ('img', models.CharField(max_length=100)),
                ('reviews', djongo.models.fields.ArrayReferenceField(on_delete=django.db.models.deletion.CASCADE, to='RestApi.Review')),
            ],
        ),
    ]

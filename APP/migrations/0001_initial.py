# Generated by Django 4.0.4 on 2022-05-17 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=274)),
                ('email', models.EmailField(max_length=254)),
                ('Occputation', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=255, null=True)),
            ],
        ),
    ]

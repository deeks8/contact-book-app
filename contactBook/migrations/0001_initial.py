# Generated by Django 2.1.4 on 2018-12-09 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('ContactId', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('EmailId', models.CharField(max_length=100, unique=True)),
                ('PhoneNumber', models.CharField(blank=True, max_length=13, null=True)),
            ],
        ),
    ]
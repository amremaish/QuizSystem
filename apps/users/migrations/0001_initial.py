# Generated by Django 4.0.2 on 2023-05-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(db_index=True, max_length=128, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

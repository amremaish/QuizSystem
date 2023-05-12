# Generated by Django 4.0.2 on 2023-05-12 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('choice_1', models.TextField()),
                ('choice_2', models.TextField()),
                ('choice_3', models.TextField()),
                ('choice_4', models.TextField()),
                ('answer_number', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='category.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

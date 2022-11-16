# Generated by Django 4.1.3 on 2022-11-16 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('AuthorName', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('AuthorBio', models.TextField()),
                ('Publisher', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('Isbn', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=100)),
                ('Genre', models.CharField(max_length=50)),
                ('PublishedDate', models.CharField(max_length=4)),
                ('Publisher', models.CharField(max_length=100)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('CopiesSold', models.IntegerField()),
                ('AvgRating', models.IntegerField()),
                ('Description', models.TextField()),
                ('AuthorName', models.ForeignKey(db_column='AuthorName', on_delete=django.db.models.deletion.CASCADE, to='bookdetail.authors')),
            ],
            options={
                'ordering': ['Isbn'],
            },
        ),
    ]
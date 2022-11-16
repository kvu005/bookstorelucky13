# Generated by Django 4.1.3 on 2022-11-16 02:47

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AuthorName', models.CharField(max_length=50)),
                ('AuthorBio', models.TextField()),
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
                ('AuthorName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratingscomments.authors')),
            ],
            options={
                'ordering': ['Isbn'],
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('UserId', models.IntegerField(primary_key=True, serialize=False)),
                ('UserName', models.TextField()),
                ('Password', models.TextField()),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('HomeAddress', models.TextField()),
            ],
            options={
                'ordering': ['UserId'],
            },
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('RatingId', models.AutoField(primary_key=True, serialize=False)),
                ('Rating', models.IntegerField()),
                ('DateStamp', models.DateField()),
                ('Isbn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratingscomments.books')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratingscomments.users')),
            ],
            options={
                'ordering': ['Rating'],
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('CommentId', models.AutoField(primary_key=True, serialize=False)),
                ('Comments', models.CharField(max_length=100)),
                ('DateStamp', models.DateField()),
                ('Isbn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratingscomments.books')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratingscomments.users')),
            ],
            options={
                'ordering': ['CommentId'],
            },
        ),
    ]

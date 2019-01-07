# Generated by Django 2.1.4 on 2019-01-07 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=7000)),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_enterprise.Answers')),
            ],
        ),
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_enterprise.Answers')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('body', models.CharField(max_length=7000)),
                ('tags', models.CharField(max_length=200)),
                ('is_answered', models.BooleanField(default=False)),
                ('has_correct_answer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Upvotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_count', models.IntegerField()),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_enterprise.Answers')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_enterprise.Questions')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=50)),
                ('reputation', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='upvotes',
            name='upvoter_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='stack_enterprise.User'),
        ),
        migrations.AddField(
            model_name='upvotes',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='stack_enterprise.User'),
        ),
        migrations.AddField(
            model_name='questions',
            name='owner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_enterprise.User'),
        ),
        migrations.AddField(
            model_name='favourites',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_enterprise.Questions'),
        ),
        migrations.AddField(
            model_name='favourites',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_enterprise.User'),
        ),
        migrations.AddField(
            model_name='comments',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_enterprise.Questions'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_enterprise.User'),
        ),
        migrations.AddField(
            model_name='answers',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_enterprise.Questions'),
        ),
        migrations.AddField(
            model_name='answers',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_enterprise.User'),
        ),
    ]

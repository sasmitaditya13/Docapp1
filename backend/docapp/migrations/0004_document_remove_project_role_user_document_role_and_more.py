# Generated by Django 4.2.5 on 2023-09-25 20:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('docapp', '0003_project_role_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('docid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('docname', models.CharField(max_length=30)),
                ('delta', models.TextField()),
                ('text', models.TextField()),
                ('project1', models.ManyToManyField(to='docapp.project')),
            ],
        ),
        migrations.RemoveField(
            model_name='project_role',
            name='user',
        ),
        migrations.CreateModel(
            name='Document_role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docrole', models.CharField(choices=[('O', 'Owner'), ('A', 'Admin'), ('K', 'Add docs'), ('E', 'Edit docs'), ('C', 'Comment'), ('R', 'Read')], default='R', max_length=1)),
                ('document', models.ManyToManyField(to='docapp.document')),
                ('user1', models.ManyToManyField(to='docapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='project_role',
            name='user',
            field=models.ManyToManyField(to='docapp.user'),
        ),
    ]
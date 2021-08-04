# Generated by Django 3.2.6 on 2021-08-04 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requesttype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('New_sset', models.CharField(max_length=50)),
                ('repair', models.CharField(max_length=50)),
                ('replacement', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='asset',
            name='category',
        ),
        migrations.AddField(
            model_name='department',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='department',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='asset',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='employeeassetrequest',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.requesttype'),
        ),
    ]

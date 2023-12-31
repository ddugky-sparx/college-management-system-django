# Generated by Django 4.2.7 on 2023-12-15 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0004_designation_is_active'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.designation'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='qualification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.qualification'),
        ),
    ]

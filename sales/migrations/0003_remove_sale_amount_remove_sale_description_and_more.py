# Generated by Django 4.2.14 on 2024-08-08 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='description',
        ),
        migrations.AddField(
            model_name='sale',
            name='cash_in',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='sale',
            name='cash_out',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='sale',
            name='closing_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='sale',
            name='till_in',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='sale',
            name='till_out',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateField(),
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
    ]

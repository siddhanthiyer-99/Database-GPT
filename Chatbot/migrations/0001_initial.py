# Generated by Django 4.2.3 on 2024-02-13 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='po_line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ponr', models.IntegerField()),
                ('prodnr', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('prodnr', models.IntegerField(primary_key=True, serialize=False)),
                ('prodname', models.TextField()),
                ('prodtype', models.TextField()),
                ('available_quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='purchase_order',
            fields=[
                ('ponr', models.IntegerField(primary_key=True, serialize=False)),
                ('podate', models.DateField()),
                ('supnr', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='supplier',
            fields=[
                ('supnr', models.IntegerField(primary_key=True, serialize=False)),
                ('supname', models.TextField(max_length=255)),
                ('supaddress', models.TextField(max_length=255)),
                ('supcity', models.TextField(max_length=255)),
                ('supstatus', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='supplies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supnr', models.IntegerField()),
                ('prodnr', models.IntegerField()),
                ('purchase_price', models.FloatField()),
                ('deliv_period', models.TextField(max_length=255)),
            ],
        ),
    ]
# Generated by Django 3.1.4 on 2021-01-08 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ANNOUNCED_PU_RESULTS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polling_unit_uniqueid', models.CharField(blank=True, max_length=200)),
                ('party_score', models.CharField(blank=True, max_length=200)),
                ('entered_by_user', models.CharField(blank=True, max_length=200)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('user_ip_address', models.CharField(blank=True, max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LGA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lga_id', models.CharField(blank=True, max_length=200, unique=True)),
                ('lga_name', models.CharField(blank=True, max_length=200, unique=True)),
                ('lga_description', models.TextField(blank=True)),
                ('entered_by_user', models.CharField(blank=True, max_length=200)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('user_ip_address', models.CharField(blank=True, max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PARTY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(blank=True, max_length=200, unique=True)),
                ('party_abbreviation', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='STATES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.CharField(blank=True, max_length=5)),
                ('state_name', models.CharField(blank=True, choices=[(1, 'Abuja'), (2, 'Abia'), (3, 'Anambra'), (4, 'Akwa Ibom'), (5, 'Adamawa'), (6, 'Bauchi'), (7, 'Bayelsa'), (8, 'Benue'), (9, 'Borno'), (10, 'Cross River'), (12, 'Ebonyi'), (13, 'Edo'), (14, 'Ekiti'), (15, 'Enugu'), (16, 'Gombe'), (17, 'Imo'), (18, 'Jigawa'), (19, 'Kaduna'), (20, 'Kano'), (21, 'Katsina'), (22, 'Kebbi'), (23, 'Kogi'), (24, 'Kwara'), (25, 'Delta'), (26, 'Nasarawa'), (27, 'Niger'), (28, 'Ogun'), (29, 'Ondo'), (30, 'Osun'), (31, 'Oyo'), (32, 'Plateau'), (33, 'Rivers'), (34, 'Sokoto'), (35, 'Taraba'), (36, 'Yobe'), (37, 'Zamfara'), (251, 'Lagos')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WARD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_id', models.CharField(blank=True, max_length=200)),
                ('ward_name', models.CharField(blank=True, max_length=200)),
                ('entered_by_user', models.CharField(blank=True, max_length=200)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('user_ip_address', models.CharField(blank=True, max_length=200)),
                ('lga_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ward_lga_id', to='polls.lga')),
            ],
        ),
        migrations.CreateModel(
            name='POLLING_UNIT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_unit_id', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('uniqueward_id', models.DecimalField(decimal_places=2, max_digits=12)),
                ('polling_unit_number', models.CharField(blank=True, max_length=200)),
                ('polling_unit_name', models.CharField(blank=True, max_length=200)),
                ('polling_unit_description', models.TextField(blank=True)),
                ('lat_poll', models.CharField(blank=True, max_length=200)),
                ('long_poll', models.CharField(blank=True, max_length=200)),
                ('entered_by_user', models.CharField(blank=True, max_length=200)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('user_ip_address', models.CharField(blank=True, max_length=200, unique=True)),
                ('lga_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pu_lga_id', to='polls.lga')),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pu_state_id', to='polls.states')),
                ('unique_id', models.ForeignKey(blank=True, default='pu', on_delete=django.db.models.deletion.CASCADE, related_name='announced_polling_unit_uniqueid', to='polls.announced_pu_results')),
                ('ward_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pu_ward_id', to='polls.ward')),
            ],
        ),
        migrations.AddField(
            model_name='lga',
            name='state_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lga_state_id', to='polls.states'),
        ),
        migrations.CreateModel(
            name='ANNOUNCED_WARD_RESULTS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_name', models.CharField(blank=True, max_length=200)),
                ('party_score', models.CharField(blank=True, max_length=200)),
                ('entered_by_user', models.CharField(blank=True, max_length=200)),
                ('date_entered', models.CharField(blank=True, max_length=200)),
                ('user_ip_address', models.CharField(blank=True, max_length=200, unique=True)),
                ('party', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ward_results', to='polls.party')),
            ],
        ),
        migrations.CreateModel(
            name='ANNOUNCED_STATE_RESULTS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(blank=True, max_length=200)),
                ('party_score', models.CharField(blank=True, max_length=200)),
                ('entered_by_user', models.CharField(blank=True, max_length=200)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('user_ip_address', models.CharField(blank=True, max_length=200, unique=True)),
                ('party', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='state_results', to='polls.party')),
            ],
        ),
        migrations.AddField(
            model_name='announced_pu_results',
            name='party',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='pu_results', to='polls.party'),
        ),
        migrations.CreateModel(
            name='ANNOUNCED_LGA_RESULTS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_score', models.CharField(blank=True, max_length=200)),
                ('entered_by_user', models.CharField(blank=True, max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user_ip_address', models.CharField(blank=True, max_length=200, unique=True)),
                ('lga_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announced_lga_name', to='polls.lga')),
                ('party', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='party', to='polls.party')),
            ],
        ),
        migrations.CreateModel(
            name='AGENT_NAME',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200)),
                ('last_name', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('poll_unit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='polling_unit', to='polls.polling_unit')),
            ],
        ),
    ]

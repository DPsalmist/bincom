# Generated by Django 3.1.4 on 2021-01-08 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_states_state_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='states',
            name='state_name',
            field=models.CharField(blank=True, choices=[('1', 'Abuja'), ('2', 'Abia'), ('3', 'Anambra'), ('4', 'Akwa Ibom'), ('5', 'Adamawa'), ('6', 'Bauchi'), ('7', 'Bayelsa'), ('8', 'Benue'), ('9', 'Borno'), ('10', 'Cross River'), ('12', 'Ebonyi'), ('13', 'Edo'), ('14', 'Ekiti'), ('15', 'Enugu'), ('16', 'Gombe'), ('17', 'Imo'), ('18', 'Jigawa'), ('19', 'Kaduna'), ('20', 'Kano'), ('21', 'Katsina'), ('22', 'Kebbi'), ('23', 'Kogi'), ('24', 'Kwara'), ('25', 'Delta'), ('26', 'Nasarawa'), ('27', 'Niger'), ('28', 'Ogun'), ('29', 'Ondo'), ('30', 'Osun'), ('31', 'Oyo'), ('32', 'Plateau'), ('33', 'Rivers'), ('34', 'Sokoto'), ('35', 'Taraba'), ('36', 'Yobe'), ('37', 'Zamfara'), ('251', 'Lagos')], max_length=200),
        ),
    ]
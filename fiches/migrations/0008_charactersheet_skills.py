# Generated by Django 4.0.3 on 2022-04-30 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competences', '0011_remove_skill_level_remove_skillsheet_i_and_more'),
        ('fiches', '0007_remove_charactersheet_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='charactersheet',
            name='skills',
            field=models.ManyToManyField(blank=True, through='competences.SkillSheet', to='competences.skill'),
        ),
    ]

from django.db import models


class SkillDetail(models.Model):
    skill = models.CharField(max_length=50)
    percentage = models.CharField(max_length=5)

    def __str__(self):
        return self.skill+" "+self.percentage


class AdditionalSkills(models.Model):
    skill = models.CharField(max_length=50)

    def __str__(self):
        return self.skill

from django.db import models


class SkillDetail(models.Model):
    skill = models.CharField(max_length=50)
    percentage = models.CharField(max_length=5)

    def __str__(self):
        return self.skill+", "+self.percentage


class AdditionalSkills(models.Model):
    skill = models.CharField(max_length=50)

    def __str__(self):
        return self.skill


class Experience(models.Model):
    companyName = models.CharField(max_length=50)
    companyLocation = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    durationFrom = models.CharField(max_length=50)
    durationTo = models.CharField(max_length=50)

    def __str__(self):
        return self.companyName+", "+self.companyLocation+", "+self.position+", "+self.durationFrom+", "+self.durationTo


class WorkDetails(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    category = models.CharField(max_length=10)
    image = models.CharField(max_length=50)
    github = models.CharField(max_length=50)
    livesite = models.CharField(max_length=50)

    def __str__(self):
        return self.name+", "+self.category

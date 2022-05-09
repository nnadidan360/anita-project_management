from django.db import models
from student.models import Assign, Project

# Create your models here.


class checkStat(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    chosen_preference = models.ForeignKey(Assign, on_delete=models.CASCADE)

    

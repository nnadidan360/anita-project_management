from django.db import models
from django.contrib.auth.models import User


# Create your models here.


status = (
    ('1', 'Pending'),
    ('2', 'Approved'),
)


class Project(models.Model):
    name = models.CharField(max_length=80)
    mat_no = models.CharField(max_length=80)
    status = models.CharField(max_length=7, choices=status, default=1)
    topic_1 = models.TextField(max_length=300, unique=True)
    topic_2 = models.TextField(max_length=300, unique=True)
    topic_3 = models.TextField(max_length=300, unique=True)


    add_date = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['name', 'mat_no']

    def __str__(self):
        return (self.name)

topics = (
    ('1', 'topic  1'),
    ('2', 'topic 2'),
    ('3', 'topic 3'),
)

class Assign(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    chosen_topic = models.CharField(max_length=7, choices=topics, default=None)
    supervisor = models.OneToOneField(User, on_delete=models.CASCADE)


    class Meta:
        ordering = ['project']


from django.db import models

# Create your models here.

class Job(models.Model):
    JobId = models.IntegerField(primary_key=True)


class Society(models.Model):
    SocietyId = models.IntegerField(primary_key=True)



class User(models.Model):
    UserId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    jobId = models.OneToOneField(
        Job,
        on_delete=models.CASCADE
    )
    societyId = models.ForeignKey(
        Society,
        on_delete=models.CASCADE
    )


class Group(models.Model):
    GroupeId = models.IntegerField(primary_key=True)
    user = models.ManyToManyField(User) 



CHOICE_LIST = [
    ('python', 'Python'),
    ('java', 'Java')
]

class Person(models.Model):

    class Meta:
        permissions = [('can_change_category', 'Can change category')]
        
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    semestre = models.CharField(
        max_length=20,
        choices=CHOICE_LIST
    )


"""
    showmigrations
    migrate migrate_name
    class.objects.filter(criteria)
"""
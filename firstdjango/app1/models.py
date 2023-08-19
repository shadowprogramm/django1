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


"""
    showmigrations
    migrate migrate_name
    class.objects.filter(criteria)
"""
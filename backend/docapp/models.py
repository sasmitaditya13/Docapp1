from django.db import models
import uuid

# Create your models here.

class User(models.Model):
    uid  = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    uname = models.CharField(max_length=30)
    uemail = models.CharField(max_length=30)

class Project(models.Model):
    pid = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    pname = models.CharField(max_length=30)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

class Project_role(models.Model):
    user = models.ManyToManyField(User)
    project = models.ManyToManyField(Project)
    rolesidentify = (("O" , "Owner"),("A" , "Admin"),("K" , "Add docs"),("E","Edit docs"),("C" , "Comment"),("R","Read"))
    role = models.CharField(
        max_length = 1,
        choices = rolesidentify,
        default= 'R'
        )

class Document(models.Model):
    docid = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    docname = models.CharField(max_length=30)
    project1 = models.ManyToManyField(Project)
    delta = models.TextField()
    text = models.TextField()

class Document_role(models.Model):
    user1 = models.ManyToManyField(User)
    document = models.ManyToManyField(Document)
    rolesidentify = (("O" , "Owner"),("A" , "Admin"),("K" , "Add docs"),("E","Edit docs"),("C" , "Comment"),("R","Read"))
    docrole = models.CharField(
        max_length = 1,
        choices = rolesidentify,
        default= 'R'
        )
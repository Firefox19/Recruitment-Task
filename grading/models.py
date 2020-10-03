from django.db import models


class Recruiter(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Candidate(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Task(models.Model):
    title = models.TextField(unique=True)

    def __str__(self):
        return self.title


class Grade(models.Model):
    value = models.IntegerField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.value) + ' - ' + str(self.task) + ' - ' + str(self.candidate)

from django.db import models


class Room(models.Model):
    roomCode = models.CharField(max_length=20, default="")
    contestantsCount = models.IntegerField(default=0)
    # JSON string representing list of budget submissions
    submissions = models.TextField(max_length=10000, default="")
    # 0 - not started, #1 - waiting for submissions, #2 - waiting for reviews
    state = models.IntegerField(default=0)


class User(models.Model):
    score = models.IntegerField(default=0)
    name = models.CharField(max_length=255, default="")
    rank = models.IntegerField(default=0)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class BudgetSubmission(models.Model):
    title = models.CharField(max_length=255, default="")
    budgetPlan = models.TextField(default="")
    BudgetCateg = models.CharField(max_length=255, default="")
    yesVotes = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

from django.db import models

class Score(models.Model):
    user = models.CharField(max_length=60)
    points = models.IntegerField()
    level = models.IntegerField()
    def __str__(self):
        return self.user + " - " + str(self.level) + " - " + str(self.points)

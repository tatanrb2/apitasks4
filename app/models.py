from django.db import models


class State(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField(blank=True, null=True)   # It's not necessary
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)    # Auto created and not editable

    def __str__(self):
        return f"{self.title} - {self.state}"

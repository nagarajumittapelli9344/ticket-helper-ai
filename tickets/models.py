from django.db import models

class Ticket(models.Model):
    TITLE_MAX_LEN = 200

    title = models.CharField(max_length=TITLE_MAX_LEN)
    description = models.TextField()
    category = models.CharField(max_length=50, blank=True)
    priority = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

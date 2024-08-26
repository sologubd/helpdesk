from django.db import models


class Status(models.TextChoices):
    IN_PROGRESS = "IN_PROGRESS", "In Progress"
    RESOLVED = "RESOLVED", "Resolved"
    POSTPONED = "POSTPONED", "Postponed"


class Ticket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(
        "teams.Team", on_delete=models.CASCADE, related_name="assigned_tickets"
    )
    status = models.CharField(
        choices=Status.choices, default=Status.IN_PROGRESS, max_length=25
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

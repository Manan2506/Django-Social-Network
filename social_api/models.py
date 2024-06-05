
from django.db import models
from django.conf import settings


class FriendRequest(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_requests', on_delete=models.CASCADE)
    status = models.CharField(max_length=10,
                              choices=(('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"FriendRequest from {self.sender} to {self.receiver}"

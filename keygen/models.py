from django.db import models


class Account(models.Model):
    email = models.EmailField(blank=False, null=False)

    def __str__(self):
        return self.email


class Key(models.Model):
    STATE = (
        (0, 'Inactive'),
        (1, 'Active'))
    hash_key = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    state = models.IntegerField(default=0, choices=STATE)
    account = models.ForeignKey(Account, null=False, blank=False,
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.hash_key



from django.db import models


class Account(models.Model):
    email = models.EmailField(blank=False, null=False)

    def __str__(self):
        return self.email


class UnDeletedKeyManager(models.Manager):
    # key manager to return keys not deleted

    def get_queryset(self):
        """ Returns queryset of keys not deleted"""
        return super(UnDeletedKeyManager, self).get_queryset().filter(deleted__exact=False)


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
    objects = UnDeletedKeyManager()

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.hash_key




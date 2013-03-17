import time
from django.db import models


class KeyableModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def cache_key(self):
        """
            Instance method to return the full cache key
        """
        return "%s-%s-%s" % (self.__class__.__name__,
                             str(self.pk),
                             str(int(time.mktime(self.updated_at.timetuple()))),
                            )
    class Meta:
        abstract = True
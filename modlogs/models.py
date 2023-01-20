from django.db import models


class ModLog(models.Model):
    unique_id = models.CharField(max_length=120, default="None")
    sub_name = models.CharField(max_length=25)
    sub_user = models.CharField(max_length=25, default="Not Specified")
    mod_name = models.CharField(max_length=25)
    mod_action = models.CharField(max_length=20)
    mod_link = models.URLField()
    mod_time = models.TextField()
    mod_item = models.TextField(null=True)

    def __str__(self):
        return self.unique_id

from django.db import models
from django.utils.translation import gettext_lazy as _


class EmailStatus(models.IntegerChoices):
    PENDING = 1, _("Pending")
    SENT = 2, _("Sent")
    FAILED = 3, _("Failed")

from django.db import models


class DeviceStatus(models.TextChoices):
    ACTIVE = "active"
    INACTIVE = "inactive"
    ONLINE = "online"
    OFFLINE = "offline"


class ObserverStatus(models.TextChoices):
    ACTIVE = "active"
    INACTIVE = "inactive"
    ONLINE = "online"
    OFFLINE = "offline"

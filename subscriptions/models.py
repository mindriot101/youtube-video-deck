from django.db import models
from django.contrib.auth.models import User


class Subscription(models.Model):
    """
    Represents a single subscription for a user

    *Responsibilities*

    * links the subscription ID to a series of videos
    * tracks the last time the subscription was checked for new items
    * stores whether the subscription is a channel or playlist
    """

    user = models.ForeignKey(
        User, related_name="subscriptions", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    youtube_id = models.CharField(max_length=255)
    type = models.CharField(max_length=31)
    last_checked = models.DateTimeField(null=True)

    class Meta:
        # Add a compound unique key on user and youtube id
        unique_together = ("user", "youtube_id")

    def unwatched(self):
        return self.videos.filter(watched=False).order_by("-published_at")

    def __str__(self):
        return self.name


class Video(models.Model):
    """
    Represents a single video, belonging to a subscription

    *Responsibilities*

    * track whether the user has watched the video
    * store the thumbnail
    * store the full url to video
    """

    name = models.CharField(max_length=255)
    thumbnail_url = models.CharField(max_length=255)
    description = models.TextField()
    youtube_id = models.CharField(max_length=255, unique=True)
    subscription = models.ForeignKey(
        Subscription, related_name="videos", on_delete=models.CASCADE
    )
    published_at = models.DateTimeField()
    watched = models.BooleanField(default=False)
    duration = models.TimeField(null=True)

    @property
    def url(self):
        """
        Helper to create the full youtube link from the video id
        """
        return "https://www.youtube.com/watch?v={}".format(self.youtube_id)

    def hover_text(self):
        """
        The text to show when the user hovers over the item in the UI
        """
        if self.description:
            return "{self.name}\n\n{self.description}".format(self=self)
        else:
            return self.name

    def __str__(self):
        return f"{self.youtube_id} from {self.subscription}"

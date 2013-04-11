from django.db import models
from django.utils import timezone
import datetime

class LinkGroup(models.Model):
    """A group of links
    """
    title = models.CharField( max_length = 120 )
    created_date = models.DateTimeField()
    
    def __unicode__(self):
        return self.title
    
    def is_recent(self):
        return timezone.now() - self.created_date < datetime.timedelta(days=1)

    
    is_recent.admin_order_field = 'created_date'
    is_recent.boolean = True
    is_recent.short_description = 'created recently?'
    
    
class Link(models.Model):
    """A favorite link
    """
    title = models.CharField( max_length = 250 )
    group = models.ForeignKey(LinkGroup)
    url = models.URLField()
    visited = models.BooleanField()
    
    def __unicode__(self):
        return self.title

from django.db import models

class LinkGroup(models.Model):
    """A group of links
    """
    title = models.CharField( max_length = 120 )
    
    def __unicode__(self):
        return self.title
    

class Link(models.Model):
    """A favorite link
    """
    title = models.CharField( max_length = 250 )
    group = models.ForeignKey(LinkGroup)
    url = models.URLField()
    visited = models.BooleanField()
    
    def __unicode__(self):
        return self.title

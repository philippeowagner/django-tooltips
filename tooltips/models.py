from django.db import models

class Tooltip(models.Model):
    """ """
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=255, db_index=True)
    selector = models.CharField(max_length=50, default='', blank=False, null=False, help_text='div:contains("example")')
    title = models.CharField(max_length=255)
    core_body = models.TextField(null=True, blank=True)
    context_body = models.TextField(null=True, blank=True)
    
    def body(self):
        if self.context_body:
            return context_body
        return self.core_body
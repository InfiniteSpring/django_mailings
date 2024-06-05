from django.db import models

class Case(models.Model):
    
    class Meta:
        db_table="case"

    """Case on site -- materials on this case"""
    name = models.CharField("Case name", max_length=255)
    

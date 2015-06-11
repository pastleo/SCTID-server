from django.db import models

class Sctid(models.Model): # Student Card to Id
    card_id = models.CharField(max_length=10,unique=True)
    student_id = models.CharField(max_length=10)

    def __str__(self):
        return "%s <==> %s" % (self.card_id,self.student_id)

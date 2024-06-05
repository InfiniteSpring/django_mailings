from django.db import models


class CommonMailingList(models.Model):

    class Meta:
        db_table="common_mailing_list"

    email = models.EmailField("Subscriber email")


class CaseMailingList(models.Model):

    class Meta:
        db_table="case_mailing_list"

    email = models.EmailField("Subscriber email")
    case = models.ForeignKey(
        to='cases.Case',
        verbose_name="Case",
        on_delete=models.CASCADE
    )
    

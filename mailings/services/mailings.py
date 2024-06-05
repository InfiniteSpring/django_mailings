from .mailchimp_services import add_mailhimp_email_with_tag
from mailings.models import CommonMailingList, CaseMailingList
from cases.models import Case


def add_email_to_common_mailchimp_list(email: str):
    """Add email to common list"""
    add_mailhimp_email_with_tag(
        audience_name='COMMON', 
        email=email,
        tag="COMMON TAG"
    )
    CommonMailingList.objects.get_or_create(email=email)


def add_email_to_case_mailchimp_list(email: str, case_id: int|str):
    """Add email to case list"""
    case = Case.objects.get(pk=case_id)
    case_tag = f"Case {case.name}" 

    add_mailhimp_email_with_tag(
        audience_name="CASE", 
        email=email,
        tag=case_tag
    )

    CaseMailingList.objects.get_or_create(email=email, case=case)
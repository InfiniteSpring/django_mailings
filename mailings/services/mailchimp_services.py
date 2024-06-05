from mailchimp3 import MailChimp
from django.conf import settings


def add_mailhimp_email_with_tag(
    audience_name: str, 
    email: str, 
    tag:str
) -> None:
    """Add email in audience with audience_id"""
    _add_email_to_mailchimp_audience(
        audience_id=settings.MAILCHIMP_AUDIENCES.get(audience_name), 
        email=email
    )
    _add_mailchimp_tag(
        audience_name=settings.MAILCHIMP_AUDIENCES.get(audience_name),
        sub_hash=_get_subscriber_hash(email=email),
        tag=tag
    )


def _get_mc_client() -> MailChimp:
    """Returns api for interaction with Mailchimp"""
    return MailChimp(
        mc_api=settings.MAILCHIMP_API_KEY , 
        mc_user=settings.MAILCHIMP_USERNAME
    )

def _add_email_to_mailchimp_audience(
        audience_id: str,
        email: str
) -> None:
    """Add email to mailchimp audience by audience_id"""
    _get_mc_client().lists.members.create(audience_id, {
        'email_address': email,
        'status': 'subscribed',
    })


def _get_subscriber_hash(email: str) -> str | None:
    """Return email id in mailchimp or None if email not found"""
    members = _get_mc_client.search_members.get(
        query=email,
        fields='exact_matches.members.id'
    ).get('exact_matches').get('memberes')
    
    if not members:
        return None
    
    return members[0].get('id')


def _add_mailchimp_tag(audience_id: str, sub_hash: str, tag: str) -> None:
    """Add tag for email with subscriber hash in audience_id"""
    _get_mc_client().lists.members.tags.update(
        list_id=audience_id, 
        subscriber_hash=sub_hash, 
        data={
            'tags': [{
                'name': tag,
                'status': 'active'
            }]
        }
    )

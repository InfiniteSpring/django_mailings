from mailings.services.mailchimp_services import add_mailhimp_email_with_tag

def webhook(request):
    """Handle webhook from paiment system"""
    add_mailhimp_email_with_tag(
        email=request.POST.get('email'),
        audience_name='DONATES',
        tag='DONATE'
    )


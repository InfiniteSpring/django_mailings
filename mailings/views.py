from django.http import JsonResponse

from .services.mailings import add_email_to_common_mailchimp_list, add_email_to_case_mailchimp_list


def add_to_common_list_view(request):
    """Add email to mailing common list"""
    
    email = request.GET.get("email")
    if not email:
        return JsonResponse({
            "success": False, 
            "message": "Email fiels is empty"
        })

    add_email_to_common_mailchimp_list(email=email)

    return JsonResponse({"success": True})


def add_to_case_list_view(request):
    """Add email to mailing case list"""
    
    email = request.GET.get("email")
    if not email:
        return JsonResponse({
            "success": False, 
            "message": "Email field is empty"
        })
    
    case_id = request.GET.get("case_id")
    if not case_id:
        return JsonResponse({
            "success": False, 
            "message": "Case_id field is empty"
        })

    add_email_to_case_mailchimp_list(email=email, case_id=case_id)

    return JsonResponse({"success": True})

from django.db.models import F
from .models import SiteAccessCounter

class SiteAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
      
        SiteAccessCounter.objects.update_or_create(defaults={'count': F('count') + 1}, id=1)
        
        response = self.get_response(request)
        return response
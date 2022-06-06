from .models import SiteVisit


class VisitsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if not SiteVisit.objects.filter(ip=request.META['REMOTE_ADDR']).exists():
            visit = SiteVisit(ip=request.META['REMOTE_ADDR'])
            visit.save()
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

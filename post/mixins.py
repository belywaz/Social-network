from django.core.exceptions import PermissionDenied



class PostIsOwnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.creater != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
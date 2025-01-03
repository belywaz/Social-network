from django.core.exceptions import PermissionDenied



class UserIsOwnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        print("instance -", instance)
        print("request.user -", request.user)
        if instance.id == self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
from rest_framework import  authentication
from rest_framework import exceptions
from rest_framework.authtoken.models import Token


class AccessKeyAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        if request.method == "POST":
            accesss_key = request.POST.get('access_key', None)
        elif request.method == "GET":
            accesss_key = request.GET.get('access_key', None)
        if not accesss_key:
            raise exceptions.NotFound("access_key not found ")
        try:
            access = Token.objects.get(key=accesss_key)
        except Token.DoesNotExist:
            raise exceptions.PermissionDenied(" No User with access_key found")
        except ValueError:
            raise exceptions.ValidationError("Badly formed hexadecimal UUID string")
        return access.user, None

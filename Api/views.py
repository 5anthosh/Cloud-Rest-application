from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Channel
from .models import Field
from .serializer import FieldSerializer
from django.http import HttpResponse
from .models import FieldHistory
from .serializer import HistorySerializer
from .authentication import AccessKeyAuthentication


@api_view(['GET'])
@authentication_classes((AccessKeyAuthentication, ))
def field_list(request, channel, format=None):
    if request.method == 'GET':
        try:
            access_key = request.GET['access_key']
            user = Token.objects.get(key=access_key)
            channel_id = Channel.objects.get(channel_name=channel, user=user.user)
        except Channel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        fields = Field.objects.filter(channel=channel_id)
        serializer = FieldSerializer(fields, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes((AccessKeyAuthentication, ))
def field_get(request, channel, field, format=None, ):
    if request.method == 'GET':
        try:
            access_key = request.GET['access_key']
            user = Token.objects.get(key=access_key)
            channel_id = Channel.objects.get(channel_name=channel, user=user.user)
        except Channel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            field = Field.objects.get(channel=channel_id, field_name=field)
        except Field.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FieldSerializer(field)
        return Response(serializer.data)


@api_view(['POST', 'GET'])
@authentication_classes((AccessKeyAuthentication, ))
def update(request):
    print(request.method)
    if request.method == "POST" :
        channel = request.POST['channel']
        field = request.POST['field']
        data = request.POST['data']
        access_key = request.POST['access_key']
    elif request.method == "GET":
        channel = request.GET['channel']
        field = request.GET['field']
        data = request.GET['data']
        access_key = request.GET['access_key']
    try:
        user = Token.objects.get(key=access_key)
        channel_id = Channel.objects.get(channel_name=channel, user=user.user)
    except Channel.DoesNotExist:
        channel_id = Channel(channel_name=channel, user=user.user)
        channel_id.save()
        field_id = Field(channel=channel_id, field_name=field, data=data)
        field_id.save()
        return HttpResponse("Created channel" + channel + " with " + " field " + field)
    try:
        field_id = Field.objects.get(channel=channel_id, field_name=field)
    except Field.DoesNotExist:
        field_id = Field(channel=channel_id, field_name=field, data=data)
        field_id.save()
        return HttpResponse("Created field" + field + " with data " + data)
    field_id.data = data
    field_id.save()
    return HttpResponse("updated")


@api_view(['GET'])
@authentication_classes((AccessKeyAuthentication, ))
def history_list(request, channel, field, format=None):
    try:
        access_key = request.GET['access_key']
        user = Token.objects.get(key=access_key)
        channel_id = Channel.objects.get(channel_name=channel, user=user.user)
    except Channel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        field_id = Field.objects.get(channel=channel_id, field_name=field)
    except Field.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    history = FieldHistory.objects.filter(field=field_id)
    serializer = HistorySerializer(history, many=True)
    return Response(serializer.data)

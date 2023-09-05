from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Person
from .serializers import *

@api_view(['GET', 'POST'])
def app_list(request):
    if request.method == 'GET':
        data = Person.objects.all()

        serializer = PersonSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

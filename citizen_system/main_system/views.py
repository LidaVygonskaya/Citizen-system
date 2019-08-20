import numpy as np
from django.db import models
from django.db.models import Func, Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from main_system.models import Citizen, CitizensGroup
from main_system.serializers import CitizenSerializer, CitizenUpdateSerializer


@api_view(['POST'])
def add_citizen_group(request: Request) -> Response:
    """
    Creates new group of citizens.
    :param request: request
    :return: Response
    """
    import_group = CitizensGroup()
    serializer = CitizenSerializer(data=request.data['citizens'], many=True, context={'import_group': import_group})

    if serializer.is_valid():
        import_group.save()

        serializer.save(import_group=import_group)
        response_data = {'data': {'import_id': import_group.import_id}}
        return Response(response_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def update_citizen(request: Request, import_id: int, citizen_id: int) -> Response:
    """
    Updates citizen's data
    :param citizen_id: citizen_id field to update
    :param import_id: import_id field of CitizenGroup
    :param request: request
    :return:
    """
    citizen_group = Citizen.objects.filter(import_group=import_id)
    citizen = citizen_group.get(citizen_id=citizen_id)
    serializer = CitizenUpdateSerializer(citizen,
                                         data=request.data,
                                         partial=True,
                                         context={'citizen_id': citizen_id,
                                                  'import_group_id': import_id,
                                                  'citizen_group': citizen_group})
    if serializer.is_valid():
        serializer.save()
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_imports_citizens(request: Request, import_id: int) -> Response:
    """
    Get all citizens from import by import_id field
    :param request: request
    :param import_id: import_id field of CitizenGroup
    :return:
    """
    queryset = Citizen.objects.filter(import_group=import_id).order_by('citizen_id')
    serializer = CitizenSerializer(queryset, many=True)
    return Response({'data': serializer.data}, status=status.HTTP_200_OK)


class Month(Func):
    function = 'EXTRACT'
    template = '%(function)s(MONTH from %(expressions)s)'
    output_field = models.IntegerField()


@api_view(['GET'])
def get_presents_amount(request: Request, import_id: int) -> Response:
    """
    Get amount of presents every citizen should buy in every month.
    :param request: request
    :param import_id: import_id field of CitizenGroup
    :return:
    """
    response_data = {month: [] for month in range(1, 13)}
    citizens_group = Citizen.objects.filter(import_group=import_id)

    for citizen in citizens_group:
        relatives = (citizens_group.filter(citizen_id__in=citizen.relatives)
                     .annotate(month=Month('birth_date'))
                     .values('month')
                     .annotate(presents=Count('month'))
                     )
        for result in relatives:
            response_data[result['month']].append({
                'citizen_id': citizen.citizen_id,
                'presents': result['presents']
            })
    return Response({'data': response_data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_towns_stat(request: Request, import_id: int) -> Response:
    """
    Get percentile for citizens by towns.
    :param request: request
    :param import_id: import_id field of CitizenGroup
    :return:
    """
    response_data = []
    citizens = Citizen.objects.filter(import_group=import_id)
    towns = citizens.values_list('town', flat=True).distinct()

    for town in towns:
        town_citizens_age = citizens.filter(town=town).values_list('age', flat=True)
        percentile_50 = np.int(np.ceil(np.percentile(np.array(town_citizens_age), 50, interpolation='linear')))
        percentile_75 = np.int(np.ceil(np.percentile(np.array(town_citizens_age), 75, interpolation='linear')))
        percentile_99 = np.int(np.ceil(np.percentile(np.array(town_citizens_age), 99, interpolation='linear')))
        response_data.append({'town': town, 'p50': percentile_50, 'p75': percentile_75, 'p99': percentile_99})

    return Response({'data': response_data}, status=status.HTTP_200_OK)

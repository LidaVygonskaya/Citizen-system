import re

from rest_framework import serializers

from main_system.models import Citizen

# TODO: попробовать вынести валидацию отдельной функцией


class CitizenListSerializer(serializers.ListSerializer):
    """
    List Serializer for citizen group for bulk creating.
    """
    def validate(self, attrs):
        citizens_ids = [citizen['citizen_id'] for citizen in attrs]
        if len(set(citizens_ids)) != len(citizens_ids):
            raise serializers.ValidationError('Field citizen_id contains duplicate values.')
        return attrs

    def create(self, validated_data):
        return Citizen.objects.bulk_create([Citizen(**data) for data in validated_data])

    def update(self, instance, validated_data):
        raise NotImplementedError


class CitizenSerializer(serializers.ModelSerializer):
    """
    Serializer for citizen group. On create.
    """
    class Meta:
        model = Citizen
        list_serializer_class = CitizenListSerializer
        fields = [
            'citizen_id',
            'town',
            'street',
            'building',
            'apartment',
            'name',
            'birth_date',
            'gender',
            'relatives'
        ]

    def _get_citizen_by_citizen_id(self, citizen_id):
        for citizen in self.initial_data:
            if citizen['citizen_id'] == citizen_id:
                return citizen
        return None

    def validate(self, attrs):
        attrs = super().validate(attrs)

        name = attrs['name']
        if not Citizen.validate_name_field(name):
            raise serializers.ValidationError(f'Name {name} is invalid')

        relatives = attrs['relatives']
        if len(set(relatives)) != len(relatives):
            raise serializers.ValidationError('Field relatives contains duplicate values.')

        current_citizen_id = attrs['citizen_id']

        for relative_id in relatives:
            relative_model = self._get_citizen_by_citizen_id(relative_id)

            if relative_model is None:
                raise serializers.ValidationError(f'Citizen with citizen_id {relative_id}'
                                                  f' is not presented in import.')

            if current_citizen_id not in relative_model['relatives']:
                raise serializers.ValidationError(f'Citizen with {relative_id} does not have citizen with citizen_id'
                                                  f' {current_citizen_id} in his relatives')
            if relative_id == current_citizen_id:
                raise serializers.ValidationError(f'Citizen with id {current_citizen_id}'
                                                  f' has self-related relatives field')
        return attrs

    def to_internal_value(self, data):
        data['import_group'] = self.context.get('import_group')
        return super().to_internal_value(data)


class CitizenUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for citizen group. On update. Exclude citizen_id field.
    """
    class Meta:
        model = Citizen
        fields = [
            'town',
            'street',
            'building',
            'apartment',
            'name',
            'birth_date',
            'gender',
            'relatives'
        ]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        current_citizen_id = self.context.get('citizen_id')

        citizens = self.context.get('citizen_group')
        citizens_ids = [citizen.citizen_id for citizen in citizens]

        name = attrs.get('name')
        if name is not None and not Citizen.validate_name_field(name):
            raise serializers.ValidationError(f'Name {name} is invalid')

        relatives = attrs.get('relatives')
        if relatives:
            if len(set(relatives)) != len(relatives):
                raise serializers.ValidationError('Field relatives contains duplicate values.')

            for relative_id in relatives:
                if relative_id not in citizens_ids:
                    raise serializers.ValidationError(f'Citizen with citizen_id {relative_id}'
                                                      f' is not presented in import.')

                if relative_id == current_citizen_id:
                    raise serializers.ValidationError(f'Citizen with id {current_citizen_id}'
                                                      f' has self-related relatives field')
        return attrs

    def update(self, instance, validated_data):
        citizens = self.context.get('citizen_group')
        current_citizen_id = self.context.get('citizen_id')

        relatives_after = set(validated_data.get('relatives', instance.relatives))
        relatives_before = set(instance.relatives)

        if relatives_after != relatives_before:
            deleted_relatives = relatives_before - relatives_after
            added_relatives = relatives_after - relatives_before

            # Delete relatives
            for relative_id in deleted_relatives:
                relative_model = citizens.get(citizen_id=relative_id)
                relative_model.relatives.remove(current_citizen_id)
                relative_model.save()

            # Add citizen to all relatives
            for relative_id in added_relatives:
                relative_model = citizens.get(citizen_id=relative_id)
                relative_model.relatives.append(current_citizen_id)
                relative_model.save()

            instance.relatives = list(relatives_after)

        instance.town = validated_data.get('town', instance.town)
        instance.street = validated_data.get('street', instance.street)
        instance.building = validated_data.get('building', instance.building)
        instance.apartment = validated_data.get('apartment', instance.apartment)
        instance.name = validated_data.get('name', instance.name)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance

    def to_representation(self, instance):
        data = {'citizen_id': instance.citizen_id}
        data.update(super().to_representation(instance))
        return data

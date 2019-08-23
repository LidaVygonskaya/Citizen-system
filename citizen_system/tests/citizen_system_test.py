import json
import time

import pytest
import requests
from citizen_system_config import c


def import_citizens(template: dict) -> int:
    response = requests.post(f'{c.host}/imports',
                             data=json.dumps(template),
                             headers={'Content-Type': 'application/json'})
    return response.json()['data']['import_id']


@pytest.fixture(scope='session')
def add_import_towns():
    return import_citizens(c.different_towns_template)


@pytest.fixture(scope='function')
def add_import_many_citizen():
    return import_citizens(c.many_citizens_template)


@pytest.fixture(scope='session')
def add_import_citizen_update():
    return import_citizens(c.citizen_update_check)


class TestCitizenCreate:
    @pytest.mark.parametrize('name, request_template', [
        ('simple_test', c.base_one_citizen_template),
        ('10000_citizens', c.many_citizens_template),
        ('many_towns', c.different_towns_template)
    ])
    def test_positive_create(self, name, request_template):
        time_start = time.time()
        response = requests.post(f'{c.host}/imports',
                                 data=json.dumps(request_template),
                                 headers={'Content-Type': 'application/json'})

        time_end = time.time()
        assert response.status_code == 201, 'Wrong response code'
        assert (time_end - time_start) < 10.0, 'Time limit exceeded'
        assert isinstance(response.json()['data']['import_id'], int), 'Wrong format import_id'

    @pytest.mark.parametrize('name, request_template', [
        ('wrong gender', c.wrong_gender_template),
        ('same_citizen_id', c.same_citizen_id_template),
        ('duplicate_relatives', c.duplicate_relatives_values),
        ('not_existant_relative', c.not_existant_relative),
        ('wrong_relation', c.wrong_relation),
        ('not_existant_date', c.not_existant_date),
        ('invalid_name', c.invalid_name_template),
    ])
    def test_wrong_params(self, name, request_template):
        response = requests.post(f'{c.host}/imports',
                                 data=json.dumps(request_template),
                                 headers={'Content-Type': 'application/json'})
        assert response.status_code == 400


class TestCitizenUpdate:
    def test_positive_update_many_relatives(self, add_import_many_citizen):
        id_ = add_import_many_citizen
        time_start = time.time()
        response = requests.patch(f'{c.host}/imports/{id_}/citizens/1000',
                                  data=json.dumps({'relatives': []}),
                                  headers={'Content-Type': 'application/json'})
        time_end = time.time()
        assert response.status_code == 200
        assert (time_end - time_start) < 10.0, 'Time limit exceeded'

    def test_example(self, add_import_citizen_update):
        """Create test like in example"""
        id_ = add_import_citizen_update
        response = requests.patch(f'{c.host}/imports/{id_}/citizens/3',
                                  data=json.dumps(c.first_update_template),
                                  headers={'Content-Type': 'application/json'})
        assert response.status_code == 200
        response_citizens = requests.get(f'{c.host}/imports/{id_}/citizens')
        assert response_citizens.json() == c.first_update_response_template, 'Wrong after first update response'

        response = requests.patch(f'{c.host}/imports/{id_}/citizens/3',
                                  data=json.dumps(c.second_update_template),
                                  headers={'Content-Type': 'application/json'})
        assert response.status_code == 200
        response_citizens = requests.get(f'{c.host}/imports/{id_}/citizens')
        assert response_citizens.json() == c.second_update_response_template, 'Wrong after second update response'

    @pytest.mark.parametrize('name, request_template', [
        ('wrong gender', c.wrong_gender_update_template),
        ('duplicate_relatives', c.duplicate_relatives_update_values),
        ('not_existant_relative', c.not_existant_update_relative),
        ('not_existant_date', c.not_existant_update_date),
        ('wrong_format_date', c.wrong_format_update_date),
        ('wrong_format_date_2', c.wrong_format_update_date_2)
    ])
    def test_wrong_params(self, name, request_template, add_import_many_citizen):
        id_ = add_import_many_citizen
        response = requests.patch(f'{c.host}/imports/{id_}/citizens/1',
                                  data=json.dumps(request_template),
                                  headers={'Content-Type': 'application/json'})
        assert response.status_code == 400


class TestCitizenGetMethods:
    def test_get_all_citizens(self, add_import_many_citizen):
        id_ = add_import_many_citizen
        time_start = time.time()
        response = requests.get(f'{c.host}/imports/{id_}/citizens',
                                headers={'Content-Type': 'application/json'})
        time_end = time.time()
        assert response.status_code == 200, 'Wrong response code'
        assert (time_end - time_start) < 10.0, 'Time limit exceeded'
        assert response.json() == {'data': c.many_citizens_template['citizens']}, 'Wrong response data'

    def test_get_birthdays(self, add_import_many_citizen):
        id_ = add_import_many_citizen
        time_start = time.time()
        response = requests.get(f'{c.host}/imports/{id_}/citizens/birthdays',
                                headers={'Content-Type': 'application/json'})
        time_end = time.time()
        assert response.status_code == 200, 'Wrong response code'
        assert (time_end - time_start) < 10.0, 'Time limit exceeded'
        assert response.json() == c.get_birthdays_response_template, 'Wrong response data'

    def test_get_percentile_stat(self, add_import_towns):
        id_ = add_import_towns
        time_start = time.time()
        response = requests.get(f'{c.host}/imports/{id_}/towns/stat/percentile/age',
                                headers={'Content-Type': 'application/json'})
        time_end = time.time()
        assert response.status_code == 200, 'Wrong response code'
        assert (time_end - time_start) < 10.0, 'Time limit exceeded'

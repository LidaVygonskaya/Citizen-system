import copy
import random
import string


class Config:
    """
    Class for config to get templates as fields.
    """

    pass


def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(string_length))


c = Config()

c.host = "http://0.0.0.0:8000"
c.base_one_citizen_template = {
    "citizens": [
        {
            "apartment": 7,
            "citizen_id": 1,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "name": "Иванов Иван Иванович",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": [],
        }
    ]
}

c.base_two_citiens_template = {
    "citizens": [
        {
            "apartment": 7,
            "citizen_id": 1,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "name": "Иванов Иван Иванович",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": [2],
        },
        {
            "apartment": 123,
            "citizen_id": 2,
            "town": "Петербург",
            "street": "Пушкина",
            "building": "Колотушкина",
            "name": "Нинова Нина Петровна",
            "birth_date": "25.08.2002",
            "gender": "female",
            "relatives": [1],
        },
    ]
}

c.citizen_without_ = {
    "citizens": [
        {
            "apartment": 7,
            "citizen_id": 1,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "name": "Иванов Иван",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": [],
        }
    ]
}

c.wrong_gender_template = copy.deepcopy(c.base_one_citizen_template)
c.wrong_gender_template["citizens"][0]["gender"] = "blablabla"

c.duplicate_relatives_values = copy.deepcopy(c.base_one_citizen_template)
c.duplicate_relatives_values["citizens"][0]["relatives"] = [1, 1]

c.not_existant_relative = copy.deepcopy(c.base_one_citizen_template)
c.not_existant_relative["citizens"][0]["relatives"] = [2]

c.invalid_name_one_word_template = copy.deepcopy(c.base_one_citizen_template)
c.invalid_name_one_word_template['citizens'][0]['name'] = 'Иван'

c.invalid_apartment = copy.deepcopy(c.base_one_citizen_template)
c.invalid_apartment['citizens'][0]['apartment'] = 'apart'

c.empty_town = copy.deepcopy(c.base_one_citizen_template)
c.empty_town['citizens'][0]['town'] = ''

c.empty_street = copy.deepcopy(c.base_one_citizen_template)
c.empty_street['citizens'][0]['street'] = ''

c.empty_building = copy.deepcopy(c.base_one_citizen_template)
c.empty_building['citizens'][0]['building'] = ''

c.empty_birth_date = copy.deepcopy(c.base_one_citizen_template)
c.empty_birth_date['citizens'][0]['birth_date'] = ''

c.empty_name = copy.deepcopy(c.base_one_citizen_template)
c.empty_name['citizens'][0]['name'] = ''

c.no_apartment = copy.deepcopy(c.base_one_citizen_template)
del c.no_apartment['citizens'][0]['apartment']

c.no_town = copy.deepcopy(c.base_one_citizen_template)
del c.no_town['citizens'][0]['town']

c.no_street = copy.deepcopy(c.base_one_citizen_template)
del c.no_street['citizens'][0]['street']

c.no_building = copy.deepcopy(c.base_one_citizen_template)
del c.no_building['citizens'][0]['building']

c.no_birth_date = copy.deepcopy(c.base_one_citizen_template)
del c.no_birth_date['citizens'][0]['birth_date']

c.no_gender = copy.deepcopy(c.base_one_citizen_template)
del c.no_gender['citizens'][0]['gender']

c.no_relatives = copy.deepcopy(c.base_one_citizen_template)
del c.no_relatives['citizens'][0]['relatives']

c.no_name = copy.deepcopy(c.base_one_citizen_template)
del c.no_name['citizens'][0]['name']

c.same_citizen_id_template = {
    "citizens": [
        {
            "apartment": 7,
            "citizen_id": 1,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "name": "Иванов Иван Иванович",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": [],
        },
        {
            "apartment": 123,
            "citizen_id": 1,
            "town": "Петербург",
            "street": "Пушкина",
            "building": "Колотушкина",
            "name": "Нинова Нина Петровна",
            "birth_date": "25.08.2002",
            "gender": "female",
            "relatives": [],
        },
    ]
}

c.wrong_relation = {
    "citizens": [
        {
            "apartment": 7,
            "citizen_id": 1,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "name": "Иванов Иван Иванович",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": [],
        },
        {
            "apartment": 123,
            "citizen_id": 2,
            "town": "Петербург",
            "street": "Пушкина",
            "building": "Колотушкина",
            "name": "Нинова Нина Петровна",
            "birth_date": "25.08.2002",
            "gender": "female",
            "relatives": [1],
        },
    ]
}

c.not_existant_date = copy.deepcopy(c.base_one_citizen_template)
c.not_existant_date["citizens"][0]["birth_date"] = "31.02.2019"

c.simple_citizen_template = {
    "apartment": 7,
    "citizen_id": 1,
    "town": "Москва",
    "street": "Льва Толстого",
    "building": "16к7стр5",
    "name": "Иванов Иван Иванович",
    "birth_date": "26.12.1986",
    "gender": "male",
    "relatives": [],
}


def generate_citizen(citizen_id):
    """
    Returns citizen, from simple citizen_template.
    :type citizen_id: citizen's id
    :return: new citizens template
    """
    new_template = copy.deepcopy(c.simple_citizen_template)
    new_template["citizen_id"] = citizen_id
    return new_template


# Template with 10 000 citizens and 2000 relationships
c.many_citizens_template = {"citizens": [generate_citizen(i) for i in range(10000)]}
c.many_citizens_template["citizens"][1000]["relatives"] = [i for i in range(1000)]
for i in range(1000):
    c.many_citizens_template["citizens"][i]["relatives"] = [1000]


# Template with 10 000 citizens and 2000 relationships and different town
c.different_towns_template = {"citizens": [generate_citizen(i) for i in range(10000)]}
c.different_towns_template["citizens"][1000]["relatives"] = [i for i in range(1000)]

c.percentile_different_towns_response_template = {
    "data": [{"town": "town", "p50": 32, "p75": 32, "p99": 32} for i in range(1000)]
}

for i in range(1000):
    c.different_towns_template["citizens"][i]["relatives"] = [1000]
    town = random_string()
    c.different_towns_template["citizens"][i]["town"] = town
    c.percentile_different_towns_response_template["data"][i]["town"] = town

c.percentile_different_towns_response_template["data"] = sorted(
    c.percentile_different_towns_response_template["data"], key=lambda elem: elem["town"]
)

c.percentile_different_towns_response_template["data"].append({"town": "Москва", "p50": 32, "p75": 32, "p99": 32})

c.percentile_import_template = {
    "citizens": [
        {
            "apartment": 7,
            "citizen_id": 1,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "name": "Иванов Иван Иванович",
            "birth_date": "26.12.2000",
            "gender": "male",
            "relatives": [2],
        },
        {
            "apartment": 123,
            "citizen_id": 2,
            "town": "Петербург",
            "street": "Пушкина",
            "building": "Колотушкина",
            "name": "Нинова Нина Петровна",
            "birth_date": "25.08.1950",
            "gender": "female",
            "relatives": [1],
        },
        {
            "apartment": 123,
            "citizen_id": 3,
            "town": "Петербург",
            "street": "Пушкина",
            "building": "Колотушкина",
            "name": "Нинова Нина Петровна",
            "birth_date": "25.08.2015",
            "gender": "female",
            "relatives": [],
        },
        {
            "apartment": 7,
            "citizen_id": 4,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "name": "Иванов Иван Иванович",
            "birth_date": "26.12.1990",
            "gender": "male",
            "relatives": [],
        },
    ]
}

c.percentile_response_template = {
    "data": [
        {"town": "Москва", "p50": 23, "p75": 26, "p99": 28},
        {"town": "Петербург", "p50": 36, "p75": 52, "p99": 68},
    ]
}

c.citizen_update_check = {
    "citizens": [
        {
            "apartment": 7,
            "citizen_id": 1,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "name": "Иванов Иван",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": [2],
        },
        {
            "apartment": 7,
            "citizen_id": 2,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "name": "Иванов Сергей",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": [1],
        },
        {
            "apartment": 23,
            "citizen_id": 3,
            "town": "Питер",
            "street": "Льва",
            "building": "16",
            "name": "Иванов Мария Леонидовна",
            "birth_date": "26.12.1986",
            "gender": "female",
            "relatives": [],
        },
    ]
}

c.first_update_template = {
    "apartment": 7,
    "town": "Москва",
    "street": "Льва Толстого",
    "building": "16к7стр5",
    "birth_date": "26.12.1986",
    "gender": "female",
    "relatives": [1],
}

c.second_update_template = {"relatives": []}

c.first_update_response_template = {
    "data": [
        {
            "citizen_id": 1,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "apartment": 7,
            "name": "Иванов Иван",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": [2, 3],
        },
        {
            "citizen_id": 2,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "apartment": 7,
            "name": "Иванов Сергей",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": [1],
        },
        {
            "citizen_id": 3,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "apartment": 7,
            "name": "Иванов Мария Леонидовна",
            "birth_date": "26.12.1986",
            "gender": "female",
            "relatives": [1],
        },
    ]
}

c.second_update_response_template = {
    "data": [
        {
            "citizen_id": 1,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "apartment": 7,
            "name": "Иванов Иван",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": [2],
        },
        {
            "citizen_id": 2,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "apartment": 7,
            "name": "Иванов Сергей",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": [1],
        },
        {
            "citizen_id": 3,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "apartment": 7,
            "name": "Иванов Мария Леонидовна",
            "birth_date": "26.12.1986",
            "gender": "female",
            "relatives": [],
        },
    ]
}

c.wrong_gender_update_template = {"gender": "blabalbal"}
c.duplicate_relatives_update_values = {"relatives": [2, 2]}
c.not_existant_update_relative = {"relatives": [8000000]}
c.not_existant_update_date = {"birth_date": "31.02.2019"}
c.wrong_format_update_date = {"birth_date": "11-11-2019"}
c.wrong_format_update_date_2 = {"birth_date": "12.25.2019"}
c.wrong_name_update_template = {"name": "Иван Иванов Иванович Слово"}
c.wrong_name_update_template_2 = {"name": "иван"}

c.invalid_name_template = {
    "citizens": [
        {
            "apartment": 7,
            "citizen_id": 1,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "name": "Иванов",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": [],
        }
    ]
}

c.invalid_name_template_four_words = {
    "citizens": [
        {
            "apartment": 7,
            "citizen_id": 1,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "name": "Иванов Иван Иванович Слово",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": [],
        }
    ]
}

c.get_birthdays_response_template = {
    "data": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
        "7": [],
        "8": [],
        "9": [],
        "10": [],
        "11": [],
        "12": [
            {"citizen_id": id_, "presents": 1} if id_ != 1000 else {"citizen_id": id_, "presents": 1000}
            for id_ in range(1001)
        ],
    }
}

c.get_birthdays_import_different_months_test = {
    "citizens": [
        {
            "apartment": 7,
            "citizen_id": 1,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "name": "Иванов Иван Иванович",
            "birth_date": "26.01.1986",
            "gender": "male",
            "relatives": [5],
        },
        {
            "apartment": 7,
            "citizen_id": 2,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "name": "Иванов Иван Иванович",
            "birth_date": "26.01.1986",
            "gender": "male",
            "relatives": [5],
        },
        {
            "apartment": 7,
            "citizen_id": 3,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "name": "Иванов Иван Иванович",
            "birth_date": "26.01.1986",
            "gender": "male",
            "relatives": [5, 4],
        },
        {
            "apartment": 7,
            "citizen_id": 4,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "name": "Иванов Иван Иванович",
            "birth_date": "26.03.1986",
            "gender": "male",
            "relatives": [3],
        },
        {
            "apartment": 7,
            "citizen_id": 5,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "name": "Иванов Иван Иванович",
            "birth_date": "26.11.1986",
            "gender": "male",
            "relatives": [1, 2, 3],
        },
        {
            "apartment": 7,
            "citizen_id": 6,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "name": "Иванов Иван Иванович",
            "birth_date": "26.05.1986",
            "gender": "male",
            "relatives": [],
        },
    ]
}

c.get_birthdays_response_different_months_test = {
    "data": {
        "1": [{"citizen_id": 4, "presents": 1}, {"citizen_id": 5, "presents": 3}],
        "2": [],
        "3": [{"citizen_id": 3, "presents": 1}],
        "4": [],
        "5": [],
        "6": [],
        "7": [],
        "8": [],
        "9": [],
        "10": [],
        "11": [{"citizen_id": 1, "presents": 1}, {"citizen_id": 2, "presents": 1}, {"citizen_id": 3, "presents": 1}],
        "12": [],
    }
}

c.simple_update_request_template = {
    "apartment": 128,
    "citizen_id": 25,
    "town": "Петербург",
    "street": "Пушкина",
    "building": "9к7стр5",
    "name": "Иванов Сменил Иванович",
    "birth_date": "22.12.1986",
    "gender": "female",
}

c.simple_update_response_template = {
    "data": {
        "apartment": 128,
        "citizen_id": 1,
        "town": "Петербург",
        "street": "Пушкина",
        "building": "9к7стр5",
        "name": "Иванов Сменил Иванович",
        "birth_date": "22.12.1986",
        "gender": "female",
        "relatives": [],
    }
}

c.get_citizens_update_response_template = {
    "data": [
        {
            "apartment": 128,
            "citizen_id": 1,
            "town": "Петербург",
            "street": "Пушкина",
            "building": "9к7стр5",
            "name": "Иванов Сменил Иванович",
            "birth_date": "22.12.1986",
            "gender": "female",
            "relatives": [],
        }
    ]
}

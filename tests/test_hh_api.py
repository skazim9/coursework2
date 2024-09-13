from src.hh_api import HeadHunterAPI


def test_head_hunter_api():
    api = HeadHunterAPI()
    vacs = api.load_vacancies("python")
    assert len(vacs) == 2000
import requests
from django.http import JsonResponse


class TagService:
    BASE_URL = 'https://www.wikidata.org/w/api.php'

    SEARCH_QS = 'action=wbsearchentities&format=json&language=en&type=item&continue=0&search=%s'

    FIND_BY_IDS_QS = 'action=wbgetentities&ids=%s&languages=en&format=json'

    FIND_BY_ID_QS = 'action=wbgetentities&ids=%s&languages=en&format=json'

    @staticmethod
    def search(query: str) -> JsonResponse:
        request_uri = TagService.BASE_URL + TagService.SEARCH_QS.format(query)

        return TagService.__return_json_response(request_uri)

    @staticmethod
    def find_by_id(e_id: int) -> JsonResponse:
        request_uri = TagService.BASE_URL + TagService.FIND_BY_ID_QS.format(e_id)

        return TagService.__return_json_response(request_uri)

    @staticmethod
    def find_by_ids(ids: tuple) -> JsonResponse:
        request_uri = TagService.BASE_URL + TagService.FIND_BY_IDS_QS.format(','.join(ids))

        return TagService.__return_json_response(request_uri)

    @staticmethod
    def __return_json_response(request_uri, payload={}, headers={}):
        response = requests.request('GET', request_uri, headers=headers, data=payload)

        return JsonResponse({'response': response.json()})
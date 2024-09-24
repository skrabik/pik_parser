import requests

class pikAPI:

    FLAT_PAGE_URI = 'https://pik-arenda.ru/flats/{}'
    MOSCOW_FLATS_ENDPOINT = 'https://vitrina.pik-arenda.ru/api/flats'

    def __init__(self):
        pass

    def get_flats(self, params):
        flats = list()
        chords = [55.38899903173059, 37.42138883979616, 55.93549878332896, 	38.14923307807739]
        i = 0
        while i < 100:
            params['page'] = i
            url = self.create_uri(endpoint=self.MOSCOW_FLATS_ENDPOINT, get_params=params, chords=chords)
            print(f'Сбор данных с url: {url}')
            res = requests.get(url)
            try:
                for el in res.json():
                    flats.append(el)
            except Exception as e:
                print(e)
                break
            i += 1
        return flats
    def create_uri(self, endpoint, get_params, chords=list()):
        endpoint += '?'
        for param in get_params:
            endpoint += ('&' if endpoint[-1] != '?' else '') + param + '=' + str(get_params[param])
        if len(chords):
            for chord in chords:
                endpoint += ('&' if endpoint[-1] != '?' else '') + 'coords[]=' + str(chord)
        return endpoint


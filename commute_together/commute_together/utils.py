import json
from urllib import request, parse 


from commute_together.models import StationModel

RASP_KEY = '396585a1-6eef-41c8-b63c-2ad283b1c38f'


def get_json(url):
	req = request.urlopen(url)
	encoding = req.headers.get_content_charset()
	data = json.loads(req.read().decode(encoding))
	return data


def get_thread_stations(thread_id):
	"""
	https://api.rasp.yandex.net/v1.0/thread/ ?
  apikey=<ключ> 
& format=<формат>
& uid=<идентификатор нитки>
& lang=<язык>
& [date=<дата>]
& [show_systems=<коды в ответе>]
	"""

	params = parse.urlencode({
		'apikey': RASP_KEY,
		'format': 'json',
		'uid': thread_id,
		'lang': 'ua'
	})

	url = 'https://api.rasp.yandex.net/v1.0/thread/?%s' % params
	
	return get_json(url)


def get_threads_between_stations(from_name, to_name):
	"""
	https://api.rasp.yandex.net/v1.0/search/ ?
  apikey=<ключ> 
& format=<формат>
& from=<код станции отправления>
& to=<код станции прибытия>
& lang=<язык>
& [date=<дата>]
& [transport_types=<тип транспорта>]
& [system=<текущая система кодирования>]
& [page=<страница>]
	"""
	from_id = StationModel.objects.get(name=from_name).code
	to_id = StationModel.objects.get(name=to_name).code

	print (from_id)

	params = parse.urlencode({
		'apikey': RASP_KEY,
		'format': 'json',
		'from': from_id,
		'to': to_id,
		'lang': 'ua',
		'transport_types': 'suburban'
	})

	url = 'https://api.rasp.yandex.net/v1.0/search/?%s' % params
	
	return get_json(url)


def get_stations_trips(station_id):
	"""
	https://api.rasp.yandex.net/v1.0/schedule/ ?
  apikey=<ключ> 
& format=<формат>
& station=<код станции>
& lang=<язык>
& [date=<дата>]
& [transport_types=<тип транспорта>]
& [system=<текущая система кодирования>]
& [show_systems=<коды в ответе>]
	"""
	params = parse.urlencode({
		'apikey': RASP_KEY,
		'format': 'json',
		'station': station_id,
		'lang': 'ua',
		'transport_types': 'suburban'
	})

	url = 'https://api.rasp.yandex.net/v1.0/schedule/?%s' % params 
	
	return get_json(url)


def load_stations_to_db():
	stations = get_thread_stations('6602V_9615001_g14_af')

	for stop in stations['stops']:
		station = StationModel(name=stop['station']['title'], code=stop['station']['code'])
		station.save()

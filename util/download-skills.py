import requests
import shutil

for skillid in range(3410):
	print('downloading skillid {}...'.format(skillid))
	r = requests.get('https://gwpvx.gamepedia.com/extensions/PvXCode/images/img_skills/{}.jpg'.format(skillid), stream=True)
	if r.status_code == 200:
		with open('img/skill/{}.jpg'.format(skillid), 'wb') as f:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f)
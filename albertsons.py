import requests
import time
from math import ceil
from collections import defaultdict
import beepy


def check_vax():
    hours_to_run = 3
    max_time = time.time() + hours_to_run*60*60
    while time.time() < max_time:
        mytime = ceil(time.time())
        response = requests.get("https://s3-us-west-2.amazonaws.com/mhc.cdn.content/vaccineAvailability.json?v={}".format(mytime))
        payload = response.json()

    
        mappings = defaultdict(list)
        for item in payload:
            mappings[item.get('address')[-5:]].append(item)
        print(time.ctime())
        
        _westside = ['90024','90025','90034','90035','90049','90056','90064','90066','90067','90073','90077','90094','90210','90212','90230','90232','90272','90291','90292','90401','90402','90403','90404','90405']
        _central = ['90004','90005','90006','90012','90013','90014','90015','90017','90019','90021','90026','90027','90028','90035','90036','90038','90039','90046','90048','90057','90068','90069','90071']
        _south = ['90001','90002','90003','90007','90008','90011','90016','90018','90037','90043','90044','90047','90059','90061','90062','90089','90220','90305']
        locs = _westside + _central + _south
        
        to_beep = False
        for z in locs:
            if z in mappings.keys():
                for i in mappings[z]:
                    if i['availability'] != 'no':
                        print(i['availability'], i['address'])
                        print(i['coach_url'])
                        to_beep = True
            else:
                pass
        if to_beep:
            beepy.beep(sound = 'coin')
        time.sleep(60)
        print()

check_vax()


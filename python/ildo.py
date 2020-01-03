import re
import sys ,os ,logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

try:
    import requests
except ImportError as s:
    logger.error(s)
url = 'https://www.xnxx.com/video-ulmp5ec/huge_natural_tits_amateur_gets_fucked_by_chubby_french'
pattern = r"'https://.*m3u8.*['^]"
resp = requests.get(url)
qualitys = re.findall(pattern,resp.text)[0].replace("'",'')

resp = requests.get(qualitys).text

presp = resp.split()[1::]
oba = [a.split(',') for a in presp]



availabe_formats = [{i.split('=')[0]:i.split('=')[1] for i in oba[o*2]} for o in range(len(oba)//2)]
links = [oba[o*2+1] for o in range(len(oba)//2)]
for i in range(len(availabe_formats)):
    availabe_formats[i].update({'link':links[i][0]})


# conv
print('hey dear wellcome ildo [xnxx , xvideos downloader]')
print('please select :')
[print(index,'\t',availabe_formats[index]['NAME']) for index in range(len(availabe_formats))]

indexNumber = int(input('please input a number :'))
print(availabe_formats[indexNumber]['link'])

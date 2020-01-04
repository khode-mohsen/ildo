import re
import sys ,os ,logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)



try:
    import requests
except ImportError as s:
    logger.error(s)

class main:
    def __init__(self):
        self.url = sys.argv[1]
        self.pattern = r"'https://.*m3u8.*['^]"
        self.run()
    def run(self):
        htmlsource = requests.get(self.url).text
        qualitys_url = re.findall(self.pattern,htmlsource)[0].replace("'",'')
        qualitys_in_m3u8 = requests.get(qualitys_url).text
        qualitys_in_m3u8_without_headline = qualitys_in_m3u8.split()[1::]
        qualitys_in_m3u8_without_headline_splited_by_cama_sign =  [a.split(',') for a in qualitys_in_m3u8_without_headline]
        qimwhsbcs = qualitys_in_m3u8_without_headline_splited_by_cama_sign
        availabe_formats = [{i.split('=')[0]:i.split('=')[1] for i in qimwhsbcs[o*2]} for o in range(len(qimwhsbcs)//2)]
        links = [qimwhsbcs[o*2+1] for o in range(len(qimwhsbcs)//2)]
        for i in range(len(availabe_formats)):
            availabe_formats[i].update({'link':links[i][0]})
        print('which quality you want?')
        [print(index,'\t',availabe_formats[index]['NAME']) for index in range(len(availabe_formats))]
        selected_index = int(input('input index number : '))
        print(self.parse_url(qualitys_url,selected_index,availabe_formats))

    def parse_url(self,url,index,av):
        modified_url = '/'.join(url.split('/')[:-1:])+'/'
        return modified_url+av[index]['link']


main()




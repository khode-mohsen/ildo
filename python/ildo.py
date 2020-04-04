import re
import sys
import os
import logging

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
        qualitys_url = re.findall(self.pattern, htmlsource)[0].replace("'", '')
        qualitys_in_m3u8 = requests.get(qualitys_url).text
        qualitys_in_m3u8_without_headline = qualitys_in_m3u8.split()[1::]
        qualitys_in_m3u8_without_headline_splited_by_cama_sign = [
            a.split(',') for a in qualitys_in_m3u8_without_headline]
        qimwhsbcs = qualitys_in_m3u8_without_headline_splited_by_cama_sign
        available_formats = [{i.split('=')[0]:i.split(
            '=')[1] for i in qimwhsbcs[o*2]} for o in range(len(qimwhsbcs)//2)]
        links = [qimwhsbcs[o*2+1] for o in range(len(qimwhsbcs)//2)]
        for i in range(len(available_formats)):
            available_formats[i].update({'link': links[i][0]})
        print('which quality you want?')
        [print(index, '\t', available_formats[index]['NAME'])
         for index in range(len(available_formats))]
        selected_index = int(input('input index number : '))
        download_url = self.parse_url(
            qualitys_url, selected_index, available_formats)
        video_name = ''.join(self.url.split('/')[-1::])+'.mkv'
        download_command = 'torify ffmpeg -i "{}" -vcodec libx264 -preset ultrafast "{}"'.format(
            download_url, video_name)

        os.system(download_command)
        print(download_command)

    def parse_url(self, url, index, av):
        modified_url = '/'.join(url.split('/')[:-1:])+'/'
        return modified_url+av[index]['link']


main()

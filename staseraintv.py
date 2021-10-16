import requests
import re
final = []
for i in range(1, 7):
    r = requests.get('https://www.staseraintv.com/index' + str(i) + '.html')
    films = re.findall('<span style=" font-weight: normal">\s*(.*)\s', r.text)
    channels = re.findall('<div class="numerocanale">\s*<br><chnum>(\d*)<\/chnum>', r.text)
    thispage = list(zip(channels, films))
    for chan, fil in thispage:
         final.append((chan, fil))

for channel, film in final:
    print('Canale   ' + channel + '  film:   ' + film)

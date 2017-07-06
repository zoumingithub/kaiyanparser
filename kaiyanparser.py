import urllib2
import request
import codecs
from tqdm import tqdm
import traceback

outf = codecs.open('/opt/dev/kaiyanparser/categorylist.txt',mode='w',encoding='utf-8')

for i in tqdm(range(0,1024,1)):
    requestUrl = "http://baobab.kaiyanapp.com/api/v3/categories/detail?id={}".format(i)
    print requestUrl
    try:
        rsp = urllib2.urlopen(requestUrl)
        content = rsp.read()
        outf.write(content.decode('utf8'))
        outf.write('\n')
        print 'succeed ',requestUrl
    except:
        print 'failed ',requestUrl
        print traceback.format_exc()
outf.close()
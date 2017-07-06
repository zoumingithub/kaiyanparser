from flask import Flask,render_template,request
import sys
import json
import urllib2
from urlparse import urlparse
import logging
import data
import logging
data.load_data()
app = Flask(__name__)

print 'catsize ', len(data.categorized_data)

@app.route('/cat/<catid>', methods=['POST','GET'])
def kaiyan_api(catid):
    if int(catid) > len(data.categorized_data):
        return "Not Found"
    docs = data.categorized_data[int(catid)]
    return render_template('kaiyan.html',videos=docs)

@app.route('/mark/<dataid>', methods=['POST','GET'])
def mark_interest(dataid):
    logging.info('mark interest {}'.format(dataid))
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1238,threaded=True)

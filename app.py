from flask import Flask, render_template
import urllib2, json

my_app = Flask(__name__)

app_id = 'd43acfa2'
app_key = '35104c97dd561b3bcfa81a7d9df94b71'

language = 'en'
word_id = 'serendipity'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

@my_app.route('/')

def root():
    request = urllib2.Request(url, headers = {'app_id': app_id, 'app_key': app_key})
    contents = urllib2.urlopen(request)
    info = contents.read()
    info_dict = json.loads(info)
    #print json.dumps(info_dict, indent=2)
    #print info_dict['results']['lexicalEntries']
    return info

'''
def NASA_root():
    u = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=3EtFP1nYRwC1RY1CMCfpXaH9yHmA4B1bkC65OFqt')
    info = u.read()
    info_dict = json.loads(info)
    return render_template('apod.html',image=info_dict['url'],summary=info_dict['explanation'])
'''

if __name__== '__main__':
    my_app.debug = True
    my_app.run()
    

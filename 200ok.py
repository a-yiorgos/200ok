import platform
import datetime
import json
from bottle import route, run, response, abort


@route('<url:re:.*>', method=['GET', 'POST'])
def hello(url='/'):

    response.headers['Content-Type'] = 'application/json'

    datum = {
            "date": datetime.datetime.utcnow(),
            "hostname": platform.node(),
            "url": url,
    }

    return json.dumps( datum, default=str)


run(host='0.0.0.0', port=8080, debug=True)

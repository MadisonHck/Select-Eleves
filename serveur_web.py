from bottle import route, run
from document import generation_plaintext, generation_html, stats_html

@route('/')
def tirage():
    return generation_plaintext()

@route('/statistique')
def statistique():
    return stats_html()

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)

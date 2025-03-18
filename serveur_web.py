from bottle import route, run
from document import generation_plaintext

@route('/')
def tirage():
    return generation_plaintext()

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)

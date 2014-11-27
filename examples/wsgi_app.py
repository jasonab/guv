import guv

guv.monkey_patch()
import guv.wsgi
import logger

logger.configure()


def app(environ, start_response):
    status = '200 OK'
    output = [b'Hello World!']
    content_length = str(len(b''.join(output)))

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', content_length)]

    start_response(status, response_headers)

    return output


if __name__ == '__main__':
    server_sock = guv.listen(('0.0.0.0', 8001))
    guv.wsgi.serve(server_sock, app)

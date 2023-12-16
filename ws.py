import tornado.ioloop
import tornado.web
import tornado.websocket
import time
import json


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        pass

    def on_close(self):
        pass

    def send_data(self, text):
        self.write_message(text)

    def on_message(self, message):
        print(message)
        self.send_data(message)

application = tornado.web.Application([
    (r'/websocket', WebSocketHandler),
])

if __name__ == '__main__':
    application.listen(3001)
    tornado.ioloop.IOLoop.current().start()
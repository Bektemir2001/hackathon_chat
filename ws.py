import tornado.ioloop
import tornado.web
import tornado.websocket
import json


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        pass

    def on_close(self):
        pass

    def send_json(self, data):
        # Convert Python dict to JSON string and send it
        json_data = json.dumps(data)
        self.write_message(json_data)

    def send_data(self, text):
        self.write_message(text)

    def on_message(self, message):
        try:
            data = json.loads(message)
            print("Received JSON:", data)

            response_data = {"response": "Received your JSON"}
            self.send_json(response_data)

        except json.JSONDecodeError as e:
            print("Error decoding JSON:", str(e))
application = tornado.web.Application([
    (r'/websocket', WebSocketHandler),
])

if __name__ == '__main__':
    application.listen(3001)
    tornado.ioloop.IOLoop.current().start()
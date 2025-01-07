from queue import Queue
import uuid


class Request:
    def __init__(self, title):
        self.id = uuid.uuid4()
        self.title = title

class Client_requests:
    def __init__(self):
        self.queue = Queue()

    def generate_request(self, new_request):
        self.queue.put(new_request)

    def process_request(self):
        while not self.queue.empty():
            current_request = self.queue.get()
            print(f'Processing request: " {current_request.title} " with id: {current_request.id}')
        else:
            return "There is no more requests. Queue is empty"


call_centre = Client_requests()

call_centre.generate_request(Request("Ethernet doesn't have a valid IP configuration"))
call_centre.generate_request(Request("No Wi-Fi adapter found"))
call_centre.generate_request(Request("Network manager not running"))

call_centre.process_request()
print(call_centre.process_request())  

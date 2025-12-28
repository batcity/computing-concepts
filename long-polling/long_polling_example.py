from flask import Flask
import threading
import requests
import time
import queue

def create_server():
    print("creating long polling server:")
    
    server = Flask(__name__)
    messages = queue.Queue()   # thread-safe, blocking
    
    @server.route('/poll')
    def poll():
    
        # blocks until an item is available
        message = messages.get()
        return message
    
    def publish_message_to_server():
        time.sleep(5)
        messages.put("hello!")
        
    threading.Thread(target=publish_message_to_server, daemon=True).start()
    server.run()
    
def poll_via_a_client():
    request = requests.get("http://127.0.0.1:5000/poll")
    print("client received the following message:", request.text)
    
    
if __name__=="__main__":   
    
    server_thread = threading.Thread(target=create_server, daemon=True)
    server_thread.start()
    
    poll_via_a_client()
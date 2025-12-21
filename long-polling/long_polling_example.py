from flask import Flask

def create_server():
    print("creating long polling server:")
    
    server = Flask(__name__)
    
    @server.route('/poll')
    def poll():
        return "hello"
    
    server.run()
    
if __name__=="__main__":   
    create_server()
    # poll_via_a_client()
    
    
from flask import Flask, request
import docker
import webbrowser  
import time

import random
import string

def generate_random_name(length=8):
    letters_and_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

app = Flask(__name__)
docker_client = docker.from_env()

@app.route('/')
def run_container():
    url = request.args.get('url')
    try:
        container_options = {
            'name': generate_random_name(),
            'detach': True,
            'shm_size': '2g',
            'environment': {'FF_OPEN_URL': url}
        }
        
        container = docker_client.containers.run("jlesage/firefox", ports={5800: None}, **container_options)
        container.reload()
        hostPort = 0
        for environs in docker_client.containers.list():
            if environs.id == container.id:
                hostPort = environs.ports['5800/tcp'][0]['HostPort']

        time.sleep(3)

        webbrowser.open(f'http://localhost:{hostPort}/', new=1, autoraise=True)

        return ""

    except docker.errors.APIError as e:
        return f"Error: {e}"
    
@app.route('/delete', methods=['POST'])
def delete_container():
    request_data = request.get_json()
    print(docker_client.containers.list())
    for environs in docker_client.containers.list():
            port = environs.ports['5800/tcp'][0]['HostPort']
            if port == request_data['port']:
                environs.stop()
                environs.remove()
                return "Container {} is deleted".format(port)
    return "Not found"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

from os import path
import subprocess
THIS_FOLDER = path.dirname(path.abspath(__file__))
AWS_KEY = '/Users/ZachLiu/OneDrive/AWS/zachliu.aws/re-tools-instance/re-tools-instance-key-pair.pem'


def create_session_on_server(host, email):
    return subprocess.check_output(
        [
            'fab',
            '-i',
            AWS_KEY,
            'create_session_on_server:email={}'.format(email),
            '--host={}'.format(host),
            '--hide=everything,status',
        ],
        cwd=THIS_FOLDER
    ).decode().strip()


def reset_database(host):
    subprocess.check_call(
        [
            'fab',
            '-i',
            AWS_KEY,
            'reset_database', 
            '--host={}'.format(host)
        ],
        cwd=THIS_FOLDER
    )
    

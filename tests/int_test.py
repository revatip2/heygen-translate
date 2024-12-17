import unittest
import time
import subprocess
import sys
from threading import Thread
import requests
sys.path.append('../client')  
from client import VideoTranslationClient  

class TestVideoTranslationIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server_process = subprocess.Popen(
            ['python3', '../server/server.py'], 
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        cls.wait_for_server_to_be_ready()

    @classmethod
    def wait_for_server_to_be_ready(cls):
        for _ in range(10):
            try:
                response = requests.get("http://127.0.0.1:5000/status")  
                if response.status_code == 200:
                    print("Server is ready.")
                    return
            except requests.ConnectionError:
                pass
            time.sleep(1)
        raise Exception("Server did not start in time!")

    @classmethod
    def tearDownClass(cls):
        cls.server_process.terminate()
        cls.server_process.wait()

    def test_video_translation(self):
        client = VideoTranslationClient(base_url="http://127.0.0.1:5000")
        print("Starting video translation check...")
        client.check_status()

if __name__ == "__main__":
    unittest.main()

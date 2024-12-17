import requests
import time

class VideoTranslationClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def check_status(self):
        start_time = time.time() 
        while True:
            
                response = requests.get(f"{self.base_url}/status")
                result = response.json()

                status = result.get("result")
                predicted_time = result.get("predicted_time", 10)  

                elapsed_time = time.time() - start_time
                remaining_time = max(0, predicted_time - elapsed_time)  

                if status == "completed":
                    print(f"Video translation completed successfully in {predicted_time} seconds!")
                    break  

                elif status == "error":
                    print("Video translation encountered an error.")
                    break  

                else:
                    print(f"Translation still pending... Predicted time: {predicted_time} seconds, Elapsed time: {elapsed_time:.2f} seconds, Remaining time: {remaining_time:.2f} seconds.")

                if remaining_time < 10:
                    print("Remaining time is less than 10 seconds, sending a ping immediately.")
                    time.sleep(remaining_time)  
                    break
                else:
                    delay = max(1, predicted_time // 2)  
                    print(f"Waiting for {delay} seconds before checking again.")
                    time.sleep(delay)


if __name__ == "__main__":
    client = VideoTranslationClient(base_url="http://127.0.0.1:5000")
    client.check_status()

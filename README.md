# Video Translation Server and Predicting Completion time dynamically using Machine Learning

The problem at hand simulates a backend video translation system with a client library to monitor its status. The challenge lies in efficiently interacting with the server, considering potential delays and the need to manage API calls without overwhelming the server or causing unnecessary delays for the user.

Here’s a breakdown of the thought process for the solution:

### 1. Understanding the Problem

Video Translation Process: Translates a video in a time-consuming process. This can depend on the video length, complexity, etc.

Instead of implementing a trivial solution where the client simply polls the server at fixed intervals, we can make the process smarter by using Machine Learning (ML) to predict the time required for translation based on several factors. This approach introduces a dynamic and predictive way to manage polling frequency, improving efficiency and reducing unnecessary requests.

### 2. Key Design Decisions
#### a. Adaptive Polling Strategy

Instead of polling the server too frequently (which would burden both the server and the client), an adaptive delay strategy was used. The client:

* Starts with a short delay between requests (e.g., 1 second).
* Dynamically adjusts the delay based on the predicted time for the translation, which is returned by the server.
* If the predicted time is low (i.e., the translation process is near completion), the delay between polls is reduced to a minimum, ensuring the user is promptly informed once the task is done.
* If the task is still pending, the client waits for a longer duration between requests, preventing unnecessary load on the server.

#### b. Prediction Model for Delays

The server uses a predictive model (RandomForestRegressor) to estimate the time required for translation. By leveraging this predicted time, the client can intelligently adjust its polling frequency. The more accurate the prediction, the more efficiently the client can handle the requests and avoid unnecessary API calls.

#### c. User-Centric Design

The library is built with a customer-focused mindset:

* Ease of Use: The client hides all complexity from the user. The user simply calls the check_status method and receives real-time status updates. There is no need to manually manage delays or retries.
* Transparency: The client provides status updates, indicating how much time has elapsed, the predicted time, and how long the user may have to wait. This ensures the user always knows where the process stands.
* Performance: The adaptive polling mechanism ensures that both server and client resources are used efficiently, striking a balance between responsiveness and resource consumption.


### Machine Learning Model
The `dataset_code.py` generates synthetic data with some probable features like video length, complexity score, and time to complete to simulate the predictive nature of the problem. This can be adjusted based on additional features which could improve the predictive capability of the model. My idea was to convey the approach effectively, and not build a robust machine learning model. Hence, the current algorithm is a simple random forest regressor with an erorr of around 300 seconds. This can be improved.

### Code File Breakdown

### 1. **`server.py`**
   - **Purpose**: Simulates the video translation backend and serves an API to check the translation status.
   - **Key functionality**: 
     - Loads the configuration file (`config.json`) to set parameters like video length and complexity score.
     - Loads the pre-trained ML model (`video_translation_model.pkl`) to predict translation completion time.
     - Exposes a `/status` endpoint that returns the status (`pending`, `completed`, or `error`) and the predicted time to complete the translation.

### 2. **`ml_dataset.py`**
   - **Purpose**: Generates a synthetic dataset to train the machine learning model for predicting video translation times.
   - **Key functionality**:
     - Randomly generates video lengths and complexity scores.
     - Calculates the time to complete based on these factors, simulating realistic translation times.
     - Saves the dataset as a CSV file (`video_translation_data.csv`).

### 3. **`ml_model.py`**
   - **Purpose**: Trains the machine learning model to predict translation times based on the generated dataset.
   - **Key functionality**:
     - Loads the dataset (`video_translation_data.csv`).
     - Trains a Random Forest Regressor model to predict the time required for video translation.
     - Evaluates the model using root mean squared error (RMSE).
     - Saves the trained model as a `.pkl` file (`video_translation_model.pkl`).

### 4. **`client.py`**
   - **Purpose**: Implements the client library that interacts with the server to get the translation status.
   - **Key functionality**:
     - Periodically checks the `/status` API to get the translation status and predicted completion time.
     - Dynamically adjusts the polling frequency based on the predicted time.

### 5. **`int_test.py`**
   - **Purpose**: Provides automated testing for the integration between the client and server.
   - **Key functionality**:
     - Starts the server as a subprocess and waits for it to become ready.
     - Tests the client’s behavior by invoking its methods and checking the responses.

### 6. **`config.json`**
   - **Purpose**: Provides configuration settings for the server, including video length, complexity score, and the path to the pre-trained model.
   - **Key functionality**:
     - Stores the configuration for video translation settings (e.g., video length, complexity score) and the path to the saved ML model (`video_translation_model.pkl`).

## Summary of Unique Features:
- **`server.py`**: Uses ML to predict translation time and adjusts status reporting accordingly.
- **`ml_dataset.py`**: Generates synthetic data to train the ML model.
- **`ml_model.py`**: Trains and saves the ML model for predicting translation time.
- **`client.py`**: Intelligent polling using the predicted translation time to optimize server interaction.
- **`intest.py`**: Automates testing of the client-server interaction.
- **`config.json`**: Stores key configuration for the server and model.

### Usage
1. `pip install requirements.txt`
2. `python3 int_test.py`

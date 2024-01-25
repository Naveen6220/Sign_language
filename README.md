# Sign Language Detection using YOLOv5

**Problem Statement:**
Mute people use hand signs to communicate, hence normal people face problem in recognizing their language by signs made. Hence there is a need of the systems which recognizes the different signs and conveys the information to the normal people

**Solution Proposed:**
The main point of this application is to use camera to recognize gestures from the sign language to offer a new means of communication. The program will be able to transcribe gestures done by dumb people into written words printed on the screen

**Project Overview:**
This project focuses on the development of a Sign Language Detection system using YOLOv5 (You Only Look Once version 5). The primary objective is to detect and interpret hand signs in real-time, facilitating communication for individuals who use sign language.

**Key Features:**
- **YOLOv5:** Implementing YOLOv5 for efficient real-time object detection, with a specific focus on recognizing hand signs.
- **Transfer Learning:** Utilizing transfer learning techniques to fine-tune the model for custom sign language recognition.
- **CI/CD with GitHub Actions:** Implementing Continuous Integration and Continuous Deployment (CI/CD) pipelines using GitHub Actions. Automated workflows are triggered with each push to GitHub, ensuring smooth testing and deployment.
- **Self-Hosted EC2 Runner:** Utilizing a self-hosted EC2 runner for GitHub Actions to push Docker images to Amazon ECR upon every GitHub push.
- **Data Extraction from GitHub:** Extracting data from GitHub repositories for model training and evaluation.

## Tech Stack Used
1. Python
2. YOLOv5
3. Transfer Learning
4. GitHub Actions
5. Docker
6. Amazon ECR

## Infrastructure Required
1. AWS EC2
2. Amazon ECR
3. GitHub Actions

## How to Run
Before running the project, ensure that you have access to AWS services like EC2 and ECR. Additionally, an AWS account is required.

### Step 1: Clone the Repository
```bash
git clone https://github.com/YourUsername/Sign_Language_Detection_YOLOv5.git
```

### Step 2: Set Up Conda Environment
```bash
conda create -n sign_language python=3.8 -y
conda activate sign_language
```

### Step 3: Install Requirements
```bash
pip install -r requirements.txt
```

### Step 4: Export Environment Variables
```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>
```

### Step 5: Run the Application Server
```bash
python app.py
```

### Step 6: Train the Model
Visit [http://localhost:8080/train](http://localhost:8080/train) to initiate model training.

### Step 7: Make Predictions
Visit [http://localhost:8080/predict](http://localhost:8080/predict) to make predictions using the trained model.

## Run Locally using Docker
1. Check if the Dockerfile is available in the project directory.
2. Build the Docker image
```bash
docker build --build-arg AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> --build-arg AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> --build-arg AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION> .
```
3. Run the Docker image
```bash
docker run -d -p 8080:8080 <IMAGE_NAME>
```

Note: Make sure to replace placeholders like `<AWS_ACCESS_KEY_ID>`, `<AWS_SECRET_ACCESS_KEY>`, `<AWS_DEFAULT_REGION>`, and `<YourUsername>` with your actual values.

Feel free to reach out if you have any questions or need further assistance!

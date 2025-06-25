#  Flask + Redis App with Docker Compose

This is a simple Python Flask web application that tracks how many times the page has been viewed — backed by Redis for persistent counting.

It's containerized and managed using **Docker Compose**.

---

##  Tech Stack

- **Python** + **Flask**
- **Redis** (key-value database)
- **Docker** & **Docker Compose**

---

## 🐳 How to Run Locally

1. Clone this repo:
   ```bash
   git clone https://github.com/charan17kk/docker-compose-flask-redis-demo.git
   cd docker-compose-flask-redis-demo
Start the containers:

bash
Copy
Edit
docker compose up
Open your browser:

arduino
Copy
Edit
http://localhost:5000
Stop the app:

bash
Copy
Edit
docker compose down
📁 Folder Structure
Copy
Edit
├── app/
│   ├── app.py
│   └── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
├── screenshot.png
📸 Screenshot

A simple web app counting page views using Flask + Redis.

💡 What I Learned
Dockerfile and image building

How containers talk using internal networks

How to orchestrate services using Compose

Real-world DevOps project flow 


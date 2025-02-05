# **Minimal Cloud Deployment for RAG Chatbot** 🚀

This guide provides step-by-step instructions to deploy the **RAG Chatbot** using **AWS EC2 for Flask API** and **AWS RDS for MySQL**.

---

## **1. Choose a Cloud Provider**
- **AWS** → EC2 (for Flask app) + RDS (for MySQL) **(Recommended)**
- **GCP** → Compute Engine + Cloud SQL
- **Azure** → Virtual Machine (VM) + Azure Database for MySQL  

---

## **2. Deploy Flask App on AWS EC2**
### **Step 1: Launch an EC2 Instance**
1. Go to **AWS EC2 Console** → Click **Launch Instance**.
2. Choose **Ubuntu 22.04 LTS** as the OS.
3. Select an **Instance Type** (e.g., `t2.micro` for free tier).
4. Configure **Security Group**:
   - Allow **Port 22** (SSH) → Your IP only.
   - Allow **Port 5000** (Flask App) → 0.0.0.0/0 (For external access).
5. Create or select a **Key Pair** (for SSH access).
6. Click **Launch**.

### **Step 2: Connect to EC2 via SSH**
```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

### **Step 3: Install Dependencies**
```bash
sudo apt update && sudo apt install -y python3-pip python3-venv

git clone https://github.com/your-repo/rag-chatbot.git
cd rag-chatbot

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **Step 4: Run Flask App**
```bash
python app.py
```
**Access it on** `http://your-ec2-public-ip:5000`.

---

## **3. Deploy MySQL Database on AWS RDS**
### **Step 1: Create an RDS Instance**
1. Go to **AWS RDS Console** → Click **Create Database**.
2. Choose **MySQL** as the engine.
3. Select **Free-tier eligible instance**.
4. Set **DB name** = `chat_history`, **Username** = `root`, **Password** = `your-password`.
5. Allow **Public access** (to connect from EC2).
6. Click **Create Database**.

### **Step 2: Connect Flask App to RDS**
Modify **database.py**:
```python
db = mysql.connector.connect(
    host="your-rds-endpoint",
    user="root",
    password="your-password",
    database="chat_history"
)
```

---

## **4. Run Flask App as a Background Service**
Instead of manually running `python app.py`, use `gunicorn`:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app --daemon
```

---

## **5. (Optional) Use Nginx + Gunicorn for Production**
1. Install Nginx:
   ```bash
   sudo apt install nginx
   ```
2. Configure Nginx:
   ```bash
   sudo nano /etc/nginx/sites-available/rag-chatbot
   ```
   Add:
   ```
   server {
       listen 80;
       server_name your-ec2-public-ip;

       location / {
           proxy_pass http://127.0.0.1:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```
3. Enable and restart Nginx:
   ```bash
   sudo ln -s /etc/nginx/sites-available/rag-chatbot /etc/nginx/sites-enabled
   sudo systemctl restart nginx
   ```

Now, your chatbot is live on `http://your-ec2-public-ip`.

---

## **6. (Optional) Dockerize & Deploy with AWS ECS**
If you want to use **Docker & ECS**, follow these steps:
1. **Build Docker Image**:
   ```bash
   docker build -t rag-chatbot .
   ```
2. **Push to AWS ECR**:
   ```bash
   aws ecr create-repository --repository-name rag-chatbot
   docker tag rag-chatbot:latest your-ecr-repo-url
   docker push your-ecr-repo-url
   ```
3. **Deploy with AWS ECS (Fargate)** → Create a task with your Docker image.

---

## **7. Monitoring & Scaling**
- **CloudWatch** → Logs & Monitoring
- **Auto-Scaling** → Scale EC2 instances automatically

---

This minimal deployment **ensures high availability and scalability** using **AWS EC2 + RDS**. Let me know if you want a **Kubernetes (EKS) setup** or **CI/CD pipeline** for auto-deployment! 🚀

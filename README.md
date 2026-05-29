# Python CI Pipeline with Jenkins and SonarQube on AWS 🚀

This project demonstrates how to build a complete **Python CI pipeline** on **AWS EC2** using **Jenkins** and **SonarQube**.  
The goal is to automate code integration, run quality checks, and maintain clean, production-ready Python code.

---

## 📌 Project Overview

In this project, two AWS EC2 instances are created:

- **Jenkins Server** → Used for CI pipeline automation
- **SonarQube Server** → Used for code quality analysis

Jenkins pulls code from GitHub, runs the build pipeline, and sends code for analysis to SonarQube.

---

## 🛠️ Technologies Used

- **AWS EC2**
- **Ubuntu 22.04**
- **Jenkins**
- **SonarQube**
- **Python**
- **Git & GitHub**
- **Java (for Jenkins & SonarQube)**

---

## 🏗️ Architecture

```text
GitHub Repository
       │
       ▼
   Jenkins EC2
(Build + Pipeline)
       │
       ▼
 SonarQube EC2
(Code Analysis)
       │
       ▼
 Quality Report
```

---

## ⚙️ AWS EC2 Setup

### Jenkins Server

Recommended:

- Ubuntu 22.04
- t2.medium

### SonarQube Server

Recommended:

- Ubuntu 22.04
- t2.medium

---

## 🔐 Security Group Rules

### Jenkins Instance

Allow:

- SSH → Port 22
- HTTP → Port 8080

### SonarQube Instance

Allow:

- SSH → Port 22
- SonarQube → Port 9000

---

## 🚀 Jenkins Installation

Update packages:

```bash
sudo apt update
```

Install Java:

```bash
sudo apt install openjdk-17-jdk -y
```

Add Jenkins repository:

```bash
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
/usr/share/keyrings/jenkins-keyring.asc > /dev/null
```

Install Jenkins:

```bash
sudo apt install jenkins -y
```

Start Jenkins:

```bash
sudo systemctl enable jenkins
sudo systemctl start jenkins
```

Check status:

```bash
sudo systemctl status jenkins
```

Access:

```text
http://<JENKINS_PUBLIC_IP>:8080
```

---

## 📊 SonarQube Installation

Install Java:

```bash
sudo apt install openjdk-17-jdk -y
```

Download SonarQube:

```bash
wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube.zip
```

Extract:

```bash
unzip sonarqube.zip
```

Run SonarQube:

```bash
./sonarqube/bin/linux-x86-64/sonar.sh start
```

Access:

```text
http://<SONARQUBE_PUBLIC_IP>:9000
```

Default login:

```text
Username: admin
Password: admin
```

---

## 🔗 GitHub Repository

Project source code:

```text
https://github.com/harsh-sojitra-901/python-ci-cd.git
```

Clone:

```bash
git clone https://github.com/harsh-sojitra-901/python-ci-cd.git
```

---

## 🔄 Jenkins Pipeline Flow

1. Developer pushes code to GitHub
2. Jenkins pulls latest code
3. Pipeline starts automatically
4. Python project build runs
5. SonarQube analyzes code
6. Quality report generated

---

## 📸 Project Screenshots

Add your screenshots here:

### AWS EC2 Instances

<img width="1621" height="285" alt="Screenshot 2026-05-22 163759" src="https://github.com/user-attachments/assets/a6ce7577-7a1c-486f-8794-48838cf39f5a" />

### Jenkins pipeline success Dashboard

<img width="1509" height="822" alt="Screenshot 2026-05-22 185249" src="https://github.com/user-attachments/assets/ef04656a-e697-47fa-beb6-c7ba1a91537e" />

### SonarQube Dashboard
<img width="1906" height="964" alt="Screenshot 2026-05-22 185650" src="https://github.com/user-attachments/assets/d11657fb-0156-44e4-8702-350daf23a0aa" />

---

## ✅ Output

- Automated Python CI pipeline
- GitHub integration
- Jenkins build automation
- SonarQube code analysis
- Clean and structured DevOps workflow

---

## 📚 Learning Outcomes

From this project:

- AWS EC2 deployment
- Jenkins installation/configuration
- SonarQube integration
- CI pipeline automation
- GitHub workflow management

---

## 👨‍💻 Author

**Harsh Sojitra**

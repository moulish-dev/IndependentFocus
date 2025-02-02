# 🚀 AI Task Manager (Gemini API + DeepSeek via Ollama)
### **An AI-Driven Task Management System Created at AI Ventures Hackathon, Imperial College London**

AI Task Manager is an **AI-powered task automation system** designed during the **AI Ventures Hackathon at Imperial College London**.  
It utilizes **Google Gemini API** and **DeepSeek (via Ollama)** to **generate structured subtasks** for any user-given task.  
The system features **an interactive AI learning panel** and **a dynamic calendar** for managing tasks efficiently.

---

## 🎯 **Features**
✅ **Hybrid AI Processing** – Uses **Google Gemini API** & **DeepSeek via Ollama**  
✅ **AI-Powered Subtasks** – Automatically generates **structured subtasks**  
✅ **Interactive Calendar** – Subtasks are assigned to **specific dates**  
✅ **AI Learning Panel** – Simulates AI **analyzing user patterns**  
✅ **Fast Local AI Processing** – Ollama runs **locally** with **DeepSeek**  
✅ **Real-Time UI Updates** – Subtasks **appear dynamically**  

---

## 🏗 **Tech Stack**
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python (Flask-like HTTP server)  
- **AI Models:**
  - **Gemini API** (Google Cloud)  
  - **DeepSeek (via Ollama)**  
- **Storage:** JSON-based  
- **Tools Used:** Local AI inference + Cloud AI API  

---

## 🛠 **Setup & Installation**

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-repo/ai-task-manager.git
cd ai-task-manager
```

### **2️⃣ Set Up Google Gemini API Key**
You'll need a **Google Gemini API key** for cloud-based task generation.  
Set it in your **environment variables** (PowerShell for Windows, Terminal for macOS/Linux):

#### **For macOS/Linux:**
```sh
export GEMINI_API_KEY="your-google-gemini-api-key"
```

#### **For Windows PowerShell:**
```sh
$env:GEMINI_API_KEY="your-google-gemini-api-key"
```

### **3️⃣ Run the Local Server**
```sh
python main.py
```

### **4️⃣ Open in Browser**
Once the server starts, go to:  
👉 **[http://localhost:8080/](http://localhost:8080/)**  

---

## 🚀 **Usage**
 **Enter a main task & due date**  
 **Subtasks appear dynamically** on the calendar  
 **AI Learning Panel updates** with insights about your working patterns  

---

## 🤖 **How It Works**
1. **User submits a task**
2. **System decides AI Processing Mode:**
   - **Uses Gemini API** (Cloud-based)  
   - **Uses DeepSeek (via Ollama) locally**  
3. **AI generates structured subtasks in JSON**
4. **Tasks dynamically update the calendar**
5. **AI Learning Panel tracks user behavior**  

---

## 🏆 **Built at AI Ventures Hackathon, Imperial College London**
This project was **developed during the AI Ventures Hackathon** to **showcase hybrid AI task automation**.  
It combines **local AI processing (Ollama + DeepSeek)** with **cloud AI (Gemini API)** for **maximum efficiency**.

---

## 🛠 **Future Enhancements**
✅ Add **customizable AI models** selection (switch between Gemini, DeepSeek, or others)  
✅ Implement **task prioritization** using AI-powered suggestions  
✅ Improve **UI/UX with animations** for better AI interaction experience  

---

## 💡 **Contributors**
👨‍💻 **Team** – Moulish, Sonal, Fariza, Ishaan, Sam
🏫 **Imperial College London** – AI Ventures Hackathon Team  

---

## 📜 **License**
This project is open-source and licensed under the **MIT License**.  
Feel free to modify, share, and contribute! 🎉

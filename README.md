# 🔐 RAG-RBAC Chatbot for FinSolve Technologies

A secure, AI-powered chatbot that enables **role-based access** to internal enterprise knowledge. Built using **Retrieval-Augmented Generation (RAG)** principles and enforcing strict **Role-Based Access Control (RBAC)**, this chatbot ensures that every department accesses only the data it is allowed to — with full auditability and transparency.

> 🧠 Designed by Peter Pandey as part of FinSolve's digital transformation initiative led by CIO Tony Sharma.

---

## 💼 Competition Background

**🏢 Organization:** FinSolve Technologies  
**📍 Domain:** FinTech  
**🎯 Function:** AI Engineering  

FinSolve faced communication delays, data silos, and lack of unified information access across departments. This chatbot was proposed as a **secure digital assistant** to provide fast, role-filtered answers and bridge interdepartmental data gaps using AI.

---

## 🛠️ Tech Stack

| Layer       | Tools Used                              |
|-------------|------------------------------------------|
| 💬 UI       | Streamlit                                |
| 🔧 Backend  | FastAPI, Modular Python App              |
| 🧠 LLM      | LLaMA 3 via Groq API                     |
| 🔍 VectorDB | ChromaDB                                 |
| ✍️ Embedding| SentenceTransformers (`all-MiniLM-L6-v2`)|
| 🔐 Auth     | Custom RBAC logic using `roles.py` & `auth.py`|

---

## 🧠 Features

- ✅ **Secure User Authentication**
- ✅ **Strict Role-Based Access Control**
- ✅ **Real-time NLP Query Handling**
- ✅ **Document Retrieval via ChromaDB**
- ✅ **Natural Answers with Groq's LLaMA3**
- ✅ **Source Citation for Every Answer**

---

## 🔐 Role Permissions

| Role          | Accessible Content                                                       |
|---------------|--------------------------------------------------------------------------|
| `finance`     | Financial reports, reimbursements, equipment costs                       |
| `marketing`   | Campaign metrics, customer feedback, sales trends                        |
| `hr`          | Employee data, payroll, attendance, performance reviews                  |
| `engineering` | Tech architecture, development docs, processes                           |
| `executive`   | 🔓 Full access to all company data                                       | 
| `employee`    | General company documents (FAQs, events, policies)                       |

---

## 🧱 Project Structure

``` RAG_chatbot
├── app/
│ ├── init.py ← Package init
│ ├── api.py ← FastAPI routes
│ ├── auth.py ← Auth & session handling
│ ├── models.py ← User & request schemas
│ ├── roles.py ← Role permission logic
│ ├── rag.py ← RAG query logic with LLM
│ └── config.py ← API keys & env setup
│
├── ingest/
│ ├── init.py
│ └── run_ingest.py ← Load markdown files, embed into ChromaDB
│
├── data/
│ └── [markdown folders: finance/, hr/, general/, etc.]
│
├── frontend/
│ └── streamlit_app.py ← UI login + chat interface
│
├── requirements.txt
└── README.md
```

## How to Run

### 1. 🔧 Install Dependencies

```pip install -r requirements.txt```

### 2.  Add Markdown Data

data/
├── finance/
│   └── report_q1.md
├── marketing/
│   └── campaign_2024.md
├── general/
│   └── leave_policy.md
...

### 3. Run Document Ingestion

python ingest/run_ingest.py

### 4. Start Backend API

streamlit run frontend/streamlit_app.py

### 5. Launch Frontend UI

streamlit run frontend/streamlit_app.py

## Sample Test Users

{
  "finance_user":  {"password": "finance_pass", "role": "finance"},
  "marketing_user": {"password": "marketing_pass", "role": "marketing"},
  "hr_user":        {"password": "hr_pass", "role": "hr"},
  "eng_user":       {"password": "eng_pass", "role": "engineering"},
  "ceo_user":      {"password": "ceo_pass", "role": "executive"},
  "employee_user":  {"password": "employee_pass", "role": "employee"}
}

## Architecture

![RAG_chatbot Architecture](https://github.com/user-attachments/assets/35685c9e-4af9-4292-9938-c40257281983)




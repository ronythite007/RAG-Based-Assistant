# 🔐 RAG-RBAC Chatbot for FinSolve Technologies

A secure, AI-powered chatbot that enables **role-based access** to internal enterprise knowledge. Built using **Retrieval-Augmented Generation (RAG)** principles and enforcing strict **Role-Based Access Control (RBAC)**, this chatbot ensures that every department accesses only the data it is allowed to — with full auditability and transparency.

---

# 🧩 Problem Statement
FinSolve Technologies faces delays and inefficiencies due to data silos across departments like Finance, HR, and Marketing. Teams struggle to access the right information securely and quickly. To solve this, a role-aware AI chatbot is needed that can authenticate users, retrieve department-specific data, and generate accurate, context-rich responses using RAG and RBAC.

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

---

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

---

## Sample Test Users

{
  "finance_user":  {"password": "finance_pass", "role": "finance"},
  "marketing_user": {"password": "marketing_pass", "role": "marketing"},
  "hr_user":        {"password": "hr_pass", "role": "hr"},
  "eng_user":       {"password": "eng_pass", "role": "engineering"},
  "ceo_user":      {"password": "ceo_pass", "role": "executive"},
  "employee_user":  {"password": "employee_pass", "role": "employee"}
}

---

## Architecture

![RAG_chatbot Architecture](https://github.com/user-attachments/assets/35685c9e-4af9-4292-9938-c40257281983)

---

## 🎓 Developed For

```🏁 Competition: Gen AI & Data Science Challenge
🏢 Company: FinSolve Technologies
👤 Role: Peter Pandey, AI Engineer
🧠 Goal: Build a secure RAG-based chatbot for department-specific answers
```
---

## Why This Solution?
```
✅ Ensures secure data access via role-based filtering
✅ Uses state-of-the-art LLMs for natural language interaction
✅ Stores and searches enterprise data using vector embeddings
✅ Built with modular architecture, easy to extend
```
---

## Author
Rohan Rajendra Thite




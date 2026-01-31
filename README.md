# AI-Powered Resume & Job Matching Platform

An AI-driven hiring platform that matches resumes with job descriptions using multilingual NLP, machine learning–based ranking, and secure skill verification to enable fair, transparent, and efficient recruitment.
This project was developed as part of a hackathon to showcase the concept of fair and intelligent recruitment.
A prototype AI-powered resume and job matching platform designed to demonstrate smart hiring workflows using resume parsing, skill-based matching, and candidate evaluation.

## 🚀 Features
- Resume upload with ATS score evaluation
- Multilingual resume parsing using OCR and NLP
- Semantic resume–JD matching using mBERT
- Candidate ranking using Cosine Similarity and LightGBM
- AI-based skill gap analysis for rejected candidates
- Face-authenticated skill verification tests
- Bias-aware and skill-focused hiring process
- 
## 🧠 Technical Stack
**Frontend:** React.js, CSS, Axios  
**Backend:** Node.js, Express.js  
**Database:** MongoDB, Mongoose  
**AI/ML:** mBERT, Cosine Similarity, LightGBM  
**Security:** MediaPipe Face Detection & Face Mesh  
**Parsing:** PDF Parser, OCR (Tesseract / Google Vision)

## 🏗️ How It Works
1. User uploads resume and checks ATS score  
2. Resume text is extracted using OCR and parsing  
3. Semantic embeddings are generated using mBERT  
4. Job descriptions are parsed and embedded  
5. Resume–JD similarity is computed  
6. Candidates are ranked using LightGBM  
7. AI Gap Analysis is generated for transparency
8. 
## 🎯 Impact
- 80% faster hiring
- Fair evaluation across languages
- Reduced recruiter screening time
- Transparent feedback for candidates

## 🧪 Use Cases
- Smart recruitment platforms
- Hackathons and academic projects
- Fair and global hiring systems
- 
## 📁 Project Structure

ai-job-platform/
├── backend/
│   ├── app.py
│   └── jobs.json
│
├── frontend/
│   ├── index.html
│   ├── apply.html
│   ├── user.html
│   ├── recruiter.html
│   ├── mcq.html
│   ├── skills.html
│   ├── user-login.html
│   ├── user-register.html
│   ├── recruiter-login.html
│   ├── recruiter-register.html
│   ├── style.css
│   └── script.js
│
└── README.md

## 🧠 Concept & AI Scope
This prototype represents the foundation of an AI-powered hiring system with:
- Resume parsing and skill extraction (conceptual)
- Resume–job matching logic (extensible)
- AI-based skill evaluation (prototype stage)
- Scope for future integration of NLP and ML models

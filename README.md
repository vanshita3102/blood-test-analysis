# 🧪 Blood Test Analyser — Fixed & Enhanced  

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Redis](https://img.shields.io/badge/Redis-Queue-red?logo=redis)](https://redis.io/)

A **safe, fixed, and enhanced** version of the original debugging assignment.  
Analyzes **blood test PDFs**, runs a simple **rule-based analysis**, and supports **background jobs via Redis Queue (RQ)**.

## ✨ Features
- ✅ Fixed bugs from the original assignment
- ✅ Rule-based mock blood test analysis *(safe, non-medical)*
- ✅ Background task processing with **Redis Queue (RQ)**
- ✅ Clear API built with **FastAPI**
- ✅ Simple setup & usage

## 🐞 Bugs Fixed
1. **Unsafe CrewAI dependencies** → replaced with deterministic mock logic
2. **Direct PDF parsing issues** → fallback to `data/sample.pdf` included
3. **Blocking requests** → introduced **Redis Queue (RQ)** for async job handling

## 🚀 Quick Setup
```bash
git clone <your-repo-link>
cd debug-assignment-fixed
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

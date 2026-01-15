# Physics AI Learning Platform

A **full-stack, cloud-deployed Physics Learning Management System (LMS)** built with **Django**, featuring **AI-powered hints, anti-cheating exams, analytics, and admin control**.  

Designed for **high school Physics (IGCSE / A-Level / KCSE)** and is **scalable, production-ready, and ready to showcase to investors or students**.

---

## Features

### Admin / Superuser
- Add Physics topics
- Create exams (Mock, Pre-mock, Mini-mock)
- Upload multiple-choice questions with:
  - Correct answers
  - AI-style hints (Concept, Formula, Approach)
- Monitor student performance and analytics
- Track hint usage for each question

### Students
- Secure login
- Take timed exams online
- Anti-cheating protection:
  - Auto-submit on timeout
  - Tab-switch detection
  - Copy/paste disabled
- Access AI-powered hints without revealing answers
- View topic-level performance analytics

### AI-Powered Hint System
- Multi-level hints:
  1. Concept reminder
  2. Relevant formula
  3. Problem-solving approach
- Easily upgradeable to OpenAI / Gemini / Claude APIs in the future

### Analytics
- Detect weak topics automatically
- Track mistakes per topic
- Monitor hint usage per student

---

## Tech Stack

| Layer       | Technology                               |
|------------|------------------------------------------|
| Backend    | Django                                   |
| Database   | PostgreSQL (Production), SQLite (Local)  |
| Frontend   | Django Templates + Tailwind CSS          |
| Deployment | Render                                    |
| Server     | Gunicorn                                  |
| Static     | WhiteNoise                                |

---

## Project Structure

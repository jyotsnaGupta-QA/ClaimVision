# 🚗 ClaimVision – Master Project Tracker

**Project Name:** ClaimVision – AI-Powered Vehicle Damage Assessment & Claim Intelligence

**Project Type:** Work Assignment

**Developer:** Jyotsna Gupta

**Technical Lead:** ChatGPT

**Project Start:** June 2026

**Current Version:** v0.4.0

**Current Sprint:** Sprint 4 – Phase 2

**Status:** Active Development

**Last Updated:** 26 June 2026

---

                    ClaimVision

        ┌──────────────────────────────┐
        │       Streamlit UI           │
        └──────────────┬───────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │        Service Layer         │
        └──────────────┬───────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │      Repository Layer        │
        └──────────────┬───────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │      SQLAlchemy ORM          │
        └──────────────┬───────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │      SQL Server Database     │
        └──────────────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │          AI Engine           │
        └──────────────────────────────┘
---

# 📚 Table of Contents

1. Project Objective
2. Technology Stack
3. Enterprise Architecture
4. Project Structure
5. Database Design
6. Sprint Progress
7. Current Sprint
8. AI Pipeline
9. Coding Standards
10. Testing Status
11. Version History
12. Development Roadmap
---

# 📌 Project Objective

Develop an enterprise-grade AI-powered vehicle damage assessment and insurance claim management system.

The application should allow users to:

* Register insurance claims
* Upload multiple vehicle damage images
* Perform AI-based damage assessment
* Estimate repair cost
* Detect fraudulent claims
* Generate repair recommendations
* Manage complete claim history

---

# 🛠 Technology Stack

| Component        | Technology                   |
| ---------------- | ---------------------------- |
| Language         | Python 3.13                  |
| UI               | Streamlit                    |
| Database         | SQL Server 2022 Express      |
| ORM              | SQLAlchemy                   |
| Database Driver  | PyODBC                       |
| Image Processing | OpenCV (Sprint 4)            |
| IDE              | VS Code                      |
| Database Tool    | SQL Server Management Studio |

---

# 🏗 Enterprise Architecture

```
Streamlit UI

↓

Service Layer

↓

Repository Layer

↓

SQLAlchemy ORM

↓

SQL Server

↓

AI Engine
```

---

# 📁 Final Project Structure

```
ClaimVision/

│
├── ai/
│   ├── __init__.py
│   ├── image_processor.py
│   ├── damage_detector.py
│   ├── cost_estimator.py
│   ├── fraud_detector.py
│   └── recommendation_engine.py
│
├── config/
│
├── database/
│   ├── db.py
│   ├── models.py
│   └── repository.py
│
├── docs/
│
├── sample_data/
│
├── services/
│   └── claim_service.py
│
├── tests/
│
├── ui/
│   ├── dashboard.py
│   ├── claim_form.py
│   ├── image_upload.py
│   └── login.py
│
├── uploads/
│
├── utils/
│
├── app.py
├── requirements.txt
├── README.md
└── ClaimVision_Master_Tracker.md
```

---

# 🗄 Database

## Database Name

```
ClaimVisionDB
```

### Tables

### Customers

* CustomerId
* FullName
* Email
* PhoneNumber
* CreatedDate

---

### Vehicle

* VehicleId
* CustomerId
* VehicleNumber
* VehicleBrand
* VehicleModel
* VehicleYear
* InsurancePolicyNumber

---

### Claims

* ClaimId
* CustomerId
* VehicleId
* AccidentDate
* AccidentLocation
* Description
* Status
* CreatedDate

---

### UploadedImages

* ImageId
* ClaimId
* ImagePath
* UploadedDate

---

### DamageAssessment

* AssessmentId
* ClaimId
* DamageType
* Severity
* EstimatedCost
* FraudScore
* Recommendation
* Confidence

---

# 📅 Sprint Progress

## ✅ Sprint 1 – Environment & Database

### Environment

* [x] Project Structure
* [x] Virtual Environment
* [x] Dependencies Installed
* [x] SQL Server Configured
* [x] VS Code Configured

### Database

* [x] ClaimVisionDB Created
* [x] Customers Table
* [x] Vehicle Table
* [x] Claims Table
* [x] UploadedImages Table
* [x] DamageAssessment Table

### SQLAlchemy

* [x] Database Connection
* [x] Base Model
* [x] SessionLocal
* [x] Connection Tested

### Repository

* [x] Repository Pattern
* [x] Customer Repository
* [x] Vehicle Repository
* [x] Claim Repository

### Service Layer

* [x] ClaimService Implemented

# 📖 Lessons Learned -- Sprint 1

- SQLAlchemy ORM basics
- Repository Pattern
- Database Design

---

## ✅ Sprint 2 – Claim Management

### Dashboard

* [x] Dashboard UI
* [x] Professional Layout
* [x] Metrics Cards
* [x] Navigation

### Claim Form

* [x] Customer Details
* [x] Vehicle Details
* [x] Accident Details

### Claim Submission

* [x] Customer Saved
* [x] Vehicle Saved
* [x] Claim Saved
* [x] Claim ID Generated

### Workflow

```
Dashboard

↓

Claim Form

↓

SQL Server

↓

Claim Created
```
# 📖 Lessons Learned -- Sprint 2

- Service Layer
- Streamlit Navigation
- Session State
---

## ✅ Sprint 3 – Image Management

### Navigation Refactoring

* [x] Single Navigation System
* [x] Session State Cleanup
* [x] Enterprise Routing
* [x] Dashboard Refactored

### Image Upload

* [x] Multiple Image Upload
* [x] Image Preview
* [x] Upload Validation
* [x] Save Images to uploads Folder
* [x] UUID File Naming

### Database

* [x] Save Image Path
* [x] Link Images to Claim
* [x] UploadedImages Table Updated

### Service Layer

* [x] upload_image()
* [x] save_uploaded_image()

### Repository

* [x] create_uploaded_image()

### End-to-End Workflow

```
Dashboard

↓

Start New Claim

↓

Claim Form

↓

Claim Created

↓

Upload Images

↓

Images Saved

↓

UploadedImages Table
```

### Testing

* [x] Claim Creation
* [x] Database Verification
* [x] Multiple Image Upload
* [x] Image Storage
* [x] Image Path Storage
* [x] Navigation Verified

---

# 📦 Project Version

Current Version

v0.4.0

Release Name

AI Foundation Release

# 📊 Current Progress

██████████████████████████████░░

75% Completed

# 📖 Lessons Learned -- Sprint 3

- File Upload
- Image Storage
- UUID Naming

---

# 🚀 Current Sprint

## Sprint 4 – AI Damage Detection

Status

🔄 In Progress

Current Phase

Phase 1 – Image Processing Completed

---

# 📋 Sprint 4 Tasks

## Image Processing

- [x] AI Module Created
- [x] OpenCV Installed
- [x] AI Folder Structure Created
- [x] ImageProcessor Class Implemented
- [x] Image Loading
- [x] Image Validation
- [x] Image Resize
- [x] RGB Conversion
- [x] Grayscale Conversion
- [x] Gaussian Blur
- [x] Complete preprocess() Pipeline
- [x] Image Saving Support
- [x] Sample Dataset Created
- [x] Unit Test Created
- [x] Pytest Configured
- [x] Image Processing Successfully Tested

---

## AI Infrastructure

- [x] AI Package Created
- [x] OpenCV Successfully Installed
- [x] Sample Dataset Created
- [x] Test Framework Established
- [x] AI Folder Structure Finalized
- [x] Pytest Successfully Configured

---

## Damage Detection

- [ ] Edge Detection
- [ ] Contour Detection
- [ ] Scratch Detection
- [ ] Dent Detection
- [ ] Crack Detection
- [ ] Damage Region Highlighting

---

## AI Assessment

* [ ] Severity Prediction
* [ ] Confidence Score
* [ ] Damage Classification

---

## Repair Intelligence

* [ ] Repair Cost Estimation
* [ ] Fraud Detection
* [ ] Recommendation Engine

# 📖 Lessons Learned -- Sprint 4
- OpenCV
- Image Processing
- Pytest
- Computer Vision Fundamentals

---

# 📋 Sprint 5

### Dashboard

* [ ] Claim History
* [ ] Search Claims
* [ ] Dashboard Analytics

### Reports

* [ ] AI Assessment Report
* [ ] PDF Download
* [ ] Print Report

### Documentation

* [ ] README.md
* [ ] Architecture.md
* [ ] Database.md
* [ ] API Documentation

---

# 🎯 Current Workflow

```
Dashboard

↓

Create Claim

↓

Customer Saved

↓

Vehicle Saved

↓

Claim Saved

↓

Upload Images

↓

Images Stored

↓

Image Processor

↓

Preprocessed Images

↓

Ready for Damage Detection
```

---

# 🔜 Next Workflow

```
Vehicle Image

↓

Load Image

↓

Resize Image

↓

Convert to RGB

↓

Convert to Gray

↓

Noise Reduction

↓

Edge Detection

↓

Contour Detection

↓

Damage Detection

↓

Severity Analysis

↓

Repair Cost Estimation

↓

Fraud Detection

↓

Recommendation Engine

↓

AI Assessment Report
```

---

# 🧠 Future AI Workflow

```
Vehicle Damage Image

↓

Image Processor

↓

Image Enhancement

↓

Edge Detection

↓

Contour Detection

↓

Damage Detector

↓

Severity Analyzer

↓

Cost Estimator

↓

Fraud Detector

↓

Recommendation Engine

↓

AI Assessment Report
```

# 🤖 AI Processing Pipeline

```text
Vehicle Image

↓

Image Loading

↓

Resize

↓

RGB Conversion

↓

Grayscale

↓

Gaussian Blur

↓

Edge Detection

↓

Contour Detection

↓

Damage Detection

↓

Severity Analysis

↓

Repair Cost Estimation

↓

Fraud Detection

↓

Recommendation Engine

↓

AI Assessment Report
```
---

# 📝 Coding Standards

* UI contains only Streamlit code.
* Business logic resides in the Service Layer.
* Database logic resides in the Repository Layer.
* SQLAlchemy handles ORM operations.
* No SQL inside UI.
* No business logic inside UI.
* Enterprise layered architecture.
* Single navigation system using Streamlit Session State.

---

# 🐞 Issues Resolved

- Python Import Issues
- SQLAlchemy Connection Issues
- Repository Pattern Integration
- Streamlit Navigation Refactoring
- Session State Management
- Image Upload Workflow
- Image Storage Integration
- End-to-End Claim Workflow
- Python Package Import Resolution
- AI Project Structure
- OpenCV Installation
- Image Processing Pipeline
- Image Validation
- Pytest Configuration
- Cross-platform Path Handling

---

# 🧪 Testing Status

## Completed

- [x] Database Connectivity
- [x] Claim Creation
- [x] Image Upload
- [x] Image Storage
- [x] Image Processor
- [x] Image Processing Pipeline
- [x] Unit Testing
- [x] Pytest Configuration

## Pending

- [ ] Edge Detection
- [ ] Contour Detection
- [ ] Damage Detector
- [ ] Cost Estimator
- [ ] Fraud Detector
- [ ] Recommendation Engine

---

# 💡 Future Improvements

## Application

- User Authentication
- Customer Login
- Admin Dashboard
- Role-Based Access
- Claim History
- Dashboard Analytics

## AI

- Deep Learning Model Integration
- YOLO Object Detection
- Damage Segmentation
- AI Confidence Scoring
- AI Heat Maps

## Infrastructure

- FastAPI REST APIs
- Docker Support
- Logging
- Audit Trail
- Cloud Storage
- Azure Deployment

## Quality

- Unit Testing
- Integration Testing
- Performance Testing
- CI/CD Pipeline

---

# 📅 Current Milestone

## ✅ Sprint 4 – Phase 1 Completed

Achievements

- Enterprise AI Folder Structure
- OpenCV Successfully Integrated
- ImageProcessor Class Implemented
- Complete Image Preprocessing Pipeline
- Image Validation
- Gaussian Blur
- RGB & Grayscale Conversion
- Sample Dataset Created
- Unit Testing with Pytest
- Enterprise Project Structure Maintained

Current Progress

Sprint 4 – Phase 2

➡️ Edge Detection & Contour Analysis

---

# 🚀 Next Milestone

Sprint 4

AI-Powered Vehicle Damage Detection using OpenCV

# 📈 Sprint Summary

| Sprint | Status |
|---------|--------|
| Sprint 1 | ✅ Completed |
| Sprint 2 | ✅ Completed |
| Sprint 3 | ✅ Completed |
| Sprint 4 Phase 1 | ✅ Completed |
| Sprint 4 Phase 2 | 🔄 In Progress |
| Sprint 5 | ⏳ Pending |

Overall Progress

75%

# 📦 Version History

| Version | Description |
|----------|-------------|
| v0.1.0 | Database Foundation |
| v0.2.0 | Claim Management |
| v0.3.0 | Image Upload Workflow |
| v0.4.0 | AI Foundation |
| v0.5.0 | Damage Detection *(Planned)* |
| v0.6.0 | AI Assessment *(Planned)* |
| v1.0.0 | Production Release *(Target)* |

# 🚀 Development Roadmap

✅ Sprint 1
Environment & Database

✅ Sprint 2
Claim Management

✅ Sprint 3
Image Upload

🔄 Sprint 4
Computer Vision

⏳ Sprint 5
AI Assessment

⏳ Version 1.0
Production Release

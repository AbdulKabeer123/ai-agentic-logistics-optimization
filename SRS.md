## Software Requirements Specification (SRS)
Project: AI Agentic Logistics Optimization System
## 1. Introduction
### 1.1 Purpose

This document describes the functional and non-functional requirements for the AI Agentic Logistics Optimization System.

###  1.2 Scope

-The system will:
-Monitor multiple delivery vehicles
-Calculate dynamic ETA
-Consider weather and urban disruptions
-Compute freshness score
-Recommend best vehicle using AI logic
-Display real-time dashboard

## 2. Overall Description
### 2.1 System Perspective

The system consists of:

-Traffic Service Module
-Weather Service Module
-Urban Event Simulation
-Freshness Calculation Engine
-AI Decision Agent
-Streamlit Dashboard Interface

### 2.2 Product Functions

The system shall:

-Fetch real-time ETA using routing service
-Fetch real-time weather data
-Simulate urban disruptions
-Adjust ETA based on environmental factors
-Calculate freshness score
-Select best vehicle
-Display dashboard results

### 2.3 User Characteristics

The primary users are:

-Logistics Managers
-Delivery Coordinators
-Operations Supervisors
-Users require basic understanding of delivery operations.

## 3. Functional Requirements
### FR1: ETA Calculation

The system shall calculate ETA using routing service.

#### FR2: Weather Integration

The system shall adjust ETA based on weather conditions.

#### FR3: Urban Event Simulation

The system shall simulate protest and construction disruptions.

#### FR4: Freshness Calculation

The system shall calculate freshness score based on ETA and shelf-life.

#### FR5: AI Decision Engine

The system shall recommend the best vehicle based on freshness score.

#### FR6: Dashboard Interface

The system shall display:

-Vehicle ID
-ETA
-Weather
-Urban Event
-Freshness Score
-Best Vehicle Recommendation

## 4. Non-Functional Requirements
#### NFR1: Performance

The system shall refresh data every 15 seconds.

#### NFR2: Reliability

The system shall handle API failures gracefully.

#### NFR3: Usability

The dashboard shall provide clear visualization with color-coded freshness.

#### NFR4: Security

API keys shall be stored securely in environment variables.

## 5. System Architecture

The architecture consists of:

User → Streamlit UI → Fleet Module →
Traffic Service + Weather Service →
ETA Adjustment Engine →
AI Decision Agent → Dashboard Output


## 6. Assumptions & Constraints

-Internet connection required for API calls
-Weather and traffic APIs must be available
-Urban events are simulated, not real-time detected
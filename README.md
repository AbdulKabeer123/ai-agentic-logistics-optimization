# AI Agentic Logistics Optimization

A real-time logistics dashboard to dynamically route vehicles delivering perishable items in Karachi. It minimizes waste using AI-driven negotiation, ETA prediction, and freshness scoring.

## Features
- Real-time ETA for multiple vehicles
- Weather-adjusted delivery time
- Freshness score for perishable items
- Best vehicle highlighted
- Auto-refresh for live updates
- Color-coded freshness (Green/Yellow/Red)

## Installation

1. Clone the repo:
git clone https://github.com/AbdulKabeer123/ai-agentic-logistics-optimization.git

cd ai-agentic-logistics-optimization


2. Create virtual environment:
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows


3. Install dependencies:
pip install -r requirements.txt


4. Create `.env` file in project root:
ORS_API_KEY=YOUR_OPENROUTESERVICE_KEY
WEATHER_API_KEY=YOUR_OPENWEATHER_KEY
GROQ_API_KEY=YOUR_GROQ_API_KEY

5. Run the Streamlit app:
streamlit run main_streamlit.py

## Freshness Score Logic

Each vehicle’s cargo has a strict 3-hour (180 minutes) shelf-life window.

Freshness Score is calculated as:
Freshness (%) = max(0, (1 - ETA / 180) * 100)

1_ETA increases → Freshness decreases
2_Weather conditions impact ETA
3_Vehicles closer to expiration are deprioritized.

## Agentic Approach
This project uses a hybrid agentic decision system:
1_Deterministic scoring (ETA + Freshness)
2_LLM-based reasoning (Groq API)

The AI agent:
1_Evaluates fleet conditions
2_Recommends which vehicle to prioritize
3_Suggests rerouting if necessary
4_Explains reasoning in natural language
5_This ensures adaptive and intelligent logistics optimization.

## Real-Time Features
1--Auto-refresh every 15 seconds
2--Live ETA updates
3--Weather-aware routing
4--AI-generated recommendations
5--Color-coded freshness visualization

## Technologies Used
Python
Streamlit
OpenRouteService API
OpenWeather API
Groq LLM API
Pandas

## Project structure have to be like this
ai-agentic-logistics-optimization/
│
├── main_streamlit.py
├── services/
│   ├── multi_vehicle.py
│   ├── groq_agent.py
│   ├── weather_service.py
│   └── eta_service.py
├── utils/
│   └── freshness.py
├── .env
├── requirements.txt
└── README.md


## Author
Abdul Kabeer
AI Agentic Logistics Optimization Project
Pakistan
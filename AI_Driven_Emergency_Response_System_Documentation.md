# AI-Driven Emergency Response & Smart Dispatch System Documentation

## 1. Project Overview
This project is a comprehensive conceptual prototype for an **AI-Based Smart Policing and Emergency Dispatch System**, specifically modeled for the **Delhi NCR** region. 
The system aims to modernize urban law enforcement by integrating:
1.  **Real-time Resource Tracking**: Monitoring police units across the city.
2.  **Strategic Infrastructure Management**: Utilizing city exit points and critical hubs for tactical advantages.
3.  **Automated Decision Logic**: A pre-defined "Crime Matrix" that determines the exact response protocol based on the severity of the incident.
4.  **AI-Powered Complaint Analysis**: Using Machine Learning (NLP) to understand and classify citizen complaints (in English/Hinglish) automatically.

---

## 2. System Architecture & Modules

### Module 1: Dynamic Resource Allocation (Officer Management)
The system maintains a real-time database of police assets to ensure the nearest and most appropriate unit is dispatched.
*   **Data Points**: Officer ID, Name, Rank (Constable, Sub-Inspector, DCP), and Real-time Location (Latitude/Longitude).
*   **Specialization**: Units are categorized by expertise such as *Traffic, Cyber Cell, Field Operations, and Investigation*.
*   **Visualization**: All units are plotted on an interactive **Folium Map**, allowing command center operators to see deployment density at a glance.

### Module 2: Strategic Infrastructure Grid
To control crime effectively, the system maps critical city infrastructure that plays a role in emergency containment and response.
*   **Toll Plazas (Exit Control)**: Critical for sealing the city during kidnappings or fugitive chases (e.g., DND Flyway, Gurgaon Border).
*   **Transport Hubs**: High-traffic areas like *ISBT Anand Vihar* and *New Delhi Railway Station* where suspects might flee.
*   **Hospitals**: Mapped to ensure rapid medical response for accidents or violent crimes (e.g., AIIMS, Safdarjung).
*   **Metro Stations**: Key transit points for crowd control.

### Module 3: The Crime Logic Matrix (The "Brain")
This is the core rule engine that dictates how the system responds to different threats. It removes human hesitation by providing instant Standard Operating Procedures (SOPs).

| Crime Type | Priority | Response Radius | Dispatch Units | Protocol / Action |
| :--- | :--- | :--- | :--- | :--- |
| **Terrorist Threat** | Critical | 30 km | Anti-Terror Squad, Army Liaison | City Lockdown & Jammer Activation |
| **Kidnapping** | Critical | 20 km | Toll Plazas, Crime Branch, PCR | **Seal Exit Points** & Vehicle Tracking |
| **Armed Robbery** | Critical | 10 km | SWAT, Checkpoints, Nearest PCRs | Perimeter Cordon & CCTV Matching |
| **Murder** | High | 8 km | Forensics, Investigation Dept | Crime Scene Preservation |
| **accident** | High | 5 km | Ambulance, Traffic Police | **Green Corridor** for Hospital Transport |
| **Chain Snatching** | Medium | 4 km | Bike Squads | Naka Bandi at Intersections |

### Module 4: Intelligent Response Workflows
The system features specialized workflows that trigger automatically based on the crime type:
*   **The "City Lockdown" Protocol (Kidnapping)**: 
    *   If a kidnapping is detected, the system **automatically alerts all Toll Plazas and Border Checkpoints**.
    *   Instruction: "Check all White Vans / Suspicious Vehicles."
    *   Goal: Prevent the suspect from leaving the city jurisdiction.
*   **The "Medical Alert" Protocol**:
    *   If the crime involves physical harm (e.g., *Serious Accident, Stabbing, Mob Violence*), the system bypasses standard checks and **immediately alerts the nearest Hospital**.
    *   Instruction: "Prepare Trauma Team / ICU."

### Module 5: AI-Powered Complaint Classifier (NLP)
To handle the volume of incoming calls/messages, the system uses an AI model to understand the nature of the emergency.
*   **Technology**: Uses **TF-IDF Vectorization** (N-grams) and a **Random Forest Classifier**.
*   **Capability**: Can understand mixed-language text (**Hinglish** + English).
    *   *Input Example*: "Kisine goli maar di hai padosi ko" -> *Detected*: **Murder**
    *   *Input Example*: "Bacha park se gayab hai" -> *Detected*: **Kidnapping**
*   **Training Data**: The model is trained on synthetic templates covering scenarios like *Kidnapping, Road Accidents, Armed Robbery, Cyber Crime, and Murder*.

---

## 3. Technology Stack
*   **Language**: Python
*   **Data Manipulation**: Pandas (for structured datasets of officers and infrastructure).
*   **Geospatial Visualization**: Folium (Leaflet.js wrapper) for interactive map dashboards.
*   **Machine Learning**: Scikit-Learn (Random Forest, TfidfVectorizer) for Natural Language Processing.
*   **Persistence**: Joblib (for saving/loading trained AI models).

## 4. Operational Workflow (User Journey)
1.  **Incident Reporting**: A user submits a complaint via text (e.g., "Armed men entered the shop").
2.  **AI Classification**: The NLP model analyzes the text and predicts the crime type (e.g., *Armed Robbery*).
3.  **Logic Lookup**: The system queries the **Crime Matrix** for the *Armed Robbery* protocol.
4.  **Strategic Alert**: 
    *   Prioritizes the event as **Critical**.
    *   Identifies the **Response Radius** (10 km).
    *   Selects the **Response Units** (SWAT, PCR).
5.  **Dispatch & Visualization**: The system prints the dispatch orders and updates the tactical map to show the incident and nearby resources.

---

## 5. Future Enhancements
*   **Live GPS Integration**: Connecting to real-world police GPS APIs for dynamic routing.
*   **Traffic Integration**: Using Google Maps API to calculate the fastest route for ambulances/PCR vans.
*   **Voice-to-Text**: Integrating Whisper AI to handle emergency voice calls directly.

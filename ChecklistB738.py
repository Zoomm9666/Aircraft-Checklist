# ChecklistB738.py

checklists = {
    "Preflight checklist": [
        {"task": "Oxygen", "response": "Checked"},
        {"task": "Nav switches", "response": "Normal"},
        {"task": "Altimeters", "response": "Set"},
        {"task": "Window heat", "response": "Auto"},
        {"task": "Fuel pumps", "response": "On"},
        {"task": "Engine start levers", "response": "Idle"},
        {"task": "Landing gear", "response": "Down"},
        {"task": "Beacon lights", "response": "On"},
        {"task": "Clearance", "response": "Received"}
    ],
    "Before Checklist": [
        {"task": "Push & Start clearance", "response": "Received"},
        {"task": "Fuel", "response": "____kgs, Pumps on"},
        {"task": "Windows & Doors", "response": "Locked"},
        {"task": "Mode Control Panel", "response": "v2__,heading__,altitude__"},
        {"task": "Take off speeds", "response": "v1__,VR__,V2__"},
        {"task": "Control Display Unit preflight", "response": "completed"},
        {"task": "Rudder and aileron trim", "response": "Free and zero"},
        {"task": "Taxi and Takeoff briefing", "response": "Completed"},
        {"task": "Anti-collision lights", "response": "On"}
    ],
    "Before Taxi Checklist": [
        {"task": "Generators", "response": "On"},
        {"task": "Probe heat", "response": "On"},
        {"task": "Anti ice", "response": "As required"},
        {"task": "Isolation valve", "response": "Auto, Closed required"},
        {"task": "Engine start switches", "response": "Сont"},
        {"task": "Pressurization", "response": "Packs on, flt auto"},
        {"task": "Autothrottle", "response": "Armed"},
        {"task": "Recall", "response": "Check"},
        {"task": "Autobrake", "response": "RTO"},
        {"task": "Engine start levers", "response": "Idle, Detent"},
        {"task": "Flight controls", "response": "Check"},
        {"task": "Ground equipment", "response": "Clear, hand signal"}
    ],
    "Before takeoff checklist": [
        {"task": "Flaps", "response": "5, Green light"},
        {"task": "Stabilizer trim", "response": "Units"}
    ],
    "After Takeoff Checklist": [
        {"task": "engine bleeds", "response": "on"},
        {"task": "packs", "response": "auto"},
        {"task": "landing gear", "response": "off"},
        {"task": "flaps", "response": "up, no lights"}
    ],
    "Descent Checklist": [
        {"task": "Pressurization", "response": "Land alt"},
        {"task": "Recall", "response": "Check"},
        {"task": "Autobrake", "response": "Set 2"},
        {"task": "Landing data", "response": "Vref__,Minimums__"},
        {"task": "Approach briefing", "response": "Completed"}
    ],
    "Landing Checklist": [
        {"task": "Engine start switches", "response": "Continuous"},
        {"task": "Speedbrake", "response": "Armed"},
        {"task": "Landing gear", "response": "Down"},
        {"task": "flaps", "response": "full, green light"}
    ],
    "After Landing Checklist": [
        {"task": "landing lights", "response": "off"},
        {"task": "flaps", "response": "up"},
        {"task": "tcas", "response": "standby"}
    ],
    "Shutdown Checklist": [
        {"task": "Fuel pumps", "response": "Off"},
        {"task": "Probe heat", "response": "Off"},
        {"task": "Hydraulic panel", "response": "Set"},
        {"task": "Flaps", "response": "Up"},
        {"task": "Parking brake", "response": "Set no park"},
        {"task": "Engine start levers", "response": "Cut off"},
        {"task": "Weather radar", "response": "Off"}
    ],
    "Secure Checklist": [
        {"task": "IRS", "response": "Off"},
        {"task": "Emergency exit lights", "response": "Off"},
        {"task": "Window heat", "response": "Off"},
        {"task": "Packs", "response": "Off"}
    ]
}

# Example usage
if __name__ == "__main__":
    for phase, tasks in checklists.items():
        print(f"\n{phase.replace('_', ' ').capitalize()}:")
        for item in tasks:
            print(f"- {item['task'].ljust(30, '.')} {item['response']}")

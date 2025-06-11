# ChecklistA320.py

checklists = {
    "Before Start checklist": [
        {"task": "Cockpit preparation", "response": "Complete (both)"},
        {"task": "Gear pins and covers", "response": "Removed"},
        {"task": "Signs", "response": "On / Auto"},
        {"task": "ADIRS", "response": "NAV"},
        {"task": "Fuel quantity", "response": "____ kg / Balanced"},
        {"task": "TO data", "response": "Set"},
        {"task": "Baro ref", "response": "Set"},
        {"task": "Windows & doors", "response": "Closed / Armed (both)"},
        {"task": "Beacon", "response": "On"},
        {"task": "Thrust levers", "response": "Idle"},
        {"task": "Parking brake", "response": "Set"}
    ],
    "After Start checklist": [
        {"task": "Anti-ice", "response": "As required"},
        {"task": "ECAM status", "response": "Checked"},
        {"task": "Pitch trim", "response": "____ % Set"},
        {"task": "Rudder trim", "response": "Zero"}
    ],
    "Before Takeoff checklist": [
        {"task": "Flight controls", "response": "Checked (both)"},
        {"task": "Flight instruments", "response": "Checked (both)"},
        {"task": "Briefing", "response": "Confirmed"},
        {"task": "Flaps setting", "response": "CONF____ (both)"},
        {"task": "FMA takeoff data", "response": "Read (PF) Checked (PNF)"},
        {"task": "Transponder", "response": "Set"},
        {"task": "ECAM memo", "response": "Takeoff no blue"},
        {"task": "Cabin", "response": "Secured for takeoff"},
        {"task": "Engine mode selector", "response": "As required"},
        {"task": "TCAS", "response": "____ TA / RA"},
        {"task": "Packs", "response": "As required"}
    ],
    "After Takeoff checklist": [
        {"task": "Landing gear", "response": "Up"},
        {"task": "Flaps", "response": "Retracted"},
        {"task": "Packs", "response": "On"},
        {"task": "Baro ref", "response": "Standard set"}
    ],
    "Approach checklist": [
        {"task": "Briefing", "response": "Confirmed"},
        {"task": "ECAM status", "response": "Checked"},
        {"task": "Seat belts", "response": "On"},
        {"task": "Baro ref", "response": "Set"},
        {"task": "MDA/DH", "response": "Set (both)"},
        {"task": "Engine mode selector", "response": "As required"}
    ],
    "Landing checklist": [
        {"task": "Cabin", "response": "Secured for landing"},
        {"task": "A/THR", "response": "Speed / Off"},
        {"task": "Go-around altitude", "response": "____ ft Set"},
        {"task": "ECAM memo", "response": "LDG no blue"},
        {"task": "Landing gear down", "response": "Signs on"},
        {"task": "Spoilers arm", "response": "Flaps set"}
    ],
    "Parking checklist": [
        {"task": "APU bleed", "response": "As required"},
        {"task": "Yellow electric pump", "response": "Off"},
        {"task": "Engines", "response": "Off"},
        {"task": "Seat belts", "response": "Off"},
        {"task": "Exterior lights", "response": "As required"},
        {"task": "Fuel pumps", "response": "Off"},
        {"task": "Parking brake & chocks", "response": "As required"},
        {"task": "Mobile phone", "response": "On"},
        {"task": "Transponder", "response": "STBY 2000"},
        {"task": "Radar/PWS", "response": "Off"},
        {"task": "Extract", "response": "OVRD"},
        {"task": "Consider heavy rain", "response": "True"}
    ],
    "Securing  checklist": [
        {"task": "ADIRS", "response": "Off"},
        {"task": "Oxygen", "response": "Off"},
        {"task": "APU bleed", "response": "Off"},
        {"task": "Emergency exit lights", "response": "Off"},
        {"task": "No smoking", "response": "Off"},
        {"task": "APU & battery", "response": "Off"},
        {"task": "Consider cold weather", "response": "True"}
    ]
}

# Example usage
if __name__ == "__main__":
    for phase, tasks in checklists.items():
        print(f"\n{phase}:")
        for item in tasks:
            print(f"- {item['task'].ljust(30, '.')} {item['response']}")

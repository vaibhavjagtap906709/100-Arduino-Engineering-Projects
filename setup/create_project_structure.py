#!/usr/bin/env python3
"""
Script to create complete directory structure for 100 Arduino Engineering Projects
Run this script to generate all project folders locally, then push to GitHub
"""

import os
import json
from pathlib import Path

# Project data with metadata
PROJECTS = [
    {"id": 1, "name": "Smart Irrigation", "category": "Smart Agriculture"},
    {"id": 2, "name": "Predictive Maintenance", "category": "Industrial Automation"},
    {"id": 3, "name": "Glucose Monitor", "category": "Healthcare"},
    {"id": 4, "name": "Line Following Robot", "category": "Robotics"},
    {"id": 5, "name": "Solar Microgrid", "category": "Renewable Energy"},
    # ... Continue for projects 6-100 (see PROJECTS_INDEX.md for full list)
]

BASE_DIR = Path("Projects")
SUBDIRS = [
    "ArduinoCode",
    "CircuitDiagram",
    "Documentation",
    "Images",
    "Datasheets",
    "Components"
]

TEMPLATE_README = """
# Project {id:02d}: {name}

## Category
{category}

## Difficulty
Intermediate to Advanced

## GitHub Repository
arduino-{slug}

## Problem Statement
[Describe the problem this project solves]

## Objectives
- Objective 1
- Objective 2
- Objective 3

## Key Components
- Arduino Board
- Sensors/Actuators
- Communication Modules

## Estimated Cost
₹[Cost in INR]

## Key Features
- Feature 1
- Feature 2
- Feature 3

## Directory Structure
- **ArduinoCode/** - Main Arduino sketch and supporting code
- **CircuitDiagram/** - Circuit schematics and PCB layouts
- **Documentation/** - Technical reports and specifications
- **Images/** - Photos and demonstration videos
- **Datasheets/** - Component datasheets
- **Components/** - Bill of Materials (BOM)

## Documentation
Refer to parent PROJECTS_INDEX.md for complete project list.
"""

TEMPLATE_INO = """
/*
  Arduino Code Template - Project {id:02d}: {name}
  Category: {category}
  Version: 1.0
  
  Complete code implementation goes here.
  Each project includes:
  - Sensor initialization
  - Main loop implementation
  - Data processing logic
  - Wireless/Cloud integration
  - Safety checks and error handling
*/

// ===== LIBRARIES =====
// Include all necessary libraries

// ===== PIN DEFINITIONS =====
// Define all hardware connections

// ===== CONSTANTS =====
// Define operational parameters

// ===== GLOBAL VARIABLES =====
// State management variables

// ===== SETUP =====
void setup() {{
  Serial.begin(9600);
  // Initialize sensors, pins, modules
}}

// ===== MAIN LOOP =====
void loop() {{
  // Read sensors
  // Process data
  // Control outputs
  // Handle communication
}}

// ===== HELPER FUNCTIONS =====
// Additional functions for modular code
"""

TEMPLATE_BOM_JSON = """
{{
  "project": "{name}",
  "projectId": {id},
  "currency": "INR",
  "estimatedTotal": 0,
  "components": [
    {{
      "id": 1,
      "name": "Arduino Board",
      "quantity": 1,
      "unitPrice": 500,
      "totalPrice": 500,
      "notes": "Main microcontroller"
    }}
  ]
}}
"""

def create_project_structure():
    """
    Create directory structure for all 100 projects
    """
    for project in PROJECTS:
        project_dir = BASE_DIR / f"{{project['id']:02d}}_{project['name'].replace(' ', '_')}"
        
        # Create main project directory
        project_dir.mkdir(parents=True, exist_ok=True)
        
        # Create subdirectories
        for subdir in SUBDIRS:
            (project_dir / subdir).mkdir(exist_ok=True)
        
        # Create README.md
        slug = project['name'].lower().replace(' ', '-')
        readme_content = TEMPLATE_README.format(
            id=project['id'],
            name=project['name'],
            category=project['category'],
            slug=slug
        )
        (project_dir / "README.md").write_text(readme_content)
        
        # Create main.ino
        ino_content = TEMPLATE_INO.format(
            id=project['id'],
            name=project['name'],
            category=project['category']
        )
        (project_dir / "ArduinoCode" / "main.ino").write_text(ino_content)
        
        # Create BOM.json
        bom_content = TEMPLATE_BOM_JSON.format(
            name=project['name'],
            id=project['id']
        )
        (project_dir / "Components" / "BOM.json").write_text(bom_content)
        
        # Create .gitkeep files to preserve empty directories
        for subdir in SUBDIRS:
            (project_dir / subdir / ".gitkeep").touch()
        
        print(f"✓ Created project {project['id']:02d}: {project['name']}")

if __name__ == "__main__":
    print("Creating directory structure for 100 Arduino projects...")
    create_project_structure()
    print("\n✓ All project directories created successfully!")
    print("Next steps:")
    print("1. Fill in project details in each README.md")
    print("2. Add Arduino code to ArduinoCode/ folders")
    print("3. Add circuit diagrams to CircuitDiagram/ folders")
    print("4. Update component lists in BOM.json")
    print("5. Commit and push to GitHub")

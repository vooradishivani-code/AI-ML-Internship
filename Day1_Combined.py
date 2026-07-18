#!/usr/bin/env python3
"""
AI & ML Internship Program - Day 1
A comprehensive introduction to Python basics and AI/ML concepts
"""

# ============================================================================
# 1. GREETING AND BASIC OUTPUT
# ============================================================================
print("=" * 60)
print("Welcome to the AI & ML Internship Program!")
print("=" * 60)
print()

# ============================================================================
# 2. VARIABLES AND DATA TYPES
# ============================================================================
print("--- Variables and Data Types ---")
internship_name = "AI & ML Internship"
duration_weeks = 12
is_active = True
participants = 25
completion_rate = 0.95

print(f"Program: {internship_name}")
print(f"Duration: {duration_weeks} weeks")
print(f"Active: {is_active}")
print(f"Participants: {participants}")
print(f"Completion Rate: {completion_rate * 100}%")
print()

# ============================================================================
# 3. LISTS AND BASIC OPERATIONS
# ============================================================================
print("--- Topics Covered ---")
topics = ["Python Basics", "Data Science", "Machine Learning", "Deep Learning", "NLP"]
for i, topic in enumerate(topics, 1):
    print(f"{i}. {topic}")
print()

# ============================================================================
# 4. DICTIONARIES
# ============================================================================
print("--- Internship Details ---")
internship_info = {
    "start_date": "January 2026",
    "end_date": "March 2026",
    "level": "Beginner to Intermediate",
    "mentors": 5,
    "projects": 3
}

for key, value in internship_info.items():
    print(f"{key.replace('_', ' ').title()}: {value}")
print()

# ============================================================================
# 5. FUNCTIONS
# ============================================================================
print("--- Custom Functions ---")

def calculate_progress(current_week, total_weeks):
    """Calculate internship progress percentage"""
    return (current_week / total_weeks) * 100

def get_level_description(level):
    """Return description based on level"""
    levels = {
        "Beginner": "Just starting your AI/ML journey",
        "Intermediate": "Building practical skills",
        "Advanced": "Ready for real-world projects"
    }
    return levels.get(level, "Unknown level")

current_week = 1
progress = calculate_progress(current_week, duration_weeks)
level_desc = get_level_description(internship_info["level"].split()[0])

print(f"Progress (Week {current_week}/{duration_weeks}): {progress:.1f}%")
print(f"Level Description: {level_desc}")
print()

# ============================================================================
# 6. LOOPS AND CONDITIONALS
# ============================================================================
print("--- Weekly Progress Status ---")
for week in range(1, 4):
    if week == 1:
        status = "Foundation"
    elif week <= 2:
        status = "Building"
    else:
        status = "Advancing"
    print(f"Week {week}: {status}")
print()

# ============================================================================
# 7. SUMMARY
# ============================================================================
print("=" * 60)
print("Get ready to explore the world of AI and Machine Learning!")
print("Let's make this internship an amazing learning experience!")
print("=" * 60)

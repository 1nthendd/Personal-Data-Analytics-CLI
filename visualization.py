"""
Visualization module for Personal Productivity Manager.
"""

import matplotlib.pyplot as plt


def plot_study_vs_mood(rows):
    """Create a scatter plot showing correlation between study hours and mood.
    """
    study_values = [row['study_hours'] for row in rows]
    mood_values = [row['mood'] for row in rows]
    plt.figure(figsize=(10, 6))
    plt.scatter(study_values, mood_values, s=80, alpha=0.7, color='#3498db')
    plt.grid(alpha=0.3)
    plt.title("Study Hours vs Mood Correlation", fontsize=14, fontweight='bold')
    plt.xlabel("Study Hours", fontsize=12)
    plt.ylabel("Mood Rating (1-10)", fontsize=12)
    plt.tight_layout()
    plt.show()
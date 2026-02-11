"""
Analytics module for Personal Productivity Manager.
"""
import math

def total_study_time(rows):
    """Calculate total study hours from dataset.
    """
    if not rows:
        return 0
    return sum(row['study_hours'] for row in rows)


def average_study_hours(rows):
    """Calculate average study hours from dataset.
    """
    if not rows:
        return 0
    total = total_study_time(rows)
    average = total / len(rows)
    return average


def best_study_day(rows):
    """Find best study day from dataset.
    """
    if not rows:
        return None
    best_day = max(rows, key=lambda x: x['study_hours'])
    return best_day['date'], best_day['study_hours']
    

def average_mood(rows):
    """Calculate average mood from dataset.
    """
    if not rows:
        return 0
    total = sum(row['mood'] for row in rows)
    return total / len(rows)


def correlation(rows):
    """Calculate Pearson correlation between study hours and mood.
    """
    if len(rows) < 2:
        return 0
    avg_study = average_study_hours(rows)
    avg_mood = average_mood(rows)
    numerator = 0
    sum_x_sq = 0
    sum_y_sq = 0
    for row in rows:
        x = row['study_hours'] 
        y = row['mood']        
        numerator += (x-avg_study)*(y-avg_mood)
        sum_x_sq += (x - avg_study) ** 2
        sum_y_sq += (y - avg_mood) ** 2
    if sum_x_sq == 0 or sum_y_sq == 0:
        return 0
    return numerator / (math.sqrt(sum_x_sq) * math.sqrt(sum_y_sq))
        


import urllib.request
import json


def retrieve_all():
    active_courses = []
    data = urllib.request.urlopen(
        "https://studies.cs.helsinki.fi/stats-mock/api/courses").read()
    courses = json.loads(data)
    for course in courses:
        course_name = course["fullName"]
        course_code = course["name"]
        year = course["year"]
        total_exercises = sum(course["exercises"])
        if course["enabled"] == True:
            active_courses.append(
                (course_name, course_code, year, total_exercises))
    return active_courses


def retrieve_course(course_name: str):
    course_data = urllib.request.urlopen(
        f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats").read()
    data = json.loads(course_data)
    total_weeks = len(data)
    max_students = 0
    total_hours = 0
    total_exercises = 0

    for week_data in data.values():
        if week_data["students"] > max_students:
            max_students = week_data["students"]
        total_hours += week_data["hour_total"]
        total_exercises += week_data["exercise_total"]

    average_hours = int(total_hours / max_students)
    average_exercises = int(total_exercises / max_students)

    result = {
        'weeks': total_weeks,
        'students': max_students,
        'hours': total_hours,
        'hours_average': average_hours,
        'exercises': total_exercises,
        'exercises_average': average_exercises
    }

    return result

import datetime


class FitnessTracker:
    def __init__(self, user_name):
        self.user_name = user_name
        self.daily_activity = {}
        self.goal = {"steps": 10000, "distance": 5, "calories": 2000}  # default goals

    def log_activity(self, date, steps, distance, calories):
        self.daily_activity[date] = {"steps": steps, "distance": distance, "calories": calories}

    def set_goals(self, steps=None, distance=None, calories=None):
        if steps: self.goal['steps'] = steps
        if distance: self.goal['distance'] = distance
        if calories: self.goal['calories'] = calories
        print(
            f"Goals set: Steps - {self.goal['steps']}, Distance - {self.goal['distance']} km, Calories - {self.goal['calories']}")

    def generate_report(self, period='weekly'):
        total_steps, total_distance, total_calories = 0, 0, 0
        count = len(self.daily_activity)

        for day, activity in self.daily_activity.items():
            total_steps += activity["steps"]
            total_distance += activity["distance"]
            total_calories += activity["calories"]

        avg_steps = total_steps // count if count else 0
        avg_distance = total_distance / count if count else 0
        avg_calories = total_calories // count if count else 0

        print(f"\n{period.capitalize()} Report:")
        print(f"Average Steps: {avg_steps}")
        print(f"Average Distance: {avg_distance} km")
        print(f"Average Calories: {avg_calories}\n")


# Example usage
tracker = FitnessTracker("Alice")
tracker.log_activity(datetime.date(2024, 11, 13), 12000, 7.5, 2500)
tracker.log_activity(datetime.date(2024, 11, 14), 8500, 4.2, 1800)
tracker.set_goals(12000, 6, 2200)
tracker.generate_report()

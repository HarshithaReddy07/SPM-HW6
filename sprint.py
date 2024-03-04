class SprintVelocityCalculator:
    """
    A class to calculate the sprint velocity based on completed sprint points.
    """
    def __init__(self):
        # Initializes with an empty list to store sprint points.
        self.points_list = []

    def collect_sprint_points(self):
        """
        Collects sprint points from user input, separated by commas.
        Converts the input string into a list of integers.
        """
        points_input = input("Enter sprint points separated by commas: ")
        self.points_list = [int(point.strip()) for point in points_input.split(',')]

    def calculate_average_velocity(self):
        """
        Calculates the average sprint velocity based on the completed sprint points.
        """
        return sum(self.points_list) / len(self.points_list) if self.points_list else 0

    def display_average_velocity(self):
        """
        Displays the average sprint velocity to the user.
        """
        average_velocity = self.calculate_average_velocity()
        print(f"Average Sprint Velocity: {average_velocity}")


class TeamCapacityCalculator:
    """
    A class to calculate the team effort-hour capacity based on team member details.
    """
    def __init__(self, sprint_days):
        # Initializes with an empty list to store team member details.
        self.team_data = []
        self.sprint_days = sprint_days

    def collect_team_capacity_data(self):
        """
        Collects team member details such as daily hours, PTO hours, and hours committed to ceremonies.
        """
        number_of_team_members = int(input("Enter the number of team members: "))
        for i in range(1, number_of_team_members + 1):
            member_data = {}
            print(f"\nTeam Member {i}:")
            member_data['daily_hours'] = int(input("Enter daily available hours: "))
            member_data['pto_hours'] = int(input("Enter PTO hours: "))
            member_data['ceremony_hours'] = int(input("Enter hours committed to ceremonies: "))
            self.team_data.append(member_data)

    def calculate_individual_effort_hours(self):
        """
        Calculates the available effort-hours for each team member based on sprint days, PTO, and ceremony hours.
        """
        individual_efforts = []
        for member in self.team_data:
            available_hours = member['daily_hours'] * (self.sprint_days - member['pto_hours'] - member['ceremony_hours'])
            individual_efforts.append(available_hours)
        return individual_efforts

    def aggregate_team_effort_hours(self, individual_efforts):
        """
        Aggregates the effort-hours of all team members to calculate the total team effort-hours.
        """
        return sum(individual_efforts)

    def display_effort_hours(self):
        """
        Displays the individual effort-hours for each team member and the total team effort-hours.
        """
        individual_efforts = self.calculate_individual_effort_hours()
        total_effort = self.aggregate_team_effort_hours(individual_efforts)
        for index, effort in enumerate(individual_efforts, start=1):
            print(f"Individual Effort for member {index}: {effort} hours")
        print(f"Total Team Effort: {total_effort} hours")


def main():
    """
    Main function to orchestrate the execution of different features based on user input.
    """
    print("Select feature to run:")
    print("A: Calculate Sprint Velocity")
    print("B: Calculate Team Effort-Hour Capacity")
    choice = input("Enter your choice (A/B): ").upper()

    if choice == 'A':
        calculator = SprintVelocityCalculator()
        calculator.collect_sprint_points()
        calculator.display_average_velocity()
    elif choice == 'B':
        sprint_days = int(input("Enter the number of sprint days: "))
        calculator = TeamCapacityCalculator(sprint_days)
        calculator.collect_team_capacity_data()
        calculator.display_effort_hours()
    else:
        print("Invalid selection. Please choose either 'A' or 'B.'")


if __name__ == "__main__":
    main()

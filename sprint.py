class SprintVelocityCalculator:
    """
    Calculates and displays the average sprint velocity based on user-input sprint points.
    """
    def __init__(self):
        """
        Initializes the SprintVelocityCalculator with an empty list for sprint points.
        """
        self.points_list = []

    def collect_sprint_points(self):
        """
        Collects sprint points from the user, validating input to ensure only integers are entered.
        """
        print("Enter sprint points (one at a time, type 'done' to finish):")
        while True:
            input_point = input("> ")
            if input_point.lower() == 'done':
                break
            try:
                self.points_list.append(int(input_point))
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def calculate_average_velocity(self):
        """
        Calculates the average velocity from the collected sprint points.

        Returns:
            float: The average velocity, or 0 if no points were collected.
        """
        if not self.points_list:
            return 0
        return sum(self.points_list) / len(self.points_list)

    def display_average_velocity(self):
        """
        Displays the calculated average sprint velocity.
        """
        average_velocity = self.calculate_average_velocity()
        if average_velocity:
            print(f"Average Sprint Velocity: {average_velocity}")
        else:
            print("No sprint points were entered to calculate velocity.")


class TeamMember:
    """
    Represents a single team member, storing their availability and commitments.
    """
    def __init__(self, daily_hours, pto_hours, ceremony_hours):
        """
        Initializes a TeamMember with their daily available hours, PTO hours, and ceremony hours.

        Parameters:
            daily_hours (int): Daily available hours for the sprint.
            pto_hours (int): Hours taken off as PTO during the sprint.
            ceremony_hours (int): Hours committed to ceremonies during the sprint.
        """
        self.daily_hours = daily_hours
        self.pto_hours = pto_hours
        self.ceremony_hours = ceremony_hours


class TeamCapacityCalculator:
    """
    Calculates and displays the team's total capacity in effort-hours for a sprint.
    """
    def __init__(self, sprint_days):
        """
        Initializes the TeamCapacityCalculator with sprint duration and an empty list for team members.

        Parameters:
            sprint_days (int): The number of days in the sprint.
        """
        self.team_members = []
        self.sprint_days = sprint_days

    def collect_team_capacity_data(self):
        """
        Collects and validates team member data from user input.
        """
        print("\nEnter team member details (type 'done' when finished):")
        while True:
            try:
                daily_hours_input = input("Enter daily available hours (or type 'done' to finish): ")
                if daily_hours_input.lower() == 'done':
                    break
                daily_hours = int(daily_hours_input)
                pto_days = int(input("Enter PTO days this sprint: "))
                ceremony_hours = int(input("Enter hours committed to ceremonies: "))
                self.team_members.append(TeamMember(daily_hours, pto_days, ceremony_hours))
            except ValueError:
                print("Invalid input. Please enter valid numbers or 'done' to finish.")
            except EOFError:
                break  # Allows ending input in environments like interactive notebooks


    def calculate_team_capacity(self):
        """
        Calculates the total team capacity in effort-hours for the sprint.

        Returns:
            int: The total effort-hours available from all team members for the sprint.
        """
        total_capacity = sum(
            (member.daily_hours * (self.sprint_days - member.pto_hours) - member.ceremony_hours)
            for member in self.team_members
        )
        return total_capacity

    def display_team_capacity(self):
        """
        Displays the calculated team capacity.
        """
        total_capacity = self.calculate_team_capacity()
        print(f"Total Team Capacity: {total_capacity} effort-hours")


def main():
    """
    Main function to run the program.
    """
    print("Select feature to run:\nA: Calculate Sprint Velocity\nB: Calculate Team Capacity")
    choice = input("Enter your choice (A/B): ").upper()

    if choice == 'A':
        calculator = SprintVelocityCalculator()
        calculator.collect_sprint_points()
        calculator.display_average_velocity()
    elif choice == 'B':
        sprint_days = int(input("Enter the number of sprint days: "))
        calculator = TeamCapacityCalculator(sprint_days)
        calculator.collect_team_capacity_data()
        calculator.display_team_capacity()
    else:
        print("Invalid selection. Please choose either 'A' or 'B'.")

if __name__ == "__main__":
    main()

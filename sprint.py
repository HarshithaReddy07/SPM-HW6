class SprintVelocityCalculator:
    """
    A class to calculate the sprint velocity based on completed sprint points.
    """
    def _init_(self):
        # Initializes with an empty list to store sprint points.
        self.points_list = []

    def collect_sprint_points(self):
        """
        Collects sprint points from user input, separated by commas.
        Converts the string input into a list of integers.
        """
        points_input = input("Enter sprint points separated by commas: ")
        self.points_list = [int(point.strip()) for point in points_input.split(',')]

    def calculate_average_velocity(self):
        """
        Calculates the average sprint velocity.
        Returns the average of the points in points_list.
        """
        return sum(self.points_list) / len(self.points_list) if self.points_list else 0

    def display_average_velocity(self):
        """
        Displays the calculated average velocity of sprints to the user.
        """
        average_velocity = self.calculate_average_velocity()
        print(f"Average Sprint Velocity: {average_velocity}")

        
class TeamCapacityCalculator:
    """
    A class to calculate the team's capacity in effort-hours.
    """
    def __init__(self, sprint_days):
        # Initializes with an empty list to store team data and sprint days.
        self.team_data = []
        self.sprint_days = sprint_days

    def collect_team_capacity_data(self):
        """
        Collects capacity data for each team member, including daily hours, PTO, and ceremony hours.
        """
        number_of_team_members = int(input("Enter the number of team members: "))
        for i in range(number_of_team_members):
            print(f"Enter data for team member {i+1}:")
            daily_hours = int(input("Enter daily available hours for the team member: "))
            # Extend this part to collect PTO and ceremony hours as needed.
            self.team_data.append(daily_hours)
    
    def calculate_individual_effort_hours(self):
        """
        Calculates and returns a list of effort-hours for each team member.
        """
        return [hours * self.sprint_days for hours in self.team_data]
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
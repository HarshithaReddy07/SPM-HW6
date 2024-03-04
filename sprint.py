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


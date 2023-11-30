import math

# Define a class for the physics calculator
class PhysicsCalculator:
    def __init__(self):
        # Initialize the unit system variable
        self.unit_system = ""

    # Method to set the unit system (SI/US) based on user input
    def set_unit_system(self):
        while True:
            # Prompt user to choose the unit system
            unit_system = input("Choose unit system (SI/US): ").upper()
            # Check if the input is either SI or US, set the unit system, and break the loop
            if unit_system in ["SI", "US"]:
                self.unit_system = unit_system
                break
            else:
                # If the input is invalid, inform the user and continue the loop
                print("Invalid choice. Please enter SI or US.")

    # Method for kinematic equations calculation
    def kinematic_equation(self):
        print("\nKinematic Equations:")
        # Get user input for initial velocity, acceleration, and time
        initial_velocity = float(input("Enter initial velocity ({}/s): ".format(self.unit_system)))
        acceleration = float(input("Enter acceleration ({}/s^2): ".format(self.unit_system)))
        time = float(input("Enter time (s): "))

        # Calculate final velocity and displacement using kinematic equations
        final_velocity = initial_velocity + acceleration * time
        displacement = initial_velocity * time + 0.5 * acceleration * time**2

        # Display the results
        print("Final Velocity: {} {}/s".format(final_velocity, self.unit_system))
        print("Displacement: {} {}".format(displacement, self.unit_system))

    # Method for gravitational force calculation
    def gravitational_force(self):
        print("\nGravitational Force:")
        # Get user input for masses and distance
        mass1 = float(input("Enter mass of object 1 (kg): "))
        mass2 = float(input("Enter mass of object 2 (kg): "))
        distance = float(input("Enter distance between objects (m): "))

        # Calculate gravitational force using Newton's law of gravitation
        gravitational_constant = 6.674 * (10**-11)
        force = (gravitational_constant * mass1 * mass2) / distance**2

        # Display the result
        print("Gravitational Force: {} N".format(force))

    # Method for energy calculation
    def energy_calculation(self):
        print("\nEnergy Calculation:")
        # Get user input for mass and height
        mass = float(input("Enter mass (kg): "))
        height = float(input("Enter height (m): "))

        # Calculate gravitational potential energy and kinetic energy
        gravitational_potential_energy = mass * 9.8 * height
        kinetic_energy = 0.5 * mass * (9.8**2)

        # Display the results
        print("Gravitational Potential Energy: {} J".format(gravitational_potential_energy))
        print("Kinetic Energy: {} J".format(kinetic_energy))

    # Method to run the physics calculator
    def run_calculator(self):
        print("Physics Calculator")
        # Set the unit system at the beginning
        self.set_unit_system()

        # Main loop to repeatedly prompt the user for physics calculations
        while True:
            print("\nChoose a physics calculation:")
            print("1. Kinematic Equations")
            print("2. Gravitational Force")
            print("3. Energy Calculation")
            print("4. Exit")

            # Get user's choice
            choice = input("Enter your choice (1-4): ")

            # Perform the chosen physics calculation or exit the program
            if choice == '1':
                self.kinematic_equation()
            elif choice == '2':
                self.gravitational_force()
            elif choice == '3':
                self.energy_calculation()
            elif choice == '4':
                print("Thanks. Goodbye!")
                break
            else:
                # Handle invalid choices
                print("Invalid choice. Please enter a number between 1 and 4.")


# Entry point of the program
if __name__ == "__main__":
    # Create an instance of the PhysicsCalculator class and run the calculator
    physics_calculator = PhysicsCalculator()
    physics_calculator.run_calculator()
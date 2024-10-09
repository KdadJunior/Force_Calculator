###########################################################
#  Computer Project #8
#  Algorithm
#    prompt for an option
#    input an option
#    loop while not end-of-program
#       if option 1:
#          prompt for the name, magnitude, and angle of a force
#          input the name, magnitude, and angle
#          add force to the calculator
#       if option 2:
#          prompt for the name of a force to remove
#          input the name
#          remove force from the calculator
#       if option 3:
#          display all forces in the calculator
#       if option 4:
#          prompt for the name of a force
#          input the name
#          find and display force components
#       if option 5:
#          compute and display resultant force
#       if option 6:
#          reset the calculator
#       if option 7:
#          exit the program
#       if invalid option:
#          display error message
#          reprompt for an option
###########################################################

from force import ForceCalculator, Force
import sys

def prompt_num(prompt_str):
    """
    Prompt the user for a numeric value, reprompting if the input is not a valid float.
    """
    while True:
        value_str = input(prompt_str)
        try:
            value = float(value_str)
            return value
        except ValueError:
            print(f"\nInput {value_str} is not a valid float number!")

def main():
    calc = ForceCalculator()
    while True:
        choice = input("\n:~Net Force Calculator Program\n"
                       "          1) Add force\n"
                       "          2) Remove force\n"
                       "          3) Show forces\n"
                       "          4) Find force components\n"
                       "          5) Compute resultant force\n"
                       "          6) Reset calculator\n"
                       "          7) Stop the program\n"
                       "          Enter option~:")
        if choice == '1':  # Add force
            name = input("\n:~Enter name of force~:")
            magnitude = prompt_num("\n:~Enter value for Magnitude (N)~: ")
            angle = prompt_num("\n:~Enter value for Angle (degrees)~: ")
            try:
                calc.add_force(name, magnitude, angle)
            except RuntimeError as e:
                print(e)
        elif choice == '2':  # Remove force
            name = input("\n:~Enter name of force~:")
            try:
                calc.remove_force(name)
            except RuntimeError as e:
                print(e)
        elif choice == '3':  # Show forces
            if not calc.get_forces():
                print("\nThere are no force objects in the calculator.")
            else:
                print("\nForce objects in the calculator")
                print(calc)
        elif choice == '4':  # Find force components
            name = input("\n:~Enter name of force~:")
            try:
                force = calc[name]
                fx, fy = force.get_components()
                print(f"\nForce components for Force object {name}:")
                print(f"\nFx = {fx:.2f}\nFy = {fy:.2f}")
            except RuntimeError as e:
                print(e)
        elif choice == '5':  # Compute net force
            net_force = calc.compute_net_force()
            print("\nResultant force of all forces in the calculator")
            print(net_force)
        elif choice == '6':  # Reset calculator
            calc = ForceCalculator()
            print("\nCalculator has been reset.")
        elif choice == '7':  # Stop the program
            break
        else:
            print("\nInvalid option. Please Try Again!")

if __name__ == "__main__":
    main()

print("Welcome to the Python Landscaper 🐍🪴 game!")

# Create a landscaper function to calculate the total earrning based on the number of days worked
def landscaper(days: int, wage: int) -> int:
    daily_earnings = days * wage
    return daily_earnings

# Create a loop function that will allow the player to keep entering intergers of days worked until they are done with the game
def main():
    print("What would you like the name of your landscaping business to be called?")
    landscaping_business = input()
    print(f'Welcome to the world of landscping {landscaping_business}! As a new business you will be starting out with just your teeth as a tool. Using just your teeth, you can spend the day cutting lawns and make $1. You can do this as much as you want. The more money you make, the better tools you can purchase!')

    # create a total earnings to be updated as the user plays
    total_earnings= 0
    wage = 1 #Start with a wage of $1/day

    while True:
        try:
            days = int(input("Enter the number of days you would like to work (or type 'exit' to quit): "))
            # take the days interger entered by the player and call on the landscaper function to return new total earnings
            daily_earnings = landscaper(days, wage)
            # add the daily earning to the total earnings
            total_earnings += daily_earnings
            print(f"After {days} days you have earned ${daily_earnings}.")
            print(f"{landscaping_business} has made a total of ${total_earnings}.")

            if total_earnings > 1000:
                print(f'You have made a total of ${total_earnings}! You have won the game!')
                break

            elif total_earnings > 500:
                wage = 250
                print(f'With a total earnings of ${total_earnings}, you had enough to upgrade from your fancy battery-powered lawnmower to a team of starving students. You can now make ${wage} per day!')
                
            elif total_earnings > 250:
                wage = 100
                print(f'With a total earnings of ${total_earnings}, you had enough to upgrade from your vintage lawnmower to a fancy battery-powered lawnmower. You can now make ${wage} per day!')
            
            elif total_earnings > 25:
                wage = 50
                print(f'With a total earnings of ${total_earnings}, you had enough to upgrade from your rusty scissors to a vintage lawnmower. You can now make ${wage} per day!')
            
            elif total_earnings > 5:
                wage = 5
                print(f'With a total earnings of ${total_earnings}, you had enough to upgrade from your teeth to a pair of rusty scissors. You can now make ${wage} per day!')


            continue_working = input("Do you want to continue working? (yes or no): ").lower()
            if continue_working != 'yes':
                print("Game Over")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number of days or type 'exit' to quit.")
            break

# call on the main game function
if __name__ == "__main__":
    main()
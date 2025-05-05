center_align = "                                                                  "

def print_app_title():
    """Return ASCII title of app"""
    ascii_title = r"""
    $$\   $$\ $$\     $$\  $$$$$$\        $$$$$$$\                        $$\                                                       $$\            $$$$$$\                      
    $$$\  $$ |\$$\   $$  |$$  __$$\       $$  __$$\                       $$ |                                                      $$ |          $$  __$$\                     
    $$$$\ $$ | \$$\ $$  / $$ /  \__|      $$ |  $$ | $$$$$$\   $$$$$$$\ $$$$$$\    $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$\  $$$$$$$\ $$$$$$\         $$ /  $$ | $$$$$$\   $$$$$$\  
    $$ $$\$$ |  \$$$$  /  $$ |            $$$$$$$  |$$  __$$\ $$  _____|\_$$  _|   \____$$\ $$ |  $$ |$$  __$$\ \____$$\ $$  __$$\\_$$  _|        $$$$$$$$ |$$  __$$\ $$  __$$\ 
    $$ \$$$$ |   \$$  /   $$ |            $$  __$$< $$$$$$$$ |\$$$$$$\    $$ |     $$$$$$$ |$$ |  $$ |$$ |  \__|$$$$$$$ |$$ |  $$ | $$ |          $$  __$$ |$$ /  $$ |$$ /  $$ |
    $$ |\$$$ |    $$ |    $$ |  $$\       $$ |  $$ |$$   ____| \____$$\   $$ |$$\ $$  __$$ |$$ |  $$ |$$ |     $$  __$$ |$$ |  $$ | $$ |$$\       $$ |  $$ |$$ |  $$ |$$ |  $$ |
    $$ | \$$ |    $$ |    \$$$$$$  |      $$ |  $$ |\$$$$$$$\ $$$$$$$  |  \$$$$  |\$$$$$$$ |\$$$$$$  |$$ |     \$$$$$$$ |$$ |  $$ | \$$$$  |      $$ |  $$ |$$$$$$$  |$$$$$$$  |
    \__|  \__|    \__|     \______/       \__|  \__| \_______|\_______/    \____/  \_______| \______/ \__|      \_______|\__|  \__|  \____/       \__|  \__|$$  ____/ $$  ____/ 
                                                                                                                                                    $$ |      $$ |      
                                                                                                                                                            $$ |      $$ |      
                                                                                                                                                            \__|      \__|"""
    print()
    print(ascii_title) 

def print_tagline():
    """Return tagline (below app title)"""
    tagline = "Find Your Flavor. Anywhere in NYC."
    print(center_align + tagline)


def print_description():
    description = """
A simple command-line tool that suggests NYC restaurants
based on your preferences—like neighborhood, cuisine, budget,
and dietary needs. Fast, personal, and perfect for foodies on the go.
    """
    for line in description.strip().split('\n'):
        print(center_align + line)

def input_get_started():
    print(center_align + "Press ENTER to Get Started: ", end="")
    return input()
    
    
    
def print_welcome_page():
    print_app_title()
    print()  # <- blank line
    print()  # <- blank line

    print_tagline()
    print()  # <- blank line

    print_description()
    print()  # <- blank line


def print_homepage():
    print()
    print("Welcome to the NYC Restaurant App!")
    print()
    print("Choose from below:")
    print()
    print("[1] User Inputs")
    print("[2] Search Restaurant")
    print("[3] View Your Favorite Restaurant")
    print("[4] Random Restaurant Recommendation")
    print()

def input_homepage():
    print("Type the number corresponding to your choice and press ENTER (e.g., 1): ", end="")
    return input()

def print_user_preference():
    print()
    print("Put in Your Preferences:")
    print()
    print("1. Neighborhood (ex. \"Brooklyn\", \"Manhattan\", \"Queens\"):")
    print("2. Price Range (Under $15, $15-$30, $30-$60, $60+):")
    print("3. Rating (Minimum Acceptable Rating):")
    print()
    
def print_search_restaurant():
    print()
    print("────────────────────────────────────────────────────────────")
    print("Search Box:")
    print("────────────────────────────────────────────────────────────")
    print()
    print("Place to eat, dine, and enjoy...")
    print()
    print("────────────────────────────────────────────────────────────")
    print("Search Results")
    print("────────────────────────────────────────────────────────────")
    print()
    print("    Restaurant 1")
    print("    Restaurant 2")
    print("    Restaurant 3")
    print()

def print_view_saved_restaurant():
    print()
    print("────────────────────────────────────────────────────────────")
    print("User: ID")
    print("User: Name")
    print("────────────────────────────────────────────────────────────")
    print()
    print("List of Favorite Restaurants")
    print("────────────────────────────────────────────────────────────")
    print()
    print("    Restaurant 1")
    print("    Restaurant 2")
    print("    Restaurant 3")
    print("    ...")
    print()


def print_restaurant_detail():
    print()
    print("    Restaurant Name")
    print()
    print("    Address of Restaurant")
    print()
    print("    Rating, Cuisine Type, Hours Open")
    print()
    print("    Reviews")
    print("    ┌───────────────────────────────────────────────┐")
    print("    │ Review #1                                     │")
    print("    │ Review #2                                     │")
    print("    │ Review #3                                     │")
    print("    │ ...                                           │")
    print("    └───────────────────────────────────────────────┘")
    print()    


                      
if __name__ == "__main__":
    print_welcome_page()
    user_get_started = input_get_started()
    if user_get_started == "":
        print_homepage()
        user_homepage = input_homepage()
        if user_homepage == "1":
            print_user_preference()
        elif user_homepage == "2":
            print_search_restaurant()
        elif user_homepage == "3":
            print_view_saved_restaurant()
        elif user_homepage == "4":
            print_restaurant_detail()
        else:
            print("\nInvalid input. Please enter a number from 1 to 4.\n")



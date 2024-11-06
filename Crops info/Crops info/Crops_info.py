
# Simple Python program to collect crop information

# Define a list to store crop data
crops = []

# Function to prompt for crop information
def get_crop_info():
    crop_name = input("Enter the crop name: ")
    season = input("Enter the growing season (e.g., summer, winter): ")
    water_requirement = input("Enter the water requirement level (e.g., high, medium, low): ")
    yield_per_hectare = input("Enter the average yield per hectare (e.g., 4 tons): ")

    # Store the information in a dictionary
    crop_info = {
        'Name': crop_name,
        'Season': season,
        'Water Requirement': water_requirement,
        'Yield per Hectare': yield_per_hectare
    }
    
    return crop_info

# Main program loop to gather multiple crops data
print("Welcome to the Crop Information Program!")
while True:
    # Prompt for crop information and add it to the list
    crop = get_crop_info()
    crops.append(crop)
    
    # Ask if user wants to enter another crop
    more = input("Would you like to enter another crop? (yes/no): ").strip().lower()
    if more != 'yes':
        break

# Display all crop information
print("\nSummary of Crops Information:")
for i, crop in enumerate(crops, start=1):
    print(f"\nCrop #{i}:")
    for key, value in crop.items():
        print(f"{key}: {value}")

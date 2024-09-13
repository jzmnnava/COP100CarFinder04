#Define List(Array) 
AllowedVehiclesList = [
   'Ford F-150',
   'Chevrolet Silverado',
   'Tesla CyberTruck',
   'Toyota Tundra',
   'Nissan Titan',
   'Rivian R1T',
   'Ram 1500'
]

#Define function to print the menu
def print_menu():
 print('********************************')
 print('AutoCountry Vehicle Finder v0.4')
 print('********************************')
 print('Please Enter the following number below from the following menu:')
 print('1. PRINT all Authorized Vehicles')
 print('2. SEARCH for Authorized Vehicle')
 print('3. ADD Authorized Vehicle')
 print('4. DELETE Authorized Vehicle')  
 print('5. Exit') 
 print('********************************')  

#Define function to print the list of authorized vehicles
def print_vehicles():
  print('\nThe AutoCountry sales manager as authorized the purchase and selling of the following vehicles:')
  for vehicle in AllowedVehiclesList:
    print(vehicle)
  print ()

#Define function to search for a vehicle
def search_vehicle():
  vehicle_name = input('\nPlease Enter the full vehichle name: ')
  if vehicle_name in AllowedVehiclesList:
     print(f'\n{vehicle_name} is an authorized vehicle')
  else:
      print(f'\n{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again.') 
  print () 

#Define function to add a vehicle
def add_vehicle():
  vehicle_name = input('\n Please enter the full vehicle name you would like to add: ')
  if vehicle_name in AllowedVehiclesList: 
    print(f'\n {vehicle_name} is already an authorized vehicle.')
  else:
    AllowedVehiclesList.append(vehicle_name)
    print(f'\nYou have added "{vehicle_name}" as an authorized vehicle.')
  print()

#Define function to delete a function
def delete_vehicle():
   vehicle_name = input('\nPlease Enter the full Vehicle Name you would like to REMOVE: ')
   if vehicle_name in AllowedVehiclesList:
      confirmation = input(f'\nAre you sure you want to remove "{vehicle_name}" from the Authorized Vehicles List? ')
      if confirmation.lower() == 'yes':
         AllowedVehiclesList.remove(vehicle_name)
         print(f'\nYou have REMOVED "{vehicle_name}" as an authorized vehicle.')
      elif confirmation.lower() == 'no':
         print_menu()
      else:
         print(f'\n"{vehicle_name}" is not found in the Authorized Vehicle list.')

#Define the main loop
while True:
  print_menu()
  choice = input('\nEnter your choice:')

  if choice == '1':
    print_vehicles()
  elif choice == '2':
    search_vehicle()
  elif choice == '3':
    add_vehicle()
  elif choice == '4':
     delete_vehicle()
  elif choice == '5':
    print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
    break
  else:
    print('Invalid choice, please try again')

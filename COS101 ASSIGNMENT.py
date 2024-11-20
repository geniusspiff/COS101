def physics_formula_menu():
    print('\nPhysics formula option:')
    print('a. angular acceleration')
    print('b. angular momentum')
    print('c. specific heat capacity')
    print('d. latent heat')
    print('e. surface tension')

physics_formula_menu()

options = input('pick an option from a to e  ')
print(options)

if options == 'a':
    angular_velocity = int(input('Enter number  '))
    time = int(input('Enter number  '))
    angular_acceleration = angular_velocity / time
    print(angular_acceleration)

elif options == 'b':
    mass = int(input('Enter mass  '))
    velocity = int(input('Enter velocity  '))
    radius = int(input('Enter radius  '))
    angular_momentum = mass * velocity * radius
    print(angular_momentum)

elif options == 'c':
    quantity_of_heat = int(input('Enter value  '))
    mass = int(input('Enter value   '))
    t1 = int(input('Enter value of t1'))
    t2 =  int(input('Enter value of t2  '))
    specific_heat_capacity = quantity_of_heat / (mass * (t2 - t1))
    print(specific_heat_capacity)

elif options == 'd':
    quantity_of_heat = int(input('enter number  '))
    mass = int(input('enter number  '))
    latent_heat = quantity_of_heat / mass
    print(latent_heat)

elif options == 'e':
    force = int(input('enter force in newton  '))
    length = int(input('enter length in meters  '))
    surface_tension = force * length
    print(surface_tension)

else :
    print('invalid option an option from a to e')
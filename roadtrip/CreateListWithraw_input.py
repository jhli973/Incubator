my_list = []
cnt = 1
while cnt < 11:
    location = raw_input("Please enter your " + str(cnt) + " stop address:")
    if location.strip() != '':
        my_list.append(location)
        cnt += 1
    else:
        break
print(my_list)    
    
""" http://www.touropia.com/top-tourist-attractions-in-washington-dc/
Washington National Cathedral
Library of Congress
Georgetown Neighborhood
National Air and Space Museum
Jefferson Memorial
Lincoln Memorial
Washington Monument
United States Capitol
White House
National Mall
"""    
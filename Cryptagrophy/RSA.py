""" Finds value for d in RSA """

e = 1019780502436124204526035803328433120546131480982513669063240298393724197157659719919974259213600826800914988178815738273 # Value of e from task
n = 1425225108873296200467113803219632795530932221093957012175185409440553760738268403886123386867226620153943341619157040813 # Value of n from task

for d in range(1, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000): # Values set to reasonable range
    if((d*e) % n == 1): # Modulo of values to fint 1
        print('First value of d that gives (de mod n = 1) is ' + str(d))
        break # Breaks with first valid value

# Puts together the end result    
print('\nWith ' + str(d) + '*' + str(e) + ' mod ' + str(n) 
      + ', we get ' + str(d*e) + ' mod ' + str(n))





        
        
        
        
        
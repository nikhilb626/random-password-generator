# .....................RANDOM PASSWORD GENERATOR................................

import random


pwlen=int(input("enter the length of password you require:"))
s="qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*"
p="".join(random.sample(s,pwlen))
print(p)





"""x = {1:"x", 2:"xx", 3:"xxx", 2:"xxxx"}
#z = max(x.keys())
z = sorted(x.keys(), reverse=True)
print(z)
y = z[0]
print(x[y])
"""

"""
sorted_dict = sorted(collected_acc.keys(), reverse=True)

max1_values_key = sorted_dict[0]
max1_accuracy_class = collected_acc[max1_values_key]

max2_values_key = sorted_dict[1]
max2_accuracy_class = collected_acc[max2_values_key]

if max1_accuracy_class == max2_accuracy_class:
    self.emergency(max1_accuracy_class)

else:
    self.emergency(max1_accuracy_class)
    self.emergency(max2_accuracy_class)"""

"""
dicri = x = {1:"x", 2:"xx", 3:"xxx", 2:"xxxx"}
str_value = set(dicri.values())
print(str_value)
for i in str_value:
    print(i)
"""


"""
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
current_date = now.date()

msg = "Dear Emergency Services,\nI am reporting a road accident that occurred on the Lotitude long \nat approximately {} on {}.".format(current_time, current_date)

print(msg)
"""




x = set()
x.add("5")
print(x)
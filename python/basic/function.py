#%%
#non return
def rocket_parts():
    print("payload, propellant, structure")

#%%
#return
def rocket_return():
    return "payload, propellant, structure"

# %%
output = rocket_parts()
print(output)

output = rocket_return()
print(output)

# %%
#input parameter
def distance(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destnation"
        
# %%
print(distance("Moon"))
print(distance("Sun"))
# %%
#input multi-parameter
def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

# %%
print(days_to_complete(238855,75))

# %%
total_day = days_to_complete(238855,75)
round(total_day)

# %%

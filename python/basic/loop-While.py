# about while loop
# while condition
## code here
#%%
user_input = ''
inputs = []

while user_input.lower() != 'done' :
    if user_input:
        inputs.append(user_input)

    user_input = input('\nEnter new value, or done when done\n')

print(inputs)


# %%

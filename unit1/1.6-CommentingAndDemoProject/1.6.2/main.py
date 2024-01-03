import drawly

# Display a welcome message
print("Welcome to Shapey")
print() # Add a blank line

# Get the user's name and favorite color
name = input("Enter your name: ")
fav_color = input("Enter your favorite color: ")

# Print a messge including the user's name
print("Thank you, " + name + ". I appreciate the info.")

# Print message and get input for the circle
# Need: x position, y position, radius
print("I want to draw a circle for you. Please give me the following information:")
x_pos = int(input("Where on the x-axis should the circle be? "))
y_pos = int(input("Where on the y-axis should the circle be? "))
radius = int(input("What would you like the radius to be? "))
print()

# Print a message prompting the user to hit enter to open the window
print("I'm excited to draw a circle for you.")
print("Hit enter to open the window.")
input() # No message, just wait for the user to hit enter

# Draw the circle. Add another prompt to get the circle to show
drawly.start(name + "'s Special " + fav_color + " Circle", background="grey")
drawly.set_color(fav_color)
drawly.circle(x_pos, y_pos, radius)
print("Hit Enter to see your circle")
input()
drawly.draw()
drawly.done()

# Print a goodbye message after the user closes the window
print("I hope you enjoyed your " + fav_color + " circle.")
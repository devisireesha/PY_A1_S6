content = "This is the content to be written to the file."

# Open the file in write mode
file = open("data.txt", "w")

# Write the content to the file using the write() method
file.write(content)

# Close the file
file.close()

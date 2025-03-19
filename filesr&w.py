# Read and write
def modify_file(input_file, output_file):
    try:
        # Open for reading 
        with open(input.file, 'r') as in_file:
            content = in_file.read()

        #Modifying content
        modified_content = content.upper()

        # Opening for writing
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File '{input_file}' has been modified and saved as '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


modify_file("input.txt", "output.txt")


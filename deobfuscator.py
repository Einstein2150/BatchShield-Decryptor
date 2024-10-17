import re

def print_banner():
    banner = r"""
 ▄▄▄▄    ▄▄▄     ▄▄▄█████▓ ▄████▄   ██░ ██   ██████  ██░ ██  ██▓▓█████  ██▓    ▓█████▄ ▓█████▄ ▓█████  ▄████▄   ██▀███ ▓██   ██▓ ██▓███  ▄▄▄█████▓ ▒█████   ██▀███     
▓█████▄ ▒████▄   ▓  ██▒ ▓▒▒██▀ ▀█  ▓██░ ██▒▒██    ▒ ▓██░ ██▒▓██▒▓█   ▀ ▓██▒    ▒██▀ ██▌▒██▀ ██▌▓█   ▀ ▒██▀ ▀█  ▓██ ▒ ██▒▒██  ██▒▓██░  ██▒▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒   
▒██▒ ▄██▒██  ▀█▄ ▒ ▓██░ ▒░▒▓█    ▄ ▒██▀▀██░░ ▓██▄   ▒██▀▀██░▒██▒▒███   ▒██░    ░██   █▌░██   █▌▒███   ▒▓█    ▄ ▓██ ░▄█ ▒ ▒██ ██░▓██░ ██▓▒▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒   
▒██░█▀  ░██▄▄▄▄██░ ▓██▓ ░ ▒▓▓▄ ▄██▒░▓█ ░██   ▒   ██▒░▓█ ░██ ░██░▒▓█  ▄ ▒██░    ░▓█▄   ▌░▓█▄   ▌▒▓█  ▄ ▒▓▓▄ ▄██▒▒██▀▀█▄   ░ ▐██▓░▒██▄█▓▒ ▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄     
░▓█  ▀█▓ ▓█   ▓██▒ ▒██▒ ░ ▒ ▓███▀ ░░▓█▒░██▓▒██████▒▒░▓█▒░██▓░██░░▒████▒░██████▒░▒████▓ ░▒████▓ ░▒████▒▒ ▓███▀ ░░██▓ ▒██▒ ░ ██▒▓░▒██▒ ░  ░  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒   
░▒▓███▀▒ ▒▒   ▓▒█░ ▒ ░░   ░ ░▒ ▒  ░ ▒ ░░▒░▒▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▓  ░░ ▒░ ░░ ▒░▓  ░ ▒▒▓  ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░  ██▒▒▒ ▒▓▒░ ░  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░   
▒░▒   ░   ▒   ▒▒ ░   ░      ░  ▒    ▒ ░▒░ ░░ ░▒  ░ ░ ▒ ░▒░ ░ ▒ ░ ░ ░  ░░ ░ ▒  ░ ░ ▒  ▒  ░ ▒  ▒  ░ ░  ░  ░  ▒     ░▒ ░ ▒░▓██ ░▒░ ░▒ ░         ░      ░ ▒ ▒░   ░▒ ░ ▒░   
 ░    ░   ░   ▒    ░      ░         ░  ░░ ░░  ░  ░   ░  ░░ ░ ▒ ░   ░     ░ ░    ░ ░  ░  ░ ░  ░    ░   ░          ░░   ░ ▒ ▒ ░░  ░░         ░      ░ ░ ░ ▒    ░░   ░    
 ░            ░  ░        ░ ░       ░  ░  ░      ░   ░  ░  ░ ░     ░  ░    ░  ░   ░       ░       ░  ░░ ░         ░     ░ ░                           ░ ░     ░        
      ░                   ░                                                     ░       ░             ░                 ░ ░                                              
                                                                                         
                          by Einstein2150                                                
    """
    print(banner)
    
def deobfuscate_file(obfuscated_file, output_file):
    try:
        # Open the obfuscated file and read the content
        with open(obfuscated_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # Remove all strings between percent signs (%), which have been randomly obfuscated
        # The regex searches for patterns like %abc% and removes them
        deobfuscated_content = re.sub(r'%[a-zA-Z]*%', '', content)

        # Save the deobfuscated content in a new file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(deobfuscated_content)

        print(f"Deobfuscation successful! The deobfuscated content is saved in '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{obfuscated_file}' was not found.")
    except IOError:
        print("Error: An I/O error occurred while processing the file.")

def main():
    
    print_banner()  # Call the banner function at the start of the program
    # Get the file for deobfuscation from the user
    obfuscated_file = input("Enter the path to the obfuscated batch file (.bat): ")
    output_file = input("Enter the output file name for the deobfuscated content (.bat): ")

    # Perform the deobfuscation
    deobfuscate_file(obfuscated_file, output_file)

if __name__ == '__main__':
    main()

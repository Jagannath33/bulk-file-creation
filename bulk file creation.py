import os

def create_files(directory, newname, filetype, count=10):
    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Create 10 new files
    for i in range(count):
        filename = f"{newname}{i}.{filetype}"
        filepath = os.path.join(directory, filename)
        
        # Create an empty file
        with open(filepath, 'w') as f:
            f.write("")  # Writing empty content
        
        print(f"Created file: {filepath}")

# Example usage
create_files("C:\\Users\\Asus\\Desktop\\file manipulation", "txt", 10)
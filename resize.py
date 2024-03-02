from PIL import Image
import os

def resize_images(input_folder, output_folder, new_width=1500):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, filename)
        if os.path.isfile(input_file_path):
            # Open the image
            with Image.open(input_file_path) as img:
                # Calculate the new height to maintain aspect ratio
                width_percent = new_width / float(img.size[0])
                new_height = int(float(img.size[1]) * float(width_percent))
                # Resize the image
                resized_img = img.resize((new_width, new_height), Image.LANCZOS)
                
                # Save the resized image to the output folder
                output_file_path = os.path.join(output_folder, filename)
                resized_img.save(output_file_path)
                print(f"Resized image saved: {output_file_path}")

# Example usage:
input_folder = "C:\\Users\\ccaba\\OneDrive\\Desktop\\resize_proyect\\raw_images"
output_folder = "C:\\Users\\ccaba\\OneDrive\\Desktop\\resize_proyect\\resized_images"
resize_images(input_folder, output_folder)

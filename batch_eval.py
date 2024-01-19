import os
import subprocess

# Directory containing the images
image_directory = 'Room_SetA'

# Output directory
output_directory = 'outputs'

# Path to the checkpoint file
checkpoint_path = 'models/scream.ckpt'

# Iterate over all files in the image directory
for filename in os.listdir(image_directory):
    if filename.endswith('.png'):  # Check if the file is a PNG image
        # Construct the full path to the image
        input_path = os.path.join(image_directory, filename)

        # Construct the command
        command = [
            'python', 'evaluate.py',
            '--checkpoint', checkpoint_path,
            '--in', input_path,
            '--out', output_directory
        ]

        # Run the command
        subprocess.run(command)

print("Processing complete.")


import qrcode
from PIL import Image
import qrcode.constants

def generate_custom_qr_code(url, filename="generated_qr(adv).png"):
    """
    Generate a custom QR code from a given URL with specified colors and save it as an image file.

    Parameters:
    - url (str): The URL to encode into a QR code.
    - filename (str): The filename for the saved QR code image. Defaults to "generated_qr(adv).png".
    """
    try:
        # Create a QRCode object with specified parameters
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR code
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level (H: 30% error correction)
            box_size=10,  # Size of each box in the QR code grid
            border=4  # Thickness of the border (minimum is 4)
        )
        
        # Add data (URL) to the QRCode object
        qr.add_data(url)
        
        # Optimize the QR code for the given data
        qr.make(fit=True)
        
        # Create an image of the QR code with specified colors
        img = qr.make_image(fill_color="red", back_color="grey")
        
        # Save the generated QR code image to a file
        img.save(filename)
        
        # Notify the user that the QR code has been successfully saved
        print(f"Custom QR code successfully saved as {filename}")
    except Exception as e:
        # Print an error message if something goes wrong
        print(f"An error occurred: {e}")

def main():
    """
    Main function to handle user input and initiate custom QR code generation.
    """
    # Prompt the user to enter a URL
    qr_link = input("Please enter the URL for which you want to generate a custom QR code: ").strip()
    
    # Check if the user input is empty
    if not qr_link:
        print("The URL cannot be empty. Please provide a valid URL.")
    else:
        # Call the function to generate and save the custom QR code
        generate_custom_qr_code(qr_link)

# Ensure the script runs only if executed directly (not imported as a module)
if __name__ == "__main__":
    main()

import qrcode as qr

def generate_qr_code(url, filename="generated_qr.png"):
    """
    Generate a QR code from a given URL and save it as an image file.

    Parameters:
    - url (str): The URL to encode into a QR code.
    - filename (str): The filename for the saved QR code image. Defaults to "generated_qr.png".
    """
    try:
        # Generate QR code image from the URL
        qr_img = qr.make(url)
        
        # Save the generated QR code image to a file
        qr_img.save(filename)
        
        # Notify the user that the QR code has been successfully saved
        print(f"QR code successfully saved as {filename}")
    except Exception as e:
        # Print an error message if something goes wrong
        print(f"An error occurred: {e}")

def main():
    """
    Main function to handle user input and initiate QR code generation.
    """
    # Prompt the user to enter a URL
    url = input("Please enter the URL for which you want to generate a QR code: ").strip()
    
    # Check if the user input is empty
    if not url:
        print("The URL cannot be empty. Please provide a valid URL.")
    else:
        # Call the function to generate and save the QR code
        generate_qr_code(url)

# Ensure the script runs only if executed directly (not imported as a module)
if __name__ == "__main__":
    main()

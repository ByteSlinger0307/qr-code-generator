# QR Code Generator

A Python project to generate QR codes from URLs. This project includes two scripts: one for creating basic QR codes and another for generating QR codes with custom colors.

## Features

- **Basic QR Code Generator**: Creates a standard QR code for a given URL.
- **Advanced QR Code Generator**: Allows customization of QR code colors (foreground and background).
- Both scripts save the generated QR code as an image file.

## Requirements

- Python 3.x
- `qrcode` library with PIL support

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/ByteSlinger0307/qr-code-generator.git
    ```

2. Navigate to the project directory:
    ```bash
    cd qr-code-generator
    ```

3. Install the required Python packages:
    ```bash
    pip install qrcode[pil]
    ```

## Usage

### Basic QR Code Generator

1. Run the script:
    ```bash
    python basic_qr_generator.py
    ```

2. Enter the URL when prompted, and a basic QR code will be saved as `generated_qr.png`.

### Advanced QR Code Generator

1. Run the script:
    ```bash
    python advanced_qr_generator.py
    ```

2. Enter the URL when prompted, and a customizable QR code will be saved as `generated_qr(adv).png`. This script allows you to set the fill and background colors of the QR code.

## Code Overview

### Basic QR Code Generator

- `import qrcode`: Imports the `qrcode` library to create QR codes.
- `qr.make(url)`: Generates a QR code image from the provided URL.
- `qr_img.save("generated_qr.png")`: Saves the QR code image as `generated_qr.png`.

### Advanced QR Code Generator

- `import qrcode`: Imports the `qrcode` library to create QR codes.
- `qr = qrcode.QRCode(...)`: Configures the QR code with version, error correction level, box size, and border.
- `qr.add_data(url)`: Adds the URL data to the QR code object.
- `qr.make(fit=True)`: Optimizes the QR code for the given data.
- `qr.make_image(fill_color="red", back_color="grey")`: Creates an image with custom fill and background colors.
- `img.save("generated_qr(adv).png")`: Saves the customizable QR code image as `generated_qr(adv).png`.

## Contributing

Feel free to fork the repository and submit pull requests with improvements or bug fixes. For any questions or suggestions, open an issue or contact me directly.

## Contact

- **Name**: Krish Dubey
- **Email**: dubeykrish0208@gmail.con
- **GitHub**: [(https://github.com/)](https://github.com/ByteSlinger0307)


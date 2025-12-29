import qrcode
from qrcode.image.styledpil import StyledPilImage
def generate_qr_code(data: str, filename: str, image_path: str):
    """Generate a QR code image given data and an image path.

    Args:
        data: Text or URL to encode
        filename: Name for the output PNG file (without extension)
        image_path: Path to the image to be used in the QR code
    """
    print("called generate qr code",filename,image_path)
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data)

    img = qr.make_image(image_factory=StyledPilImage, embedded_image_path=image_path)
    output_file = f"{filename}.png"
    img.save(output_file)

    return f" successfully  QR code generated and  saved as {output_file} containing: {data[:50]}..."
tool_schema={
        "type": "function",
        "function": {
            "name": "generate_qr_code",
            "description": "Generate a QR code (PNG) from text/URL and embed an image inside it.",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "string",
                        "description": "The text or URL to encode in the QR code"
                    },
                    "filename": {
                        "type": "string",
                        "description": "Name for the output file (without extension)"
                    },
                    "image_path": {
                        "type": "string",
                        "description": "Path to the image to embed inside the QR code"
                    }
                },
                "required": ["data", "filename", "image_path"]
            }
        }
    }
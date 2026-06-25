from PIL import Image

def hide_message(image_path, message, output_path, password):
    # Combine password + message
    secured_message = password + "|||" + message + "###END###"
    binary_message = ''.join(format(ord(c), '08b') 
                             for c in secured_message)
    
    image = Image.open(image_path)
    image = image.convert("RGB")
    pixels = list(image.getdata())

    if len(binary_message) > len(pixels) * 3:
        raise ValueError("Message is too long for this image!")

    new_pixels = []
    msg_index = 0

    for pixel in pixels:
        r, g, b = pixel

        if msg_index < len(binary_message):
            r = (r & 0xFE) | int(binary_message[msg_index])
            msg_index += 1

        if msg_index < len(binary_message):
            g = (g & 0xFE) | int(binary_message[msg_index])
            msg_index += 1

        if msg_index < len(binary_message):
            b = (b & 0xFE) | int(binary_message[msg_index])
            msg_index += 1

        new_pixels.append((r, g, b))

    new_image = Image.new("RGB", image.size)
    new_image.putdata(new_pixels)
    new_image.save(output_path)
    return output_path


def reveal_message(image_path, password):
    image = Image.open(image_path)
    image = image.convert("RGB")
    pixels = list(image.getdata())

    binary_message = ""
    for pixel in pixels:
        for channel in pixel:
            binary_message += str(channel & 1)

    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        char = chr(int(byte, 2))
        message += char
        if message.endswith("###END###"):
            full_message = message[:-9]
            # Check password
            if "|||" in full_message:
                stored_password, actual_message = full_message.split("|||", 1)
                if stored_password == password:
                    return actual_message
                else:
                    return "ACCESS DENIED! Wrong password! 🔴"
            return full_message

    return "No hidden message found!"
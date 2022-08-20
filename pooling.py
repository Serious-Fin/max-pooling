from PIL import Image
import sys


def main():
    
    # Read command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python pooling.py input.jpg 2 (pool size eg. 2, 5, ... px")

    # Read image and return a 2D list containing tuples that store
    # red, green and blue (r, g, b) values of each pixel maximum
    rgb = read_image(sys.argv[1], sys.argv[2])

    # Return new image with provided pixel colors
    n_image = draw_image(rgb)

    n_image.show()


def read_image(image_name, pool_size):
    """Function, that reads image, finds maximum pixels in pools and
       returns a 2D list containing their (r, g, b) values"""

    # Try and open image
    try:
        img = Image.open(image_name)
        pool_size = int(pool_size)
    except:
        sys.exit("No image with such name found or incorrect pool size")

    rgb = []
    height = img.size[1]
    width = img.size[0]

    # Loop through the whole image chunk by chunk
    for y in range(0, height, pool_size):

        row = []

        for x in range(0, width, pool_size):

            # Prepare to save max pixel
            max_px = ((0, 0, 0), 0)

            # Loop through each pixel in pool
            for y_p in range(y, y+pool_size, 1):
                for x_p in range(x, x+pool_size, 1):

                    # Check whether pixel is in bounds
                    if 0 <= y_p < height and 0 <= x_p < width:
                        # Get pixels' r, g, b values
                        values = img.getpixel((x_p, y_p))

                        # Check if it's new max
                        if sum(values) > max_px[1]:
                            max_px = (values, sum(values))

            # Add max pixel values to row list
            row.append(max_px[0])
        
        # Add row list to result list
        rgb.append(row)
    
    return rgb


def draw_image(rgb):
    """Function, that draws provided pixels on a new image"""

    # Get height and width of new image
    height = len(rgb)
    width = len(rgb[0])

    print(f"New resolution: {width}x{height}")

    # Create new image
    new_image = Image.new('RGB', (width, height))

    # Set it's pixel colors
    for y in range(height):
        for x in range(width):
            new_image.putpixel((x, y), rgb[y][x])

    return new_image


if __name__ == "__main__":
    main()
import pygame
import os

def add_watermark(image_path, watermark_text):
    # Initialize Pygame
    pygame.init()

    # Load the image
    image = pygame.image.load(image_path)

    # Create a surface with the same size as the image
    surface = pygame.Surface(image.get_size(), pygame.SRCALPHA)

    # Set the font properties
    font = pygame.font.SysFont("Arial", 50)
    text_color = (255, 255, 255)  # White

    # Render the watermark text
    text = font.render(watermark_text, True, text_color)

    # Calculate the position to place the watermark (centered)
    x = (surface.get_width() - text.get_width()) // 2
    y = (surface.get_height() - text.get_height()) // 2

    # Blit the image and the watermark text onto the surface
    surface.blit(image, (0, 0))
    surface.blit(text, (x, y))

    # Create a new folder for the watermarked images (if it doesn't exist)
    output_folder = "watermarked_images"
    os.makedirs(output_folder, exist_ok=True)

    # Save the watermarked image
    output_path = os.path.join(output_folder, "watermarked_" + os.path.basename(image_path))
    pygame.image.save(surface, output_path)

    # Quit Pygame
    pygame.quit()

    print("Watermarked image saved:", output_path)

image_path = #specify the image path"
watermark_text = "Watermark"

add_watermark(image_path, watermark_text)
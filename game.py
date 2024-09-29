import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load a sound file
pygame.mixer.music.load('audio.mp3')  # Replace with your file path

# Play the sound
pygame.mixer.music.play()

# Keep the program running until the sound finishes
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

import pygame
import time

# Screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
CAR_WIDTH = 100
CAR_HEIGHT = 40
CAR_SPEED = 8  # Increase this value for a faster car

# Set your desired stopping point here
STOP_LINE_POSITION = SCREEN_WIDTH / 1.5

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Traffic Light Simulation")

def draw_traffic_light(state):
    # Draw traffic light box
    pygame.draw.rect(screen, BLACK, pygame.Rect(SCREEN_WIDTH - 100, 50, 50, 150))

    # Draw lights
    if state == 0:
        pygame.draw.rect(screen, RED, pygame.Rect(SCREEN_WIDTH - 90, 60, 30, 30))
    else:
        pygame.draw.rect(screen, BLACK, pygame.Rect(SCREEN_WIDTH - 90, 60, 30, 30))

    if state == 1:
        pygame.draw.rect(screen, GREEN, pygame.Rect(SCREEN_WIDTH - 90, 100, 30, 30))
    else:
        pygame.draw.rect(screen, BLACK, pygame.Rect(SCREEN_WIDTH - 90, 100, 30, 30))

def draw_car(x):
    # Change the car color to white
    pygame.draw.rect(screen, WHITE, pygame.Rect(x, SCREEN_HEIGHT - 100, CAR_WIDTH, CAR_HEIGHT))

def draw_stop_line():
    # Draw a small block at the stop line position
    pygame.draw.rect(screen, WHITE, pygame.Rect(STOP_LINE_POSITION - 10, SCREEN_HEIGHT - 120, 20, 10))  # Small block

def main():
    clock = pygame.time.Clock()
    car_x = -CAR_WIDTH  # Start position of the car off-screen
    traffic_light_state = 0  # 0 = Red, 1 = Green
    light_change_time = time.time()  # Track the time for light change
    car_stopped = False  # Track if the car has stopped

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill(BLACK)

        # Update car position
        if traffic_light_state == 1:  # Green light
            if car_stopped:
                # Allow the car to move again after stopping
                car_stopped = False
            car_x += CAR_SPEED
            if car_x > SCREEN_WIDTH:
                car_x = -CAR_WIDTH  # Reset car position off-screen
        elif traffic_light_state == 0:  # Red light
            if car_x < STOP_LINE_POSITION - CAR_WIDTH:
                car_x += CAR_SPEED
            if car_x >= STOP_LINE_POSITION - CAR_WIDTH:
                car_stopped = True  # Stop the car when it reaches the stop line

        # Draw everything
        draw_stop_line()  # Draw the small stop block
        draw_traffic_light(traffic_light_state)
        draw_car(car_x)

        # Update display
        pygame.display.flip()

        # Check if it's time to change the traffic light
        if time.time() - light_change_time > 5:  # 5 seconds for each light
            traffic_light_state = 1 - traffic_light_state  # Toggle between 0 and 1
            light_change_time = time.time()

        # Cap the frame rate
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
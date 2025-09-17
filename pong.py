import pygame

pygame.init()

# initials

WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pong game")  # window name
run = True
# colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
# for the ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 0.1, 0.1

# for paddles
paddle_width, paddle_height = 20, 120
left_paddle_x, left_paddle_y = WIDTH-990, (HEIGHT/2)-50
right_paddle_x, right_paddle_y = WIDTH-paddle_width-10, (HEIGHT/2)-50
right_paddle_vel = left_paddle_vel = 0

# main loop
while run:
    wn.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.5
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.5
            if i.key == pygame.K_w:
                left_paddle_vel = -0.5
            if i.key == pygame.K_s:
                left_paddle_vel = 0.5
        if i.type == pygame.KEYUP:
            right_paddle_vel = 0
            left_paddle_vel = 0
    # ball movement control
    if ball_y <= 0+radius or ball_y >= HEIGHT - radius:
        ball_vel_y = ball_vel_y*-1
    if ball_x >= WIDTH-radius or ball_x <= 0+radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        ball_vel_x = ball_vel_x*-1
        ball_vel_y = ball_vel_y*-1

    # paddle movement
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel
    # paddle movement restrictions
    if right_paddle_y >= HEIGHT-paddle_height or right_paddle_y <= 0:
        right_paddle_vel = 0

    if left_paddle_y >= HEIGHT-paddle_height or left_paddle_y <= 0:
        left_paddle_vel = 0

    # ball bouncing from paddles
    # left paddle
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *= -1

    # right paddle
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x
            ball_vel_x *= -1

    # Ball movement
    ball_x += ball_vel_x
    ball_y += ball_vel_y

    # objects
    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, RED, (left_paddle_x, left_paddle_y,
                     paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, (right_paddle_x, right_paddle_y,
                     paddle_width, paddle_height))

    pygame.display.update()
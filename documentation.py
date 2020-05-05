# if jump_event == False and x <= 210 and y <= 470 or jump_event == False and x >= 290 and y <= 470:
# 	y += 470 - y
# if x_event == 1 and y_event == 1:
# 	x += speed
# 	y += speed
# 	if x >= 500 - width:
# 		x_event = 0
# 	if y >= 500 - height:
# 		y_event = 0
# if x_event <= 0 and y_event == 1:
# 	x -= speed
# 	y += speed
# 	if x == 0:
# 		x_event = 1
# 	if y >= 500 - height:
# 		y_event = 0
# if x_event == 1 and y_event <= 0:
# 	x += speed
# 	y -= speed
# 	if x >= 500 - width:
# 		x_event = 0
# 	if y == 0:
# 		y_event = 1
# if x_event <= 0 and y_event <= 0:
# 	x -= speed
# 	y -= speed
# 	if x == 0:
# 		x_event = 1
# 	if y == 0:
# 		y_event = 1

  # if keys[pygame.K_UP] and y > 0:
  # 	y -= speed
  # if keys[pygame.K_DOWN] and y < 500 - height:
  # 	y += speed

# 	image_path = os.path.dirname(__file__)
# print(image_path)
# walkRight = [pygame.image.load(os.path.join(image_path, 'pygame_right_1.png')),
#              pygame.image.load(os.path.join(image_path, 'pygame_right_2.png')),
#              pygame.image.load(os.path.join(image_path, 'pygame_right_3.png')),
#              pygame.image.load(os.path.join(image_path, 'pygame_right_3.png')),
#              pygame.image.load(os.path.join(image_path, 'pygame_right_4.png')),
#              pygame.image.load(os.path.join(image_path, 'pygame_right_5.png')),
#              pygame.image.load(os.path.join(image_path, 'pygame_right_6.png'))]
#
# walkLeft = [pygame.image.load(os.path.join(image_path, 'pygame_left_1.png')),
#             pygame.image.load(os.path.join(image_path, 'pygame_left_2.png')),
#             pygame.image.load(os.path.join(image_path, 'pygame_left_3.png')),
#             pygame.image.load(os.path.join(image_path, 'pygame_left_4.png')),
#             pygame.image.load(os.path.join(image_path, 'pygame_left_5.png')),
#             pygame.image.load(os.path.join(image_path, 'pygame_left_6.png'))]
#
# bg = pygame.image.load(os.path.join(image_path, 'pygame_bg.jpg'))
# playerStand = pygame.image.load(os.path.join(image_path, 'pygame_idle.png'))

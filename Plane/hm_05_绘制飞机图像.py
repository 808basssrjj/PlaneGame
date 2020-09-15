import pygame

# 游戏的初始化
pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (190, 500))

# 可统一调用
pygame.display.update()


# 游戏循环 > 游戏开始
while True:
    pygame.event.get(1000)

pygame.quit()

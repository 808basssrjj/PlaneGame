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

# 创建时钟对象
click = pygame.time.Clock()

# 1> 定义Rect记录飞机的初始位置
hero_rect = pygame.Rect(190, 500, 102, 126)

# 游戏循环 > 游戏开始
while True:
    pygame.event.get(1000)
    # 指定循环体内部的执行频率
    click.tick(60)

    # 2>修改飞机位置
    hero_rect.y -= 1
    # 3>调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    # 4>update跟新
    pygame.display.update()


pygame.quit()

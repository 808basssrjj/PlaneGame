import pygame

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
# 1>加载图像数据
bg = pygame.image.load("./images/background.png")
# 2>屏幕对象调用blit方法
screen.blit(bg, (0, 0))
# 3>update更新
pygame.display.update()

# 游戏循环
while True:
    pygame.event.get(1000)

pygame.quit()

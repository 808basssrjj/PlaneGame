import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战精灵"""

    def __init__(self, image_name, speed=1):

        # 调用初始化父类方法
        super().__init__()

        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在垂直方向移动
        self.rect.y += self.speed


class BackGround(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 1.调用父类方法创建背景精灵
        super().__init__("./images/background.png")
        # 2.
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self,):

        # 1. 调用父类方法
        super().update()
        # 2. 判断是否移出屏幕，如果移出，重新回到上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""
    pass

    def __init__(self, is_alt=False):
        # 1.调用父类方法创建敌机精灵
        super().__init__("./images/enemy1.png")
        # 2.指定敌机的初始速度
        self.speed = random.randint(1, 3)
        # 3.指定敌机的初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self, ):
        # 1. 调用父类方法，保持垂直方向飞行
        super().update()
        # 2. 判断是否移出屏幕，如果移出，从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕，需要删除！")
            # kill方法可以将精灵从精灵组移除，精灵就会销毁
            self.kill()

    def __del__(self):
        # print("敌机挂了 %s" % self.rect)
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 1.调用父类方法创建英雄精灵 设置images和speed
        super().__init__("./images/me1.png", 0)
        # 2.指定英雄的初始随机位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 3.创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 在水平方向移动
        self.rect.x += self.speed
        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # print("发射子弹")

        for i in (0, 1, 2):
            # 1.创建子弹精灵
            bullet = Bullet()
            # 2.设置子弹位置
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.y - i * 20
            # 3.将子弹精灵添加到子弹精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    pass
    """子弹精灵"""

    def __init__(self):
        # 1.调用父类方法创建子弹精灵 设置初始速度
        super().__init__("./images/bullet1.png", -2)

    def update(self, ):
        # 1. 调用父类方法，向上方飞行
        super().update()
        # 2. 判断是否移出屏幕，如果移出，从精灵组删除敌机
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        # print("子弹被销毁...")
        pass

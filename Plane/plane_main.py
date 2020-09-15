import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")

        # 1. 创建游戏窗口
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2. 创建游戏时钟
        self.click = pygame.time.Clock()
        # 3. 调用私有方法，精灵和精灵组的创建
        self.__create_sprites__()

        # 4. 设置定时器事件
        # 4.1>每过1s创建一架敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 4.2>每过0.5s发射子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    # 创建精灵和精灵组
    def __create_sprites__(self):
        # 创建背景精灵的背景精灵组
        bg1 = BackGround()
        bg2 = BackGround(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵组
        self.enmey_group = pygame.sprite.Group()

        # 创建英雄精灵的英雄精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    # 初始化设置并开始
    def start_game(self):
        print("游戏开始...")
        while True:
            pass
            # 1. 设置刷新帧率
            self.click.tick(FRAME_PER_SEC)
            # 2. 监听事件
            self.__event_handler()
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 跟新/绘制精灵组
            self.__update_sprites()
            # 5. 跟新显示
            pygame.display.update()

    # 监听事件
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出场...")
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.enmey_group.add(enemy)
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                # print("向右移动...")
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        # 使用键盘提供的方式获取键盘按键  返回一个元组
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            # print("持续向右移动...")
            self.hero.speed = 2
        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    # 碰撞检测
    def __check_collide(self):
        # 1.子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enmey_group, True, True)
        # 2.敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enmey_group, True)
        if len(enemies) > 0:
            # 让英雄牺牲
            self.hero.kill()
            # 游戏结束
            PlaneGame.__game_over()

    # 跟新/绘制精灵组
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enmey_group.update()
        self.enmey_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    # 游戏退出
    @staticmethod
    def __game_over():
        print("游戏退出...")
        # 卸载所有模块
        pygame.quit()
        # 退出
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 游戏开始
    game.start_game()

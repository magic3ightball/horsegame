import pygame
import random
import time

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('경마 게임')

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# 배경 이미지 로드 및 크기 조정
background_image = pygame.image.load('background.jpg')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# 말 이미지 로드 및 크기 조정
horse_image = pygame.image.load('horse.jpg')
horse_width = 100  # 말 이미지의 폭
horse_height = 100  # 말 이미지의 높이
horse_image = pygame.transform.scale(horse_image, (horse_width, horse_height))

# 지렁이 및 우주선 이미지 로드 및 크기 조정
worm_image = pygame.image.load('worm.jpg')
worm_image = pygame.transform.scale(worm_image, (horse_width, horse_height))
spaceship_image = pygame.image.load('spaceship.jpg')
spaceship_image = pygame.transform.scale(spaceship_image, (horse_width, horse_height))

# 말 이름 목록
horse_names = ["클로이", "엘리", "헤일리", "아리아", "제이", "테라", "레리엘", "니키", "루크", "홒", "리샤", "윈터", "주영"]

# 말 클래스 정의
class Horse:
    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.x = 0
        self.y = 50 * horse_names.index(name)  # 말의 위치를 이름 인덱스에 따라 설정
        self.speed = random.uniform(1, 2)
        self.original_image = image
        self.last_speed_change_time = time.time()  # 마지막 속도 변경 시간을 기록

    def move(self):
        self.x += self.speed
        current_time = time.time()
        if current_time - self.last_speed_change_time >= 2:  # 2초마다 속도 변경
            self.last_speed_change_time = current_time
            if random.choice([True, False]):
                self.speed = random.uniform(3, 4)
                self.image = spaceship_image
                print(f"{self.name}이 우주선을 탔다!")
            else:
                self.speed = random.uniform(0.5, 1)
                self.image = worm_image
                print(f"{self.name}이 지렁이로 변했다!")
        else:
            self.image = self.original_image

# 말 객체 생성
horses = [Horse(name, horse_image) for name in horse_names]

# 폰트 설정
font = pygame.font.Font(None, 24)  # 이름 폰트 크기 조정

# 시작 시간 기록
start_time = time.time()

# 게임 루프
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 경과 시간 계산
    elapsed_time = time.time() - start_time

    if elapsed_time < 10:
        for horse in horses:
            horse.move()
            screen.blit(horse.image, (horse.x, horse.y))
            # 말의 이미지 아래에 이름 출력
            name_text = font.render(horse.name, True, BLACK)
            text_rect = name_text.get_rect(center=(horse.x + horse_width // 2, horse.y + horse_height + 10))
            screen.blit(name_text, text_rect.topleft)
    else:
        # 10초가 지나면 순위를 계산하여 출력
        horses.sort(key=lambda h: h.x, reverse=True)
        winners = horses[:3]
        for i, horse in enumerate(winners):
            result_text = font.render(f"{i+1}등: {horse.name}", True, BLACK)
            screen.blit(result_text, (screen_width // 2 - result_text.get_width() // 2, screen_height // 2 + i * 40))
        
        # 게임 루프 종료
        running = False

    pygame.display.flip()
    clock.tick(60)

# 종료 대기
time.sleep(5)
pygame.quit()
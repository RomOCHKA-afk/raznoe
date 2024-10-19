import math
import random
import tkinter as tk

root = tk.Tk()
canvas_width = 1920
canvas_height = 1080

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

cameraX = 0
cameraY = 0
cameraSpeedFactor = 1.5


class Player:
    def __init__(self, id, x, y, size, base_speed):
        self.id = id
        self.x = x
        self.y = y
        self.size = size
        self.base_speed = base_speed

    @property
    def speed(self):
        return self.base_speed / math.sqrt(self.size)

    def moveTo(self, mouse_x, mouse_y):
        self.dx = mouse_x - (canvas_width / 2)
        self.dy = mouse_y - (canvas_height / 2)
        self.angle = math.atan2(self.dy, self.dx)

        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

        # Ограничение движения игрока в пределах канваса
        self.x = max(self.size, min(self.x, canvas_width - self.size))
        self.y = max(self.size, min(self.y, canvas_height - self.size))

    def draw(self):
        canvas.delete(self.id)
        canvas.create_oval(self.x - self.size - cameraX, self.y - self.size - cameraY,
                           self.x + self.size - cameraX, self.y + self.size - cameraY,
                           fill="blue", outline="black", tags=self.id)


class Food:
    def __init__(self):
        self.foods = []
        for _ in range(100):
            food_item = [
                random.randint(0, canvas_width),
                random.randint(0, canvas_height),
                5
            ]
            self.foods.append(food_item)

    def draw(self):
        for food in self.foods:
            x, y, size = food
            canvas.create_oval(x - size - cameraX, y - size - cameraY,
                               x + size - cameraX, y + size - cameraY,
                               fill="green", outline="black")


# Функция для отрисовки игроков
def draw_players():
    for player in allPlayers:
        player.draw()


# Функция для отрисовки еды
def draw_foods():
    food.draw()  # Теперь правильно вызываем метод draw у экземпляра food


def check_collisions():
    for food_item in food.foods:
        food_x, food_y, food_size = food_item
        distance = math.sqrt((currentPlayer.x - food_x) ** 2 + (currentPlayer.y - food_y) ** 2)


def eat_food():
    global food  # Мы используем объект food, который содержит список foods
    for food_item in food.foods[:]:  # Проходим по копии списка еды
        food_x, food_y, food_size = food_item
        if check_collisions(currentPlayer, food_item):  # Проверяем столкновение с едой
            currentPlayer.size += food_size / 2  # Увеличиваем размер игрока
            food.foods.remove(food_item)  # Удаляем съеденную еду

            # Спавним новую еду
            new_food = [random.randint(0, canvas_width), random.randint(0, canvas_height), 5]
            food.foods.append(new_food)  # Добавляем новую еду


# Создаем игрока
currentPlayer = Player("myId", canvas_width / 2, canvas_height / 2, 10, base_speed=10)
allPlayers = [currentPlayer]  # Добавляем игрока в список всех игроков

# Создаем еду
food = Food()


def mouse_move(event):
    currentPlayer.moveTo(event.x, event.y)


def game_loop():
    canvas.delete("all")  # Очистка канваса
    draw_foods()  # Отрисовка еды
    draw_players()  # Отрисовка игроков
    eat_food()
    check_collisions()  # Проверка столкновений
    root.after(30, game_loop)  # Запуск следующего кадра



canvas.bind("<Motion>", mouse_move)

# Запускаем игровой цикл
game_loop()

# Запускаем основной цикл приложения
root.mainloop()

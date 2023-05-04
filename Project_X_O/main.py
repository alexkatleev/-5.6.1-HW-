def display_board(board):
   print(board[1] + '|' + board[2] + '|' + board[3])
   print('-+-+-')
   print(board[4] + '|' + board[5] + '|' + board[6])
   print('-+-+-')
   print(board[7] + '|' + board[8] + '|' + board[9])


# Функция для проверки победителя
def check_winner(board, player):
   if (board[1] == board[2] == board[3] == player) or \
           (board[4] == board[5] == board[6] == player) or \
           (board[7] == board[8] == board[9] == player) or \
           (board[1] == board[4] == board[7] == player) or \
           (board[2] == board[5] == board[8] == player) or \
           (board[3] == board[6] == board[9] == player) or \
           (board[1] == board[5] == board[9] == player) or \
           (board[3] == board[5] == board[7] == player):
      return True
   else:
      return False


# Функция для осуществления хода
def make_move(board, player, position):
   board[position] = player
   display_board(board)


# Игровое поле
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Отображение начального игрового поля
display_board(board)

# Игроки
player1 = 'X'
player2 = 'O'

# Первый ход - игрок 1
current_player = player1

# Игровой цикл
for i in range(9):
   print("Ход игрока", current_player)
   position = int(input("Выберите позицию на поле (1-9): "))
   make_move(board, current_player, position)

   # Проверка победы
   if check_winner(board, current_player):
      print("Игрок", current_player, "победил!")
      break

   # Смена игрока
   if current_player == player1:
      current_player = player2
   else:
      current_player = player1

# Если никто не победил, объявляем ничью
if not check_winner(board, player1) and not check_winner(board, player2):
   print("Ничья!")
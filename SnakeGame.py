import curses
import random

def main(stdscr):
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(1)
    win.timeout(100)

    snk_x = sw // 4
    snk_y = sh // 2
    snake = [[snk_y, snk_x], [snk_y, snk_x - 1], [snk_y, snk_x - 2]]

    food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
    win.addch(food[0], food[1], curses.ACS_PI)

    key = curses.KEY_RIGHT

    while True:
        next_key = win.getch()
        key = key if next_key == -1 else next_key

        head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            head[0] += 1
        elif key == curses.KEY_UP:
            head[0] -= 1
        elif key == curses.KEY_LEFT:
            head[1] -= 1
        elif key == curses.KEY_RIGHT:
            head[1] += 1

        snake.insert(0, head)

        if head == food:
            food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
            win.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')

        if (head[0] in [0, sh] or head[1] in [0, sw] or head in snake[1:]):
            msg = "Game Over! Press any key to exit."
            win.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)
            win.getch()
            break

        win.addch(head[0], head[1], curses.ACS_CKBOARD)

curses.wrapper(main)

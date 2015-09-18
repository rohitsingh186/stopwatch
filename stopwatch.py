# template for "Stopwatch: The Game"


# import module
import simplegui
import math

# define global variables
current_time = 0
success = 0
stopped = 0
is_running = False
watch_color = "White"
inst_on = False
score_on = False
width = 700
height = 500
text_width = -1
score_width = -1
watch_pos = [100, 100]
score_pos = [100, 100]
player_name = "New Player"
high_scorers = [["Rohit Singh", 70], ["Abhinav Ingole", 60]]


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    d = t % 10
    num_seconds = t / 10
    c = num_seconds % 10
    b = (num_seconds / 10) % 6 
    a = (num_seconds / 10) / 6
    return str(a) + ":" + str(b) + str(c) + ":" + str(d)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global is_running, watch_color
    is_running = True
    watch_color = "White"
    timer.start()

    
def stop():
    global is_running, success, stopped, watch_color
    timer.stop()
    if is_running:
        stopped += 1
        if current_time % 10 == 0:
            success += 1
            watch_color = "Green"
        else:
            watch_color = "Red"
    is_running = False

    
def reset():
    global current_time, is_running, success, stopped, watch_color
    if is_running:
        timer.stop()
        is_running = False
    current_time = 0
    success = 0
    stopped = 0
    watch_color = "White"
    
def instruction():
    global inst_on, is_running, score_on
    if inst_on:
        inst_on = False
        label.set_text('')
        instruction_button.set_text('Instruction')
    else:
        if is_running:
            timer.stop()
            is_running = False
        if score_on:
            high_score_button.set_text('High Scores')
            score_on = False
            label.set_text('')
        inst_on = True
        instruction_button.set_text('***** Instruction *****')
        label.set_text("Your aim in this game will be to stop the watch when the right most digit hits 0. " +
                        "To stop the game, click on the 'Stop' button. You will get one point if you stop it " +
                        "at the right moment else no point will be given. To continue the game, click on the " +
                       "'Start' button. You can also start a new game by clicking the 'Reset' button. Score is " +
                       "saved for high score entry (if it is) after hitting reset button (not in between).")

def high_score():
    global score_on, is_running, inst_on
    if score_on:
        score_on = False
        label.set_text('')
        high_score_button.set_text('High Scores')
    else:
        if is_running:
            timer.stop()
            is_running = False
        if inst_on:
            instruction_button.set_text('Instruction')
            inst_on = False
            label.set_text('')
        score_on = True
        high_score_button.set_text('***** High Scores *****')
        string = ""
        for i in range(len(high_scorers)):
            string = string + str(i + 1) + ". " + high_scorers[i][0] + " : " + str(high_scorers[i][1]) + "% "
        label.set_text(string)    
        
        
def input_handler(inp):
    global player_name, is_running
    if is_running:
        timer.stop()
        is_running = False
    player_name = inp
        
    
# define event handler for timer with 0.1 sec interval
def stopwatch():
    global current_time
    current_time += 1

    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(current_time), watch_pos, 100, watch_color)
    canvas.draw_text("Score : " + str(success) + "/" + str(stopped), score_pos, 40, "Orange")
    if stopped == 0:
        accuracy = ""
        accuracy_color = "Green"
    else:
        accuracy = str(success * 100 / stopped) + "%"
        if int(accuracy[:-1]) < 50:
            accuracy_color = "Red"
        else:
            accuracy_color = "Green"
    canvas.draw_text("Accuracy : " + accuracy, (20, 50), 40, accuracy_color)
    
    
# create frame
frame = simplegui.create_frame("Stopwatch", width, height)
frame.set_canvas_background("Black")


# create timer
timer = simplegui.create_timer(100, stopwatch)


# register event handlers
frame.set_draw_handler(draw)

inp = frame.add_input('Enter Player Name', input_handler, 200)
inp.set_text('New Player')
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)
instruction_button = frame.add_button("Instructions", instruction, 200)
high_score_button = frame.add_button("High Scores", high_score, 200)
label = frame.add_label('')

# Calculating position for drawing watch at the center
text_width = frame.get_canvas_textwidth('0:00:0', 100)
watch_pos = [(width - text_width) / 2, 280]
score_width = frame.get_canvas_textwidth('Score : 10/200', 40)
score_pos = [(width - score_width), 50]


# start frame
frame.start()


# Please remember to review the grading rubric

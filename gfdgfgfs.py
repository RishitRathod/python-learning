import cv2
import numpy as np
import tkinter as tk
from PIL import ImageTk, Image

cap = cv2.VideoCapture('video.mp4')

min_width_react = 80  # min width rectangle
min_height_react = 80  # min height rectangle

count_line_position = 550

# Initialize Subtractor
algo = cv2.createBackgroundSubtractorMOG2()

def center_handle(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

detect = []
offset = 6  # Allowable error between pixels
counter = 0

while True:
    ret, frame1 = cap.read()
    if not ret:
        break  # Break the loop if no frame is read

    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    # Applying on each frame
    img_sub = algo.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
    dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernel)

    counterShape, _ = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame1, (25, count_line_position), (1200, count_line_position), (255, 127, 0), 3)

    for c in counterShape:
        (x, y, w, h) = cv2.boundingRect(c)
        validate_counter = (w >= min_width_react) and (h >= min_height_react)
        if not validate_counter:
            continue

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "Vehicle" + str(counter), (x, y - 20), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 244, 0), 2)

        center = center_handle(x, y, w, h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0, 0, 255), -1)

        for (x, y) in detect:
            if y < (count_line_position + offset) and y > (count_line_position - offset):
                counter += 1
                cv2.line(frame1, (25, count_line_position), (1200, count_line_position), (0, 127, 255), 3)
                detect.remove((x, y))
                print("Vehicle Counter 1: " + str(counter))

        cv2.putText(frame1, "VEHICLE COUNTER : " + str(counter), (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 155), 3)

    cv2.imshow('Video Original', frame1)

    if cv2.waitKey(1) == 13:
        break
    
    
    
cap = cv2.VideoCapture('video1.mp4')

min_width_react = 80  # min width rectangle
min_height_react = 80  # min height rectangle

count_line_position = 450

# Initialize Subtractor
algo = cv2.createBackgroundSubtractorMOG2()

def center_handle(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

detect = []
offset = 6  # Allowable error between pixels
counter1 = 0

while True:
    ret, frame1 = cap.read()
    if not ret:
        break  # Break the loop if no frame is read

    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    # Applying on each frame
    img_sub = algo.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
    dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernel)

    counterShape, _ = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame1, (25, count_line_position), (1200, count_line_position), (255, 127, 0), 3)

    for c in counterShape:
        (x, y, w, h) = cv2.boundingRect(c)
        validate_counter = (w >= min_width_react) and (h >= min_height_react)
        if not validate_counter:
            continue

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "Vehicle" + str(counter), (x, y - 20), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 244, 0), 2)

        center = center_handle(x, y, w, h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0, 0, 255), -1)

        for (x, y) in detect:
            if y < (count_line_position + offset) and y > (count_line_position - offset):
                counter1 += 1
                cv2.line(frame1, (25, count_line_position), (1200, count_line_position), (0, 127, 255), 3)
                detect.remove((x, y))
                print("Vehicle Counter 1: " + str(counter1))

        cv2.putText(frame1, "VEHICLE COUNTER 1: " + str(counter1), (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 155), 3)

    cv2.imshow('Video Original', frame1)

    if cv2.waitKey(1) == 13:
        break
    
    
cap = cv2.VideoCapture('video1.mp4')

min_width_react = 80  # min width rectangle
min_height_react = 80  # min height rectangle

count_line_position = 450

# Initialize Subtractor
algo = cv2.createBackgroundSubtractorMOG2()

def center_handle(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

detect = []
offset = 6  # Allowable error between pixels
counter2 = 0

while True:
    ret, frame1 = cap.read()
    if not ret:
        break  # Break the loop if no frame is read

    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    # Applying on each frame
    img_sub = algo.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
    dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernel)

    counterShape, _ = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame1, (25, count_line_position), (1200, count_line_position), (255, 127, 0), 3)

    for c in counterShape:
        (x, y, w, h) = cv2.boundingRect(c)
        validate_counter = (w >= min_width_react) and (h >= min_height_react)
        if not validate_counter:
            continue

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "Vehicle" + str(counter), (x, y - 20), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 244, 0), 2)

        center = center_handle(x, y, w, h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0, 0, 255), -1)

        for (x, y) in detect:
            if y < (count_line_position + offset) and y > (count_line_position - offset):
                counter2 += 1
                cv2.line(frame1, (25, count_line_position), (1200, count_line_position), (0, 127, 255), 3)
                detect.remove((x, y))
                print("Vehicle Counter 1: " + str(counter2))

        cv2.putText(frame1, "VEHICLE COUNTER 1: " + str(counter2), (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 155), 3)

    cv2.imshow('Video Original', frame1)

    if cv2.waitKey(1) == 13:
        break
    
    
cap = cv2.VideoCapture('video1.mp4')

min_width_react = 80  # min width rectangle
min_height_react = 80  # min height rectangle

count_line_position = 450

# Initialize Subtractor
algo = cv2.createBackgroundSubtractorMOG2()

def center_handle(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

detect = []
offset = 6  # Allowable error between pixels
counter3 = 0

while True:
    ret, frame1 = cap.read()
    if not ret:
        break  # Break the loop if no frame is read

    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    # Applying on each frame
    img_sub = algo.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
    dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernel)

    counterShape, _ = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame1, (25, count_line_position), (1200, count_line_position), (255, 127, 0), 3)

    for c in counterShape:
        (x, y, w, h) = cv2.boundingRect(c)
        validate_counter = (w >= min_width_react) and (h >= min_height_react)
        if not validate_counter:
            continue

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "Vehicle" + str(counter), (x, y - 20), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 244, 0), 2)

        center = center_handle(x, y, w, h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0, 0, 255), -1)

        for (x, y) in detect:
            if y < (count_line_position + offset) and y > (count_line_position - offset):
                counter3 += 1
                cv2.line(frame1, (25, count_line_position), (1200, count_line_position), (0, 127, 255), 3)
                detect.remove((x, y))
                print("Vehicle Counter 1: " + str(counter3))

        cv2.putText(frame1, "VEHICLE COUNTER 1: " + str(counter3), (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 155), 3)

    cv2.imshow('Video Original', frame1)

    if cv2.waitKey(1) == 13:
        break
  
cv2.destroyAllWindows()
cap.release()



if(counter>counter1):
    if(counter>counter2):
        if(counter>counter3):
            greetings = tk.Label(text="side 1")
            greetings.pack()
# greetings.mainloop()

            Label = tk.Label(
                text="ict,department",
                foreground= "white", 
                background= "black"
            )
            Label.mainloop()
else:
   greetings = tk.Label(text="side 2")
   greetings.pack()
# greetings.mainloop()

   Label = tk.Label(
    text="ict,department",
    foreground= "white", 
    background= "black"
    )    
   
   Label.mainloop()

   root = tk.Tk()

   canvas = tk.Canvas(root, width=300, height=300)
   canvas.pack()

   img = Image.open("image.png")
   photo_img = ImageTk.PhotoImage(img)

   canvas.create_image(150, 150, image=photo_img)
   root.mainloop()



    
    
 



import face_recognition
import cv2
import os
import sys
import pygame
import random
from pygame import *
import PIL

# Initalizing Video Capture Variables
video_capture = cv2.VideoCapture(0)
face_locations = []
process_this_frame = True
default_loaded = False
raised_loaded = False
start_game = False

# Setting up Pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Put On Your Game Face!')

white = [255, 255, 255]
screen.fill(white)

done = False
color = (0,0,0)

are_brows_lifted = False

# LOAD IMAGES
start_img = pygame.image.load('images/start_splash.png').convert_alpha()
#load_default_img = pygame.image.load('images/load_def_img.png')
num1_img = pygame.image.load('images/num1_img.png').convert_alpha()
num2_img = pygame.image.load('images/num2_img.png').convert_alpha()
num3_img = pygame.image.load('images/num3_img.png').convert_alpha()
num4_img = pygame.image.load('images/num4_img.png').convert_alpha()
num5_img = pygame.image.load('images/num5_img.png').convert_alpha()
instr_neutral_img = pygame.image.load('images/neutral_inst.png').convert_alpha()
instr_raise_img = pygame.image.load('images/raise_inst.png').convert_alpha()
bend_img = pygame.image.load('images/bend.tiff')
stand_img = pygame.image.load('images/stand.tiff')

# Default Frame Values
weighted_avg_right_d = 0
weighted_avg_left_d = 0
weighted_avg_nose_d = 0
brow_distance_d_def = 0
brow_distance_d_raised = 0
# Frame-By-Frame Values
weighted_avg_right = 0
weighted_avg_left = 0
weighted_avg_nose = 0

# Bools for load buttons
load_default = False
load_raised = False

def capture_frame_face(image):
    weighted_avg_right = 0
    weighted_avg_left = 0
    weighted_avg_nose = 0
    cv2.imwrite("frame.jpg", image)
    face_landmarks_list= face_recognition.face_landmarks(image)
    
    for face_landmarks in face_landmarks_list:
        weighted_avg_left = (face_landmarks["left_eyebrow"][0][1] + face_landmarks["left_eyebrow"][1][1] + face_landmarks["left_eyebrow"][2][1] + face_landmarks["left_eyebrow"][3][1]) / 4
        weighted_avg_right = (face_landmarks["right_eyebrow"][0][1] + face_landmarks["right_eyebrow"][1][1] + face_landmarks["right_eyebrow"][2][1] + face_landmarks["right_eyebrow"][3][1]) / 4
        weighted_avg_nose = (face_landmarks["nose_bridge"][0][1] + face_landmarks["nose_bridge"][1][1] + face_landmarks["nose_bridge"][2][1] + face_landmarks["nose_bridge"][3][1]) / 4
    weighted_avg_brows = (weighted_avg_left + weighted_avg_right) / 2
    
    brow_distance = weighted_avg_nose - weighted_avg_brows

    return brow_distance

def capture_default_face(default_image):
    cv2.imwrite("defaultframe_neutral.jpg", default_image)
    face_landmarks_list_d = face_recognition.face_landmarks(default_image)
    
    for face_landmarks in face_landmarks_list_d:
        weighted_avg_left_d = (face_landmarks["left_eyebrow"][0][1] + face_landmarks["left_eyebrow"][1][1] + face_landmarks["left_eyebrow"][2][1] + face_landmarks["left_eyebrow"][3][1]) / 4
        weighted_avg_right_d = (face_landmarks["right_eyebrow"][0][1] + face_landmarks["right_eyebrow"][1][1] + face_landmarks["right_eyebrow"][2][1] + face_landmarks["right_eyebrow"][3][1]) / 4
        weighted_avg_nose_d = (face_landmarks["nose_bridge"][0][1] + face_landmarks["nose_bridge"][1][1] + face_landmarks["nose_bridge"][2][1] + face_landmarks["nose_bridge"][3][1]) / 4
    weighted_avg_brows_d = (weighted_avg_left_d + weighted_avg_right_d) / 2
    
    global brow_distance_d_def
    brow_distance_d_def = weighted_avg_nose_d - weighted_avg_brows_d
    default_loaded = True
    return default_loaded

def capture_raised_face(raised_image):
    cv2.imwrite("defaultframe_neutral.jpg", raised_image)
    face_landmarks_list_d = face_recognition.face_landmarks(raised_image)
    
    for face_landmarks in face_landmarks_list_d:
        weighted_avg_left_d = (face_landmarks["left_eyebrow"][0][1] + face_landmarks["left_eyebrow"][1][1] + face_landmarks["left_eyebrow"][2][1] + face_landmarks["left_eyebrow"][3][1]) / 4
        weighted_avg_right_d = (face_landmarks["right_eyebrow"][0][1] + face_landmarks["right_eyebrow"][1][1] + face_landmarks["right_eyebrow"][2][1] + face_landmarks["right_eyebrow"][3][1]) / 4
        weighted_avg_nose_d = (face_landmarks["nose_bridge"][0][1] + face_landmarks["nose_bridge"][1][1] + face_landmarks["nose_bridge"][2][1] + face_landmarks["nose_bridge"][3][1]) / 4
    weighted_avg_brows_d = (weighted_avg_left_d + weighted_avg_right_d) / 2
    
    global brow_distance_d_raised
    brow_distance_d_raised = weighted_avg_nose_d - weighted_avg_brows_d
    raised_loaded = True
    return raised_loaded

def eyebrow_raised_bool(are_brows_lifted):
    return are_brows_lifted


# MAIN GAME LOOP
while not done:


    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # Add load events here
    pygame.display.update()

    start_time = pygame.time.get_ticks()
    screen.blit(start_img, (50,100))
    
    if(start_game == False):
        if pygame.time.get_ticks() > 2000:
            screen.fill(white)
            screen.blit(instr_neutral_img, (50,100))
            pygame.display.update()
        if pygame.time.get_ticks() > 5000:
            screen.fill(white)
            screen.blit(num5_img, (300,50))
            pygame.display.update()
        if pygame.time.get_ticks() > 6000:
            screen.fill(white)
            screen.blit(num4_img, (300,50))
            pygame.display.update()
            # LOADING DEFAULT FACE IMAGE
            load_default = True
        if pygame.time.get_ticks() > 7000:
            screen.fill(white)
            screen.blit(num3_img, (300,50))
            pygame.display.update()
        if pygame.time.get_ticks() > 8000:
            screen.fill(white)
            screen.blit(num2_img, (300,50))
            pygame.display.update()
        if pygame.time.get_ticks() > 9000:
            screen.fill(white)
            screen.blit(num1_img, (300,50))
            pygame.display.update()
        if pygame.time.get_ticks() > 10000:
            screen.fill(white)
            screen.blit(instr_raise_img, (50,100))
            pygame.display.update()
        if pygame.time.get_ticks() > 12000:
            screen.fill(white)
            screen.blit(num5_img, (300,50))
            pygame.display.update()
        if pygame.time.get_ticks() > 13000:
            screen.fill(white)
            screen.blit(num4_img, (300,50))
            pygame.display.update()
        if pygame.time.get_ticks() > 14000:
            screen.fill(white)
            screen.blit(num3_img, (300,50))
            pygame.display.update()
            load_raised = True
        if pygame.time.get_ticks() > 15000:
            screen.fill(white)
            screen.blit(num2_img, (300,50))
            pygame.display.update()
        if pygame.time.get_ticks() > 16000:
            screen.fill(white)
            screen.blit(num1_img, (300,50))
            pygame.display.update()
    else:
        screen.fill(white)

        if are_brows_lifted:
            color = (0,128,255)
            screen.fill(color)
            screen.blit(bend_img, (200,200))
        else:
            color = (255, 100, 0)
            screen.fill(color)
            screen.blit(stand_img, (200,200))


    #pygame.draw.rect(screen,color,pygame.Rect(30,30,60,60))
    #pygame.draw.rect(screen,(50,205,50),pygame.Rect(100,100,60,60))


    pygame.display.flip()

    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (whcih OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)

        image = rgb_small_frame

        if (not default_loaded) and load_default:
            default_loaded = capture_default_face(image)

        if not raised_loaded and load_raised:
            raised_loaded = capture_raised_face(image)

        if default_loaded and raised_loaded:
            are_brows_lifted = False
            start_game = True
            unique_brow_raise = brow_distance_d_raised - brow_distance_d_def
            frame_brow_distance = capture_frame_face(image)
            #print(frame_brow_distance)
            #print(unique_brow_raise)
            if frame_brow_distance > unique_brow_raise + brow_distance_d_def - 2.3:
                are_brows_lifted = True
            else:
                are_brows_lifted = False
            if(are_brows_lifted):
                print("Brows Lifted")
                
    process_this_frame = not process_this_frame

    #cv2.imshow('Video', frame)



   

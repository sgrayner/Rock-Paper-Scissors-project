import cv2
import random
from keras.models import load_model
import numpy as np
import time
model = load_model('Rock_paper_scissors_project/keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def play():

    def get_computer_choice():
        computer_choice = random.choices(['rock', 'paper', 'scissors'])[0]
        return computer_choice

    def get_prediction():
        print('Show either a rock, paper or scissors sign to your camera')
        start_time = time.time()
        message = ''
        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            #print(prediction)
            elapsed = time.time() - start_time
            if elapsed <= 1 and message != '5 seconds remaining!':
                message = '5 seconds remaining!'
                print(message)
            elif elapsed <= 2 and elapsed > 1 and message != '4 seconds remaining!':
                message = '4 seconds remaining!'
                print(message)
            elif elapsed <= 3 and elapsed > 2 and message != '3 seconds remaining!':
                message = '3 seconds remaining!'
                print(message)
            elif elapsed <= 4 and elapsed > 3 and message != '2 seconds remaining!':
                message = '2 seconds remaining!'
                print(message)
            elif elapsed <= 5 and elapsed > 4 and message != '1 second remaining!':
                message = '1 second remaining!'
                print(message)
            elif elapsed > 5 and message != 'End':
                message = 'End'
                print(message)
                sign = np.argmax(prediction)
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        signs = ['You chose scissors', 'You chose paper', 'You chose rock', 'Try again']
        print(signs[sign])
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        return signs[sign]

    def get_winner(computer_choice, user_choice):
        if computer_choice == 'rock' and user_choice == 'You chose scissors' or computer_choice == 'scissors' and user_choice == 'You chose paper' or computer_choice == 'paper' and user_choice == 'You chose rock':
            print('You lost!')

        elif user_choice == 'You chose rock' and computer_choice == 'scissors' or user_choice == 'You chose scissors' and computer_choice == 'paper' or user_choice == 'You chose paper' and computer_choice == 'rock':
            print('You won!')

        elif user_choice == 'Try again':
            print('Your sign was not recognised, try again')

        else:
            print('It is a tie')

    
    user_choice = get_prediction()
    computer_choice = get_computer_choice()
    print('The computer chose ', computer_choice)
    get_winner(computer_choice, user_choice)

play()
    




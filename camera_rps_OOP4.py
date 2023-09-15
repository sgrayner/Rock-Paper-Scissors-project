import cv2
import random
import time
import numpy as np
from keras.models import load_model

model = load_model('Rock_paper_scissors_project/keras_model.h5')

class RPS:
    '''
    This class is used to contain the methods to run the rock-paper-scissors game.
    
    Attributes:
        user_wins (int): The number of rounds the user has won
        computer_wins (int): The number of rounds the computer has won
    '''
    def __init__(self, user_wins, computer_wins):
        self.user_wins = user_wins
        self.computer_wins = computer_wins

    def get_computer_choice(self):
        '''
        This function is used to generate the computer's choice of sign.
        
        Returns:
            str: a random string out of rock, paper or scissors.
        '''
        computer_choice = random.choices(['rock', 'paper', 'scissors'])[0]
        return computer_choice

    def get_prediction(self):
        '''
        This function is used to retrieve the users sign based on visual 
        input from a camera.
        
        Returns:
            str: the sign detected from the user, either rock, paper, scissors 
            or 'Try again'.
        '''
        cap = cv2.VideoCapture(0)
        
        #This code is obtaining visual input from the user using their camera.

        while True:
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) 
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            
            # This code is running a countdown giving the user 5 seconds to make their choice.

            print('Show either a rock, paper or scissors sign to your camera')
            start_time = time.time()
            message = ''
            while True:
                elapsed = int(time.time() - start_time)
                if elapsed == 0 and message != '5 seconds remaining!':
                    message = '5 seconds remaining!'
                    print(message)
                elif elapsed == 1 and message != '4 seconds remaining!':
                    message = '4 seconds remaining!'
                    print(message)
                elif elapsed == 2 and message != '3 seconds remaining!':
                    message = '3 seconds remaining!'
                    print(message)
                elif elapsed == 3 and message != '2 seconds remaining!':
                    message = '2 seconds remaining!'
                    print(message)
                elif elapsed == 4 and message != '1 second remaining!':
                    message = '1 second remaining!'
                    print(message)
                elif elapsed >= 5:
                    sign = np.argmax(prediction)
                    break
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break
            signs = ['scissors', 'paper', 'rock', 'Try again']
            # After the loop release the cap object
            cap.release()
            # Destroy all the windows
            cv2.destroyAllWindows()

            return signs[sign]

    def get_winner(self, computer_choice, user_choice):
        '''
        This function is used to determine who has won each round of the game.
        
        Parameters:
            computer_choice (str): The choice of sign made by the computer
            user_choice (str): The choice of sign made by the user
        '''
        if computer_choice == 'rock' and user_choice == 'scissors'\
            or computer_choice == 'scissors' and user_choice == 'paper'\
            or computer_choice == 'paper' and user_choice == 'rock':
            self.computer_wins += 1
            print('You lost this round!')
        elif user_choice == 'rock' and computer_choice == 'scissors'\
            or user_choice == 'scissors' and computer_choice == 'paper'\
            or user_choice == 'paper' and computer_choice == 'rock':
            self.user_wins += 1
            print('You won this round!')
        elif user_choice == 'Try again':
            print('Your sign was not recognised, try again')
        else:
            print('This round is a tie')

    def play(self):   
        '''
        This function is used to keep track of how many rounds have been played,
        as well as calling the other methods in the game and checking if the
        user choice is valid.
        '''
        round_number = 0
        while self.user_wins < 3 and self.computer_wins < 3:
            round_number += 1
            print(f'Round {round_number}!')
            input('Press Enter to start the round...')
            user_choice = self.get_prediction()
            if user_choice != 'Try again':
                print(f'You chose {user_choice}')
                computer_choice = self.get_computer_choice()
                print(f'The computer chose {computer_choice}')
            self.get_winner(computer_choice, user_choice)
        if self.user_wins == 3:
            print('Congratulations, you have won three rounds! You win!')
        else:
            print('The computer has won three rounds, you lose!')

if __name__ == '__main__':
    game = RPS(0, 0).play()
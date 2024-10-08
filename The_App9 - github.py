##
# TO DISTRIBUTE THIS AS AN APP, REMOVED THE TERMINAL NOTIFICATIONS, AND CREATED A NOTIFICATION WINDOW INSTEAD

import cv2
import time
import os
from datetime import datetime
import requests
import pandas as pd
from io import StringIO
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
import tkinter as tk
import json
from tkinter import messagebox
import sys

# Temporarily redirect standard output to null
with open(os.devnull, 'w') as f:
    old_stdout = sys.stdout
    sys.stdout = f

    # Import pygame here
    import pygame

    # Restore standard output
    sys.stdout = old_stdout
# from threading import Timer
duration = 3000


def show_notification(message, duration=3000):
    notification_root = tk.Tk()
    notification_root.geometry("500x300")  # Size of the notification window

    # Center the window on the screen
    screen_width = notification_root.winfo_screenwidth()
    screen_height = notification_root.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (500 / 2))
    y_coordinate = int((screen_height / 2) - (300 / 2))
    notification_root.geometry(f"+{x_coordinate}+{y_coordinate}")

    notification_root.overrideredirect(True)
    tk.Label(notification_root, text=message, font=('Helvetica', 14), wraplength=280).pack(expand=True, padx=20,
                                                                                           pady=20)
    notification_root.after(duration, notification_root.destroy)  # Auto-close after duration
    notification_root.mainloop()


submit_and_exit = False
start_clicked = False

print('All required modules are installed! Thank you for your patience.')
show_notification("All required modules are installed! \n\n Thank you for your patience!", duration)

# DOWNLOAD THE LINKS

try:
    # ACCESS TO GOOGLE CREDENTIALS
    credentials_share_link = 'paste the link here'
    credentials_id = credentials_share_link.split('/')[5]
    direct_link = f'paste the link here={credentials_id}'
    response = requests.get(direct_link)
    json_string = response.text
    credentials_dict = json.loads(json_string)
except:
    # BACK UP ACCESS TO GOOGLE CREDENTIALS
    credentials_share_link = 'paste the link here'
    credentials_id = credentials_share_link.split('/')[5]
    direct_link = f'paste the link here={credentials_id}'
    response = requests.get(direct_link)
    json_string = response.text
    credentials_dict = json.loads(json_string)
# except:
#     pass
# # Specify the path to your local JSON file
# local_json_file_path = r"C:\Users\corec\Codes\video_rating_app\ml-osats-rating-serviceaccnt-credentials.json"
#
# # Load the JSON data from the local file
# with open(local_json_file_path, 'r') as file:
#     credentials_dict = json.load(file)

##
# Define users with their passwords
users = {
    'USERNAME1': 'PASSWORD1',
    'USERNAME2': 'PASSWORD2',
    }

# Function to check login credentials
def check_login(event=None):
    username = username_entry.get()
    password = password_entry.get()

    if username in users and users[username] == password:
        # Find the user's number based on the username
        global Rater
        Rater = list(users.keys()).index(username) + 1  # +1 to make the count start at 1 instead of 0
        login_window.destroy()  # Close the login window
        show_notification("Successful login!", duration)
        print('Successful login!')
    else:
        messagebox.showerror("Login Failed", "Invalid username or password. Please use capital letters.")


# Function to handle window close event
def on_close():
    print("User closed the window without logging in.")
    sys.exit(0)  # Exit the application


# Create the login window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("500x280")  # Width x Height

screen_width = login_window.winfo_screenwidth()
screen_height = login_window.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (400 / 2))
y_coordinate = int((screen_height / 2) - (200 / 2))
login_window.geometry(f"+{x_coordinate}+{y_coordinate}")

# Add space above the username entry
space_label = tk.Label(login_window, height=2)  # Height is in text lines
space_label.pack()

# Configure the close window protocol
login_window.protocol("WM_DELETE_WINDOW", on_close)

font_specs = ("Helvetica", 16)

# Username entry
username_label = tk.Label(login_window, text="Username:", font=font_specs)
username_label.pack()
username_entry = tk.Entry(login_window, font=font_specs)
username_entry.pack(pady=(0, 20))  # Increase padding for more space
username_entry.focus()

# Password entry
password_label = tk.Label(login_window, text="Password:", font=font_specs)
password_label.pack()
password_entry = tk.Entry(login_window, show="*", font=font_specs)
password_entry.pack(pady=(0, 20))  # Increase padding for more space

# Login button
login_window.bind('<Return>', check_login)
login_button = tk.Button(login_window, text="Login", command=check_login, font=font_specs)
login_button.pack()

login_window.mainloop()

# data = StringIO(response.text)
# credentials_df = pd.read_csv(data, header=None)
# credentials_dict = credentials_df.to_dict(orient='records')
# # If the DataFrame has only one row, you might want just the first record
# credentials_dict = credentials_dict[0] if credentials_dict else {}

""" # # # # # RATER SPECIFIC ACCESS TO GOOGLE DRIVE FOLDER WITH VIDEO LINKS # # # # # """
if Rater == 1:
    share_link = 'paste the link here'  # RATER 1
elif Rater == 2:
    share_link = 'paste the link here'  # RATER 2
elif Rater == 3:
    share_link = 'paste the link here'  # RATER 3
elif Rater == 4:
    share_link = 'paste the link here'  # RATER 4
elif Rater == 5:
    share_link = 'paste the link here'  # RATER 5
elif Rater == 6:
    share_link = 'paste the link here'  # RATER 6
elif Rater == 7:
    share_link = 'paste the link here'  # RATER 7
elif Rater == 8:
    share_link = 'paste the link here'  # RATER 8
elif Rater == 9:
    share_link = 'paste the link here'  # RATER 9
elif Rater == 10:
    share_link = 'paste the link here'  # RATER 10

audiofiles_link = 'paste the link here'  # this file all the names of the videos with audio files
# if there is no name for that video file, no audio will play for that video

# Extract the file ID from the link
video_ids = share_link.split('/')[5]
# Convert to a direct download link
direct_link = f'https://drive.google.com/uc?id={video_ids}'

audio_ids = audiofiles_link.split('/')[5]
audiofiles_direct_link = f'https://drive.google.com/uc?id={audio_ids}'

# Download the file content
response = requests.get(direct_link)
audio_response = requests.get(audiofiles_direct_link)

# Check if the request was successful
if response.status_code == 200:
    data = StringIO(response.text)
    df = pd.read_csv(data)
    data = StringIO(audio_response.text)
    audio_df = pd.read_csv(data)
    show_notification("Now we have access to the video links!", duration)
    print('Now we have access to the video links!')
else:
    show_notification("Failed to download the file.", duration)
    print('Failed to download the file.')


def hersey(df, audio_df, R, video_name, N, Total, T):
    global rating_given, rating_file, frame_count, start_time
    video_url = f'https://drive.google.com/uc?id={R}'

    ##
    # DOWNLOAD THE VIDEO FROM CLOUD
    show_notification("Downloading the next video! This may take long...", duration)
    print('\nDownloading the video! Please wait...')

    response = requests.get(video_url)
    with open(f'temp_video.mp4', 'wb') as file:
        file.write(response.content)

    try:
        # Download audio in case the video had an audio
        # Find the id for the row where 'name' matches video_name
        video_name = video_name[
                     :-4]  # remove the .mp4 extension and compare it to audio file name without .mp3 extension
        matching_id = audio_df.loc[audio_df['name'].str[:-4] == video_name, 'id'].values[0]

        direct_link = f'https://drive.google.com/uc?id={matching_id}'
        response = requests.get(direct_link)
        with open(f'temp_audio.mp3', 'wb') as file:
            file.write(response.content)
        local_audio_path = os.path.abspath(f'temp_audio.mp3')
    except:
        pass

    # Get the full path of the local video file
    local_video_path = os.path.abspath(f'temp_video.mp4')

    # START WINDOW
    # Create the main window, only at the beginning of the session
    if T == 0:
        root = tk.Tk()
        root.title("Start Application")


        # Get the screen dimension
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Find the center position
        width = 800
        height = 300
        center_x = int(screen_width / 2 - width / 2)
        center_y = int(screen_height / 2 - height / 2)

        # Set the position of the window to the center of the screen
        root.geometry(f'{width}x{height}+{center_x}+{center_y}')

        def on_start_button_click():
            global start_clicked
            start_clicked = True
            # This function is called when the Start/Continue button is clicked
            # Add your logic here to start or continue the app
            print("Starting or continuing the application...")
            root.destroy()  # This will close the window

        # Add a "Ready?" label above the button
        ready_label = tk.Label(root, text="Ready?", font=("Helvetica", 25))
        ready_label2 = tk.Label(root, text=f"So far, {N} of {Total} videos are completed.", font=("Helvetica", 20))
        ready_label.pack(expand=True, anchor=tk.CENTER)
        ready_label2.pack(expand=True, anchor=tk.CENTER)

        # Create the Start/Continue button
        start_button = tk.Button(root, text="Start/Continue", font=("Helvetica", 20), command=on_start_button_click)
        start_button.pack(expand=True)
        # Start the GUI event loop
        root.mainloop()

        if not start_clicked:
            show_notification("Application closed. Exiting...", duration)
            print("Application closed without starting.")
            sys.exit()  # Exit the application

    # Function to calculate the new size maintaining the aspect ratio
    def get_new_size(screen_width, screen_height, original_width, original_height):
        screen_ratio = screen_width / screen_height
        video_ratio = original_width / original_height

        if video_ratio > screen_ratio:
            # Width is the limiting factor
            new_width = screen_width
            new_height = int(screen_width / video_ratio)
        else:
            # Height is the limiting factor
            new_height = screen_height
            new_width = int(screen_height * video_ratio)

        return new_width, new_height

    # Initialize Pygame for audio playback
    pygame.mixer.init()

    try:
        # Load the audio
        pygame.mixer.music.load(f'temp_audio.mp3')
    except:
        pass

    # Function to handle mouse events
    def click_event(event, x, y, flags, params):
        global rating_given, rating_file, frame_count, start_time
        if event == cv2.EVENT_LBUTTONDOWN:
            # Check if the click is within the button y-range
            if 50 <= y <= 150:
                button_width = 170  # Width of each button
                gap = 10  # Gap between buttons
                for i in range(7):
                    x_start = 50 + i * (button_width + gap)
                    x_end = x_start + button_width
                    if x_start <= x <= x_end:
                        rating = ["Excellent", "Very Good", "Good", "Average", "Below Average", "Poor", "Very Poor"][i]
                        print(f"Rated: {rating} at frame {frame_count}")
                        # Record video_id, frame number, and the rating in the file
                        rating_file.write(f"VideoID, {R}, Frame, {frame_count}, Rating, {rating}\n")
                        rating_given = True
                        start_time += time.time() - (
                                start_time + frame_count / frame_rate)  # Adjust start_time for the delay
                        break  # Break the loop once a valid rating is given

    # Get the screen size
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()

    cap = cv2.VideoCapture(local_video_path)

    if not cap.isOpened():
        show_notification("Error: Could not open video.", duration)
        print("Error: Could not open video.")
        exit()

    # Get original video dimensions
    original_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    original_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # Calculate the aspect ratios
    screen_ratio = screen_width / screen_height
    video_ratio = original_width / original_height

    # Calculate new window size
    new_width, new_height = get_new_size(screen_width, screen_height, original_width, original_height)

    # Define a tolerance for aspect ratio matching
    tolerance = 0.05

    if abs(screen_ratio - video_ratio) <= tolerance:
        # Aspect ratios are close enough, use fullscreen
        cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    else:
        # Aspect ratios differ, resize and centralize window
        new_width, new_height = get_new_size(screen_width, screen_height, original_width, original_height)
        cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Video", new_width, new_height)
        x_position = (screen_width - new_width) // 2
        y_position = (screen_height - new_height) // 2
        cv2.moveWindow("Video", x_position, y_position)  # Center the window

    cv2.setMouseCallback("Video", click_event)
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    rating_frame_interval = round(15 * frame_rate)  # seconds * frame_rate
    frame_count = 0
    rating_given = False
    start_time = time.time()

    # Create a unique filename for the ratings file
    unique_filename = datetime.now().strftime("ratings_%Y%m%d_%H%M%S.txt")
    rating_file = open(unique_filename, "w")

    try:
        pygame.mixer.music.play()
    except:
        pass

    while True:
        if not rating_given:
            ret, frame = cap.read()
            if not ret:
                break

        frame_count += 1
        expected_time = start_time + (frame_count / frame_rate)

        # Draw the "buttons" on the frame if it's time for rating
        if frame_count % rating_frame_interval == 0 and not rating_given:  # Every rating_frame_interval frames, a rating will be asked
            # Define button colors and labels
            colors = [(0, 255, 0), (127, 255, 0), (255, 255, 0), (255, 0, 0), (128, 0, 128), (64, 0, 192), (0, 0, 255)]
            labels = ["Excellent", "Very Good", "Good", "Average", "Below Average", "Poor", "Very Poor"]
            button_width = 170  # Width of each button
            gap = 10  # Gap between buttons

            for i, (color, label) in enumerate(zip(colors, labels)):
                x_start = 50 + i * (button_width + gap)
                cv2.rectangle(frame, (x_start, 50), (x_start + button_width, 150), color, -1)
                cv2.putText(frame, label, (x_start + 10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            try:
                pygame.mixer.music.pause()
            except:
                pass

            while not rating_given and frame_count % rating_frame_interval == 0:
                cv2.imshow("Video", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    pygame.mixer.quit()
                    cap.release()
                    cv2.destroyAllWindows()
                    break

        if rating_given:
            try:
                pygame.mixer.music.unpause()
            except:
                pass
            rating_given = False

        # Wait until the expected time to display the frame, to achieve normal speed display
        while time.time() < expected_time:
            time.sleep(0.001)

            cv2.imshow("Video", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            pygame.mixer.quit()
            cap.release()
            cv2.destroyAllWindows()
            break

    pygame.mixer.quit()
    cap.release()
    cv2.destroyAllWindows()
    rating_file.write(f"Successful completion of VideoID, {R}\n")
    rating_file.close()
    cap = None

    # UPLOAD THE RATINGS TO THE CLOUD
    credentials_json = json.dumps(credentials_dict)

    """ # # # # # Rater specific folder_ID //  F O R   R A T E R - X # # # # # """
    if Rater == 1:
        folder_id = 'paste the link here'  # RATER 1
    elif Rater == 2:
        folder_id = 'paste the link here'  # RATER 2
    elif Rater == 3:
        folder_id = 'paste the link here'  # RATER 3
    elif Rater == 4:
        folder_id = 'paste the link here'  # RATER 4
    elif Rater == 5:
        folder_id = 'paste the link here'  # RATER 5
    elif Rater == 6:
        folder_id = 'paste the link here'  # RATER 6
    elif Rater == 7:
        folder_id = 'paste the link here'  # RATER 7
    elif Rater == 8:
        folder_id = 'paste the link here'  # RATER 8
    elif Rater == 9:
        folder_id = 'paste the link here'  # RATER 9
    elif Rater == 10:
        folder_id = 'paste the link here'  # RATER 10

    credentials = service_account.Credentials.from_service_account_info(json.loads(credentials_json))
    # Create the service client
    service = build('drive', 'v3', credentials=credentials)

    # File to upload
    file_path = os.getcwd()
    file_path = os.path.join(file_path, unique_filename)
    file_metadata = {'name': unique_filename, 'parents': [folder_id]}
    media = MediaFileUpload(file_path, mimetype='text/plain')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"Your ratings are uploaded successfully to the cloud as {unique_filename}")

    ##
    # SIX-ITEM OSATS RATING

    def create_rating_scale(master, row, category, ratings, font_size, buttons):
        """Create a row of rating scale (buttons with descriptive labels) for a given category."""
        # Category label
        label = tk.Label(master, text=category, font=("Helvetica", font_size))
        label.grid(row=row, column=1)

        # Function to handle button click
        def button_click(button):
            # Reset all buttons in this category
            for btn in buttons[category]:
                btn.config(bg="SystemButtonFace",
                           text=btn['text'].replace("✓ ", ""))  # Remove checkmark and reset color
            # Mark the clicked button as selected/deselected
            if "✓" not in button['text']:
                button.config(bg="dark green", text=f"✓ {button['text']}")  # Darker color and add checkmark
                selected_ratings[category] = button['text'].replace("✓ ", "")
            else:
                button.config(bg="SystemButtonFace", text=button['text'].replace("✓ ", ""))  # Reset to default
                selected_ratings[category] = None

        # Create buttons for each rating
        buttons[category] = []
        for i, rating in enumerate(ratings, start=2):
            # Set a fixed width for buttons
            button_width = max(
                len(str(r)) for r in ratings) + 2  # Calculate width based on rating length + space for checkmark
            button = tk.Button(master, text=str(rating), font=("Helvetica", font_size), width=button_width)
            button.grid(row=row, column=i, padx=2)
            button.config(command=lambda btn=button: button_click(btn))
            buttons[category].append(button)

    def center_window(root, width, height):
        """Center the window on the screen."""
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    def submit_and_close(selected_ratings, filename, root, folder_id, video_id, n):
        global submit_and_exit

        # Check if all categories have been rated
        if None in selected_ratings.values():
            messagebox.showwarning("Incomplete Ratings", "Please rate all categories before submitting.")
            return

        """Save the ratings and close the window."""
        with open(f"SixItems{filename}", "w") as file:
            for category, rating in selected_ratings.items():
                file.write(f"{category}: {rating}\n")
            file.write(f"VideoID, {video_id}")

        # Upload to the cloud
        file_path = os.getcwd()
        file_path = os.path.join(file_path, f'SixItems{filename}')
        file_metadata = {'name': f'SixItems{filename}', 'parents': [folder_id]}
        media = MediaFileUpload(file_path, mimetype='text/plain')
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f"Your ratings are uploaded successfully to the cloud as SixItems{filename}")
        try:
            root.destroy()
        except tk.TclError:
            pass  # Window is already closed, do nothing

        if n:
            submit_and_exit = True

    # Create the main window
    root = tk.Tk()
    root.title("Rating Scale")

    # Set window size and center it
    window_width = 1400
    window_height = 400
    center_window(root, window_width, window_height)

    # Categories, Ratings, Font Size, Buttons Dictionary, and Selected Ratings
    categories = ['Respect for Tissue', 'Hemostasis', 'Instrument Handling', 'Economy of Movement', 'Flow', 'Overall']
    ratings = ["Excellent", "Very Good", "Good", "Average", "Below Average", "Poor", "Very Poor"]
    font_size = 11
    buttons = {}
    selected_ratings = {category: None for category in categories}

    # Configure the grid for vertical centering
    total_rows = len(categories) + 10
    for i in range(total_rows):
        root.grid_rowconfigure(i, weight=1)

    # Empty column configuration for horizontal centering
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(len(ratings) + 2, weight=1)

    # Creating a row for each category
    for i, category in enumerate(categories):
        create_rating_scale(root, i + 1, category, ratings, font_size, buttons)

    # SUBMIT AND CONTINUE button to save the ratings and continue to the next video
    submit_button = tk.Button(root, text="Submit and Continue", font=("Helvetica", 10),
                              command=lambda: submit_and_close(selected_ratings, unique_filename, root, folder_id,
                                                               R, False))
    submit_button.grid(row=total_rows - 1, column=1, sticky="e", padx=10, pady=10)

    # SUBMIT AND EXIT button to save the ratings and close the application
    submit_and_exit_button = tk.Button(root, text="Submit and Exit", font=("Helvetica", 10),
                                       command=lambda: submit_and_close(selected_ratings, unique_filename, root,
                                                                        folder_id, R, True))
    submit_and_exit_button.grid(row=total_rows - 1, column=len(ratings) + 2, sticky="w", padx=10, pady=10)

    # Start the GUI event loop
    root.mainloop()

    ##
    # UPDATE THE VIDEO LINK CSV FILE
    # modify the file and save the modified file locally
    df.loc[0, "where_we_left"] = N
    df.to_csv('drive_files_20240117_125440.csv', index=False)
    try:
        # upload the locally saved file
        file_metadata = {'name': 'drive_files_20240117_125440.csv'}
        media = MediaFileUpload('drive_files_20240117_125440.csv', mimetype='text/csv')

        updated_file = service.files().update(fileId=video_ids, body=file_metadata, media_body=media).execute()

        show_notification(f"Your records on the cloud are succcesfully updated", duration)
        print(f"Your records are updated on this cloud file: drive_files_20240117_125440.csv")
    except:
        show_notification(f"There was an error that prevented updating your records on the cloud", duration)
        print(f"There was an error that prevented updating your records on the cloud")


# Read where we left from the .csv file
N = int(df.where_we_left[0])  # Read and convert N to an integer
T = -1  # To track the number of ratings done in this session

for R, video_name in zip(df['id'][N + 1:], df['name'][N + 1:]):
    N = N + 1  # In the .csv file start where_we_left from -1, so that the very first reading starts from 0
    T = T + 1
    if submit_and_exit:
        break

    # DELETE THE TEMPORARY VIDEO AND AUDIO FILES
    file_path = os.getcwd()
    try:
        os.remove(os.path.join(file_path,
                               f'temp_video.mp4'))
        # print(f"Previous temporary video file is successfully deleted.")
        os.remove(os.path.join(file_path, f'temp_audio.mp3'))
        # print(f"Previous temporary audio file is successfully deleted.")
    except OSError as e:
        print()
        # print(f"Error at deleting the temporary files.")
        # print(f"Error: {e.filename} - {e.strerror}.")

    print(f"Working on videoID: {R}")
    hersey(df, audio_df, R, video_name, N, len(df), T)

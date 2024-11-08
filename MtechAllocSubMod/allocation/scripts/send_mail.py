import requests
import time

def send_clashmail(student_data, professor):
    # Deployment URL of the Google Apps Script Web App
    deployment_url = 'https://script.google.com/macros/s/AKfycbxK6BCSTHbgrQhixbw2PaLUYskRekV5h7sBV_B29pbCL7Y0BERWR5rWP2GzWGwoCt50zw/exec'

    professor_email = 'rohithraichu@gmail.com'

    payload = {
        'action': 'createForm',
        'students': student_data,
        'email': professor_email
    }

    print(student_data)

    # Send request to create the form
    response = requests.post(deployment_url, json=payload)
    print("Form Creation Response -> ", response.text)  # This will print the form URL

    # Send GET request to retrieve the selected student
    start_time = time.time()
    hello_count = 0
    while True:
        time.sleep(1)
        print("buffer")

        # Check if 10 seconds have passed
        if time.time() - start_time >= 10 and hello_count < 2:
            reponse = requests.post(deployment_url, json={'action': 'sendReminder'})
            print(reponse.text)
            hello_count += 1
            start_time = time.time()  # Reset the timer
            if hello_count == 2:
                print("Max number of reminders have been sent!")

        payload = {'action': 'getFormResponse'}
        response = requests.post(deployment_url, json=payload)
        print("Form Response -> ", response.text)  # This will print the selected student
        if response.text == "No responses found.":
            continue
        else:
            selected_student = response.text
            break

    payload = {'action' : 'resetForm'}
    response = requests.post(deployment_url, json=payload)
    print("Form has been reset/deleted!")

    return selected_student

    

    



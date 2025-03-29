from datetime import date
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import os
import mysql.connector
import bcrypt
import hashlib
import pickle
import joblib
from flask_session import Session
# from flask import session
import pickle
import numpy as np





symp = [
    'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering',
    'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue',
    'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_urination',
    'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings',
    'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level',
    'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration',
    'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite',
    'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea',
    'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload',
    'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision',
    'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose',
    'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate',
    'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
    'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity',
    'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid',
    'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts',
    'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain',
    'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness',
    'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
    'loss_of_smell', 'bladder_discomfort', 'foul_smell_of_urine', 'continuous_feel_of_urine',
    'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression',
    'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
    'abnormal_menstruation', 'dischromic_patches', 'watering_from_eyes', 'increased_appetite',
    'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration',
    'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections',
    'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption',
    'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking',
    'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting',
    'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
    'yellow_crust_ooze','prognosis'
]



prognosis = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
    'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma',
    'Hypertension', 'Migraine', 'Cervical spondylosis', 'Paralysis (brain hemorrhage)',
    'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
    'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis',
    'Tuberculosis', 'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
    'Heart attack', 'Varicose veins', 'Hypothyroidism', 'Hyperthyroidism',
    'Hypoglycemia', 'Osteoarthritis', 'Arthritis', '(vertigo) Paroxysmal Positional Vertigo',
    'Acne', 'Urinary tract infection', 'Psoriasis', 'Impetigo'
]





app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'disease_pred'
app.config['MYSQL_PORT'] = 3306  # Default MySQL port
app.config['MYSQL_SSL_DISABLED'] = False  


'''app.config['MYSQL_HOST'] = 'localhost'  # Host where MySQL is running (localhost for local setup)
app.config['MYSQL_USER'] = 'root'  # MySQL user (root is default on local setups)
app.config['MYSQL_PASSWORD'] = ''  # Password for root (empty if no password is set)
app.config['MYSQL_DB'] = 'healthcare'  # The name of the database you want to connect to
app.config['MYSQL_PORT'] = 3306  # Default MySQL port
app.config['MYSQL_SSL_DISABLED'] = False  # Set to True if you want to disable SSL (usually False for local setups)
'''


mysql = MySQL(app)



@app.route("/")  # this sets the route to this page
def home():

    return render_template("index.html")
# Flask application file


model = joblib.load(open("model.pkl", "rb"))

print(type(model))  # Should output something like <class 'sklearn.tree._classes.DecisionTreeClassifier'>

#@app.route("/predict", methods=["POST", 'GET'])
#def predict():
#    if request.method == "POST":
#        # Get the selected symptoms from the form data
#        selected_symptoms = request.form.getlist("symptom")
#        print("Selected Symptoms:", selected_symptoms)  # Debugging output
#
#        # Create a binary representation of the selected symptoms
#        symptoms = np.zeros(len(symp))  # Create an array of zeros
#        for i, symptom in enumerate(symp):
#            if symptom in selected_symptoms:
#                symptoms[i] = 1  # Set the corresponding index to 1
#                print(f"Symptoms[{i}] = 1 for {symptom}")  # Debugging output
#
#        print("Symptoms array:", symptoms)  # Check the array structure
#
#        try:
#            # Use the model to make a prediction
#            result = model.predict(symptoms.reshape(1, -1))  # Ensure proper shape
#            print("Model prediction result:", result)  # Debugging output
#            
#            # Since result is a class name, find its index in prognosis
#            prediction = result[0]  # Get the first prediction (class name)
#            prediction_index = prognosis.index(prediction)  # Find the index in prognosis
#            
#            return render_template("predict1.html", result=prognosis[prediction_index])
#        except Exception as e:
#            print("Prediction Error:", str(e))  # Print any error that occurs
#            return render_template("predict1.html", result="Error during prediction.")
#
#    return render_template("predict1.html")
#
#
#print("Number of Features in Symptoms:", len(symp))

@app.route("/predict", methods=["POST", 'GET'])
def predict():
    if request.method == "POST":
        selected_symptoms = request.form.getlist("symptom")
        print(f"Selected Symptoms: {selected_symptoms}")

        if not selected_symptoms:
            return render_template("predict1.html", result="Please select at least one symptom.")

        symptoms = np.zeros(len(symp))  # Initialize the array
        for symptom in selected_symptoms:
            if symptom in symp:
                index = symp.index(symptom)
                symptoms[index] = 1  # Set the index for the selected symptom to 1

        result = model.predict(symptoms.reshape(1, -1))  # Ensure proper shape
        print(f"Model prediction result: {result}")  # Check the model output
        
        # result is expected to be a list of predicted disease names
        if len(result) > 0:  # Check if result is not empty
            predicted_disease = result[0]  # Directly use the predicted disease name
            return render_template("predict1.html", result=f"Predicted Diagnosis: {predicted_disease}")
        else:
            return render_template("predict1.html", result="No prediction made.")

    return render_template("predict1.html")

print("Model feature names:", model.feature_names_in_)














@app.route("/blood")  # this sets the route to this page
def blood():
    return render_template("blood.html")

@app.route("/ngo")  # this sets the route to this page
def ngo():
    return render_template("ngo.html")

@app.route("/add_checkups", methods=['GET', 'POST'])  # this sets the route to this page
def add_checkups():
    #ngo wrk
    if request.method == "POST":
        details = request.form
        ngo_name = details['ngo_name']
        type_check = details['type_check']
        date = details['date']
        time = details['time']

        contact = details['contact']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO add_check(ngo_name, type_check, date,time, contact) VALUES (%s, %s, %s, %s, %s)",
                    (ngo_name, type_check, date,time, contact))
        mysql.connection.commit()
        cur.close()
        # return 'success'

        return '<script>alert("CHECK-UP TYPE ADDED SUCCESFULLY");window.location="/ngo_server"</script>'

    return render_template("add_checkups.html")



@app.route('/ngo_sign_up', methods=['GET', 'POST'])
def ngo_sign_up():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        ngo_name = userDetails['ngo_name']
        type1 = userDetails['type1']
        pass1 = userDetails['pass1']
        number = userDetails['number']

        hashed_password = bcrypt.hashpw(pass1.encode('utf-8'), bcrypt.gensalt())

        # Initialize cursor
        # conn = mysql.connect()
        # cursor = conn.cursor()
        cursor = mysql.connection.cursor()
        # Insert user details into the table
        cursor.execute("INSERT INTO ngo_users(ngo_name, type1, pass1, number) VALUES(%s, %s, %s, %s)", (ngo_name, type1, hashed_password, number))
        mysql.connection.commit()
        cursor.close()

        # Redirect to login page
        return '<script>alert("ngo registered successfully");window.location="/ngo_login"</script>'

    return render_template('ngo_sign_up.html')


@app.route('/ngo_login', methods=['POST','GET'])
def login_post():
    if request.method == 'POST':
        # Get form data
        ngo_name = request.form['ngo_name']
        pass1 = request.form['pass1']

        # Initialize cursor
        cursor = mysql.connection.cursor()

        # Execute the query to check if the user exists
        query = "SELECT * FROM ngo_users WHERE ngo_name = %s"
        cursor.execute(query, (ngo_name,))
        user = cursor.fetchone()

        # Close the cursor
        cursor.close()

        # Check if the user exists and verify the password
        if user and bcrypt.checkpw(pass1.encode('utf-8'), user[1].encode('utf-8')):
            # Create the session
            # session['p_name'] = p_name

            # Redirect the user to a protected page
            return '<script>alert("Logged in successfully");window.location="/ngo_server"</script>'

        else:
            # If the user does not exist or password is incorrect, redirect to login page
            return '<script>alert("Wrong username or password");window.location="/ngo_login"</script>'
    #
    # if request.method == 'POST':
    #     # Get form data
    #     ngo_name = request.form['ngo_name']
    #     pass1 = request.form['pass1']
    #
    #     # Initialize cursor
    #     cursor = mysql.connection.cursor()
    #
    #     # Execute the query to check if the user exists
    #     query = "SELECT * FROM ngo_users WHERE ngo_name = %s"
    #     cursor.execute(query, (ngo_name,))
    #     user = cursor.fetchone()
    #
    #     # Close the cursor
    #     cursor.close()
    #
    #     # Check if the user exists and verify the password
    #     if user and bcrypt.checkpw(pass1.encode('utf-8'), user['pass1']):
    #
    #         # Create the session
    #         session['ngo_name'] = ngo_name
    #
    #         # Redirect the user to a protected page
    #         return '<script>alert("Logged in successfully");window.location="/ngo_server"</script>'
    #
    #     else:
    #         # If the user does not exist or password is incorrect, redirect to login page
    #         return '<script>alert("Wrong username or password");window.location="/ngo_login"</script>'

    return render_template('ngo_login.html')



# @app.route('/ngo_logout')
# def ngo_logout():
#     #clear the session data
#     session.clear()
#     return redirect(url_for('ngo_login'))

@app.route("/ngo_server")
def ngo_server():
    return render_template("ngo_server.html")


#patient sign up
# @app.route("/patient_sign_up" ,methods=['POST','GET'])
# def patient_sign_up():
#     if request.method == 'POST':
#         # Fetch form data
#         userDetails = request.form
#         p_name = userDetails['p_name']
#         email = userDetails['email']
#         pass1 = userDetails['pass']
#         number = userDetails['number']
#         address = userDetails['address']
#
#         hashed_password = bcrypt.hashpw(pass1.encode('utf-8'), bcrypt.gensalt())
#
#         # Initialize cursor
#         # conn = mysql.connect()
#         # cursor = conn.cursor()
#         cursor = mysql.connection.cursor()
#         # Insert user details into the table
#         cursor.execute("INSERT INTO patient_users(p_name, email, pass, number, address) VALUES(%s, %s, %s, %s, %s)",
#                        (p_name, email, hashed_password, number, address))
#         mysql.connection.commit()
#         cursor.close()
#
#         # Redirect to login page
#         return '<script>alert(" Registered successfully");window.location="/user_login"</script>'
#
#     return render_template("patient_sign_up.html")
@app.route("/patient_sign_up" ,methods=['POST','GET'])
def patient_sign_up():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        p_name = userDetails['p_name']
        email = userDetails['email']
        password1 = userDetails['password1']
        number = userDetails['number']
        address = userDetails['address']

        hashed_password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())

        # Initialize cursor
        cursor = mysql.connection.cursor()
        # Insert user details into the table
        cursor.execute("INSERT INTO patient_users(p_name, email, password1, number, address) VALUES(%s,  %s,%s, %s, %s)",
                       (p_name, email, hashed_password, number, address))
        mysql.connection.commit()
        cursor.close()

        # Redirect to login page
        return '<script>alert("Registered successfully");window.location="/patient_login"</script>'

    return render_template("patient_sign_up.html")


#login patient

# @app.route('/patient_login', methods=['GET', 'POST'])
# def patient_login():
#     if request.method == 'POST':
#         #get the form data
#         p_name = request.form['p_name']
#         password1 = request.form['password1']
#
#
#         cur = mysql.connection.cursor()
#         #
#
#        # execute the query to check if the user exists
#         query = "SELECT * FROM patient_users WHERE p_name=%s AND password1=%s"
#         cur.execute(query, (p_name, password1))
#         user = cur.fetchone()
#
#      #   close the cursor and the connection
#         cur.close()
#
#
#         #check if the user exists
#         if user:
#             #create the session
#             session['p_name'] = p_name
#
#             #redirect the user to a protected page
#             return '<script>alert(" Registered successfully");window.location="/"</script>'
#
#         else:
#             #if the user does not exist, redirect the user back to the login page
#             return '<script>alert(" Wrong password");window.location="/patient_login"</script>'
#     return render_template('patient_login.html')
#doc sign
@app.route('/patient_login', methods=['GET', 'POST'])
def patient_login():
    if request.method == 'POST':
        # Get form data
        p_name = request.form['p_name']
        password1 = request.form['password1']

        # Initialize cursor
        cursor = mysql.connection.cursor()

        # Execute the query to check if the user exists
        query = "SELECT * FROM patient_users WHERE p_name = %s"
        cursor.execute(query, (p_name,))
        user = cursor.fetchone()

        # Close the cursor
        cursor.close()

        # Check if the user exists and verify the password
        if user and bcrypt.checkpw(password1.encode('utf-8'), user[4].encode('utf-8')):
            # Create the session
            # session['p_name'] = p_name

            # Redirect the user to a protected page
            return '<script>alert("Logged in successfully");window.location="/"</script>'

        else:
            # If the user does not exist or password is incorrect, redirect to login page
            return '<script>alert("Wrong username or password");window.location="/patient_login"</script>'

    return render_template('patient_login.html')

@app.route("/doc_sign_up" ,methods=['GET', 'POST'])
def doc_sign_up():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        d_name = userDetails['d_name']
        passwrd1 = userDetails['passwrd1']
        email = userDetails['email']
        special = userDetails['special']

        number = userDetails['number']
        address = userDetails['address']

        hashed_password = bcrypt.hashpw(passwrd1.encode('utf-8'), bcrypt.gensalt())

        # Initialize cursor
        # conn = mysql.connect()
        # cursor = conn.cursor()
        cursor = mysql.connection.cursor()
        # Insert user details into the table
        cursor.execute("INSERT INTO doc_user(d_name, email, passwrd1, number, address,special) VALUES(%s, %s, %s, %s, %s, %s)",
                       (d_name, email, hashed_password, number, address, special))
        mysql.connection.commit()
        cursor.close()

        # Redirect to login page
        return '<script>alert(" Registered successfully");window.location="/"</script>'

    return render_template("doc_sign_up.html")





# 



@app.route("/donate", methods=['GET', 'POST'])  # this sets the route to this page blood donation
def donate():
        if request.method == "POST":
            details = request.form
            Name = details['name']
            age = details['age']
            blood_group = details['blood_group']
            past_illness = details['past_illness']
            mobile = details['mobile']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO b_donation(Name, age, blood_group, past_illness, mobile) VALUES (%s, %s, %s, %s, %s)", (Name, age, blood_group, past_illness, mobile))
            mysql.connection.commit()
            cur.close()
            # return 'success'

            return '<script>alert("EVERY DROP MATTERS!! Note:you will get a call within 7 days");window.location="/blood"</script>'

        return render_template('donate.html')


@app.route("/receive")  # this sets the route to this page
def receive():

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM b_donation")
    fetchdata = cur.fetchall()
    cur.close()
    return render_template("receive.html" , data = fetchdata)

@app.route("/doc_list")  # this sets the route to this page
def doc_list():

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM doc_user")
    fetchdata = cur.fetchall()
    cur.close()
    return render_template("doc_list.html" , data = fetchdata)


@app.route("/ngo_list")
def ngo_list():

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM ngo_users")
    fetchdata = cur.fetchall()
    cur.close()
    return render_template("ngo_list.html", data = fetchdata)

@app.route("/upcomin_check")
def upcomin_check():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM add_check")
    fetchdata = cur.fetchall()
    cur.close()
    # patients view
    return render_template("upcomin_check.html", data=fetchdata)


#doc appointment

@app.route('/doc_appointment', methods=['GET', 'POST'])
def doc_appointment():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, location, specialty FROM doc_list")
    doctors = cur.fetchall()
    today = date.today().isoformat()
    return render_template('doc_appointment.html', doctors=doctors, today=today)

@app.route('/filter', methods=['POST'])
def filter_doctors():
    location = request.form.get('filter_location')
    specialty = request.form.get('filter_specialty')
    cur = mysql.connection.cursor()
    query = "SELECT * FROM doc_list WHERE 1=1"
    params = []
    if location:
        query += " AND location = %s"
        params.append(location)
    if specialty:
        query += " AND specialty = %s"
        params.append(specialty)
    cur.execute(query, tuple(params))
    filtered_doctors = cur.fetchall()
    return render_template('doc_appointment.html', doctors=filtered_doctors, today=date.today().isoformat())

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    patient_name = request.form['patient_name']
    appointment_date = request.form['appointment_date']
    doctor_id_str = request.form.get('doctor_id')  # Get doctor_id from form

    if doctor_id_str:
        try:
            doctor_id = int(doctor_id_str)  # Convert to integer
        except ValueError:
            return "Invalid doctor ID"

        # Check if doctor exists in the doctors table
        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM doctors WHERE id = %s", (doctor_id,))
        doctor_exists = cur.fetchone()

        if not doctor_exists:
            return "Error: Selected doctor does not exist!"

        # Insert appointment
        cur.execute("INSERT INTO appointments (doctor_id, patient_name, appointment_date) VALUES (%s, %s, %s)",
                    (doctor_id, patient_name, appointment_date))
        mysql.connection.commit()

        return redirect(url_for('appointment_success'))
    else:
        return "Doctor ID is required"


@app.route('/appointment_success')
def appointment_success():
    cur = mysql.connection.cursor()
    cur.execute("SELECT a.id, d.name AS doctor, a.patient_name, a.appointment_date FROM appointments a JOIN doc_list d ON a.doctor_id = d.id")
    appointments = cur.fetchall()
    return render_template('appointment_success.html', appointments=appointments)





if __name__ == "__main__":
    app.run(debug=True)

    # things which r done
    #
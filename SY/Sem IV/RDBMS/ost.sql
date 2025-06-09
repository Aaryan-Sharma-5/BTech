/* 
1. Create The following  tables :
Hospital (hospital_id, hospital_name, address)
Doctor ( doctor_id, hospital_id, doctor_name, specialization,
experience_in_years)
Patient (patient_id,doctor_id, patient_name, age , gender, diagnosis)
Appointment (appointment_id,patient_id, doctor_id, appointment_date) */

CREATE TABLE Hospital (
  hospital_id SERIAL PRIMARY KEY,
  hospital_name VARCHAR(64),
  address VARCHAR(128)
);

CREATE TABLE Doctor (
  doctor_id SERIAL PRIMARY KEY,
  hospital_id INT NOT NULL,
  doctor_name VARCHAR(255) NOT NULL,
  specialization VARCHAR(255) NOT NULL,
  experience_in_years INT NOT NULL,
  FOREIGN KEY (hospital_id) REFERENCES Hospital(hospital_id)
);

CREATE TABLE Patient (
  patient_id SERIAL PRIMARY KEY,
  doctor_id INT NOT NULL,
  patient_name VARCHAR(255) NOT NULL,
  age INT NOT NULL,
  gender VARCHAR(255) NOT NULL,
  diagnosis VARCHAR(255) NOT NULL,
  FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id)
);

CREATE TABLE Appointment (
  appointment_id SERIAL PRIMARY KEY,
  patient_id INT NOT NULL,
  doctor_id INT NOT NULL,
  appointment_date DATE NOT NULL,
  FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
  FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id)
);

INSERT INTO Hospital (hospital_name, address) VALUES
('CityCare Hospital', '123 Main St, Springfield'),
('Green Valley Medical', '456 Green Blvd, Rivertown'),
('Sunrise Health Center', '789 Sunrise Ave, Lakeside'),
('Wellness Clinic', '101 Health Rd, Brookfield'),
('Starlight Hospital', '202 Galaxy Lane, Starcity');

INSERT INTO Doctor (hospital_id, doctor_name, specialization, experience_in_years) VALUES
(1, 'Dr. Sarah Johnson', 'Cardiology', 12),
(2, 'Dr. Amit Verma', 'Neurology', 8),
(3, 'Dr. Emily Wong', 'Orthopedics', 10),
(4, 'Dr. Rajesh Kumar', 'Pediatrics', 6),
(5, 'Dr. Lisa Smith', 'Dermatology', 15);

INSERT INTO Patient (doctor_id, patient_name, age, gender, diagnosis) VALUES
(1, 'John Doe', 45, 'Male', 'Hypertension'),
(2, 'Priya Mehta', 33, 'Female', 'Migraine'),
(3, 'Michael Brown', 60, 'Male', 'Arthritis'),
(4, 'Anita Desai', 5, 'Female', 'Flu'),
(5, 'Tom Clarkson', 28, 'Male', 'Acne');

INSERT INTO Appointment (patient_id, doctor_id, appointment_date) VALUES
(1, 1, '2025-04-12'),
(2, 2, '2025-04-13'),
(3, 3, '2025-04-14'),
(4, 4, '2025-04-15'),
(5, 5, '2025-04-16');

-- 1. Retrieve all doctors from the database.
SELECT doctor_id, doctor_name, specialization, experience_in_years
FROM Doctor
WHERE hospital_id = 1;

--2. Count the number of patients treated by each doctor
SELECT d.doctor_id, d.doctor_name, COUNT(p.patient_id) AS total_patients
FROM Doctor d
LEFT JOIN Patient p ON d.doctor_id = p.doctor_id
GROUP BY d.doctor_id, d.doctor_name;

--3. List all patients with a diagnosis of ‘Malaria’
SELECT patient_id, patient_name, age, gender, doctor_id
FROM Patient
WHERE diagnosis = 'Malaria';

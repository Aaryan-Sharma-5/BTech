import java.util.*;

// Base class for User
abstract class User {
    private String id;
    private String name;
    private int age;

    // Constructor with validation
    public User(String id, String name, int age) {
        if (id == null || id.trim().isEmpty()) {
            throw new IllegalArgumentException("ID cannot be empty");
        }
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Name cannot be empty");
        }
        if (age < 0) {
            throw new IllegalArgumentException("Age cannot be negative");
        }
        this.id = id;
        this.name = name;
        this.age = age;
    }

    // Getters and setters
    public String getId() { return id; }
    public String getName() { return name; }

    public void setName(String name) {
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Name cannot be empty");
        }
        this.name = name;
    }
    public int getAge() { return age; }
    public abstract String getRole();
}


// Doctor class (inherits from User)
class Doctor extends Users {
    private String specialization;

    public Doctor(String id, String name, int age, String specialization) {
        super(id, name, age);
        this.specialization = specialization;
    }

    public String getSpecialization() { return specialization; }
    public void setSpecialization(String specialization) { this.specialization = specialization; }

    @Override
    public String getRole() {
        return "Doctor";
    }

    public void scheduleAppointment(Patient patient, String date) {
        System.out.println("Appointment scheduled for patient: " + patient.getName() + " on " + date);
    }
}

// Patient class (inherits from User)
class Patient extends Users {
    private String medicalHistory;

    public Patient(String id, String name, int age, String medicalHistory) {
        super(id, name, age);
        this.medicalHistory = medicalHistory;
    }

    public String getMedicalHistory() { return medicalHistory; }
    public void setMedicalHistory(String medicalHistory) { this.medicalHistory = medicalHistory; }

    @Override
    public String getRole() {
        return "Patient";
    }

    public void bookAppointment(Doctor doctor, String date) {
        System.out.println("Appointment booked with Dr. " + doctor.getName() + " on " + date);
    }
}

// Appointment class (Association between Patient and Doctor)
class Appointment {
    private Patient patient;
    private Doctor doctor;
    private String date;

    public Appointment(Patient patient, Doctor doctor, String date) {
        this.patient = patient;
        this.doctor = doctor;
        this.date = date;
    }

    public void showAppointmentDetails() {
        System.out.println("Appointment Details:");
        System.out.println("Patient: " + patient.getName());
        System.out.println("Doctor: " + doctor.getName() + " (Specialization: " + doctor.getSpecialization() + ")");
        System.out.println("Date: " + date);
    }
}

// Billing class (for managing patient billing)
class Bill {
    private Patient patient;
    private double consultationFee;
    private double treatmentCost;
    private double totalAmount;

    // Constructor with validation
    public Bill(Patient patient, double consultationFee, double treatmentCost) {
        if (patient == null) {
            throw new IllegalArgumentException("Patient cannot be null");
        }
        if (consultationFee < 0) {
            throw new IllegalArgumentException("Consultation fee must be positive");
        }
        if (treatmentCost < 0) {
            throw new IllegalArgumentException("Treatment cost must be positive");
        }
        
        this.patient = patient;
        this.consultationFee = consultationFee;
        this.treatmentCost = treatmentCost;
        this.totalAmount = consultationFee + treatmentCost;
    }

    public void generateBill() {
        System.out.println("Generating Bill for Patient: " + patient.getName());
        System.out.println("Consultation Fee: $" + consultationFee);
        System.out.println("Treatment Cost: $" + treatmentCost);
        System.out.println("Total Amount: $" + totalAmount);
    }
}


// Main class to run the system
public class HospitalManagementSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input Doctor Details
        System.out.println("Enter Doctor Details");
        System.out.print("Doctor ID: ");
        String doctorId = scanner.nextLine();
        
        System.out.print("Doctor Name: ");
        String doctorName = scanner.nextLine();
        
        int doctorAge = -1;
        while (doctorAge < 0) {
            System.out.print("Doctor Age (must be positive): ");
            if (scanner.hasNextInt()) {
                doctorAge = scanner.nextInt();
                if (doctorAge < 0) {
                    System.out.println("Invalid input. Age must be a positive number.");
                }
            } else {
                System.out.println("Invalid input. Please enter a valid number.");
                scanner.next(); 
            }
        }
        scanner.nextLine(); 
        
        System.out.print("Doctor Specialization: ");
        String specialization = scanner.nextLine();

        Doctor doctor = new Doctor(doctorId, doctorName, doctorAge, specialization);

        System.out.println("\nEnter Patient Details");
        System.out.print("Patient ID: ");   
        String patientId = scanner.nextLine();
        
        System.out.print("Patient Name: ");
        String patientName = scanner.nextLine();
        
        int patientAge = -1;
        while (patientAge < 0) {
            System.out.print("Patient Age (must be positive): ");
            if (scanner.hasNextInt()) {
                patientAge = scanner.nextInt();
                if (patientAge < 0) {
                    System.out.println("Invalid input. Age must be a positive number.");
                }
            } else {
                System.out.println("Invalid input. Please enter a valid number.");
                scanner.next(); 
            }
        }
        scanner.nextLine(); 
        
        System.out.print("Medical History: ");
        String medicalHistory = scanner.nextLine();

        Patient patient = new Patient(patientId, patientName, patientAge, medicalHistory);

        // Input Appointment Date
        System.out.println("\nSchedule an Appointment");
        System.out.print("Enter Appointment Date (YYYY-MM-DD): ");
        String appointmentDate = scanner.nextLine();

        patient.bookAppointment(doctor, appointmentDate);
        Appointment appointment = new Appointment(patient, doctor, appointmentDate);
        appointment.showAppointmentDetails();

        // Generate Bill
        System.out.println("\nEnter Billing Details");
        
        double consultationFee = -1;
        while (consultationFee < 0) {
            System.out.print("Consultation Fee (must be positive): ");
            if (scanner.hasNextDouble()) {
                consultationFee = scanner.nextDouble();
                if (consultationFee < 0) {
                    System.out.println("Invalid input. Fee must be positive.");
                }
            } else {
                System.out.println("Invalid input. Please enter a valid number.");
                scanner.next(); 
            }
        }
        
        double treatmentCost = -1;
        while (treatmentCost < 0) {
            System.out.print("Treatment Cost (must be positive): ");
            if (scanner.hasNextDouble()) {
                treatmentCost = scanner.nextDouble();
                if (treatmentCost < 0) {
                    System.out.println("Invalid input. Cost must be positive.");
                }
            } else {
                System.out.println("Invalid input. Please enter a valid number.");
                scanner.next();
            }
        }
        Bill bill = new Bill(patient, consultationFee, treatmentCost);
        bill.generateBill();
        scanner.close();
    }
}
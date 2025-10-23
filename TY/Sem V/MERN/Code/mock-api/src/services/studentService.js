import axios from 'axios';

// API Configuration
const API_BASE_URL = 'https://68beac919c70953d96ed2874.mockapi.io/students';

// Create axios instance with default config
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for error handling
apiClient.interceptors.request.use(
  (config) => config,
  (error) => Promise.reject(error)
);

// Response interceptor for error handling
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

// API Service Functions
export const studentService = {
  // Get all students
  getAllStudents: async () => {
    try {
      const response = await apiClient.get('/');
      // Return the students data directly
      return response.data;
    } catch (error) {
      throw new Error(`Failed to fetch students: ${error.message}`);
    }
  },

  // Get student by ID
  getStudentById: async (id) => {
    try {
      const response = await apiClient.get(`/${id}`);
      // Return the student data directly
      return response.data;
    } catch (error) {
      throw new Error(`Failed to fetch student with ID ${id}: ${error.message}`);
    }
  },

  // Create new student
  createStudent: async (studentData) => {
    try {
      // Send only the required student data
      const apiData = {
        name: studentData.name,
        email: studentData.email,
        rollNo: studentData.rollNo
      };

      const response = await apiClient.post('/', apiData);
      
      // Return the created student data
      return response.data;
    } catch (error) {
      throw new Error(`Failed to create student: ${error.message}`);
    }
  },

  // Update student
  updateStudent: async (id, studentData) => {
    try {
      // Send only the required student data
      const apiData = {
        name: studentData.name,
        email: studentData.email,
        rollNo: studentData.rollNo
      };

      const response = await apiClient.put(`/${id}`, apiData);
      
      // Return the updated student data
      return response.data;
    } catch (error) {
      throw new Error(`Failed to update student with ID ${id}: ${error.message}`);
    }
  },

  // Delete student
  deleteStudent: async (id) => {
    try {
      await apiClient.delete(`/${id}`);
      return { success: true, message: 'Student deleted successfully' };
    } catch (error) {
      throw new Error(`Failed to delete student with ID ${id}: ${error.message}`);
    }
  },
};

// Export individual functions for convenience
export const {
  getAllStudents,
  getStudentById,
  createStudent,
  updateStudent,
  deleteStudent
} = studentService;

// Export the API client for direct use if needed
export { apiClient };

// Export default
export default studentService;

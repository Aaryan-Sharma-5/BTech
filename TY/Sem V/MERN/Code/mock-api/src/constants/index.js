// API Configuration
export const API_CONFIG = {
  BASE_URL: 'https://68beac919c70953d96ed2874.mockapi.io/students',
  TIMEOUT: 10000,
  HEADERS: {
    'Content-Type': 'application/json',
  },
};

export const STUDENT_FIELDS = ['name', 'email', 'rollNo'];

export const VALIDATION_RULES = {
  NAME: {
    MIN_LENGTH: 2,
    MAX_LENGTH: 50,
    REQUIRED: true,
  },
  EMAIL: {
    PATTERN: /\S+@\S+\.\S+/,
    REQUIRED: true,
  },
  ROLLNO: {
    REQUIRED: true,
    MIN_LENGTH: 1,
    MAX_LENGTH: 20,
  },
};

// UI Messages
export const MESSAGES = {
  SUCCESS: {
    STUDENT_ADDED: 'Student added successfully!',
    STUDENT_UPDATED: 'Student updated successfully!',
    STUDENT_DELETED: 'Student deleted successfully!',
  },
  ERROR: {
    FETCH_STUDENTS: 'Failed to fetch students. Please try again later.',
    FETCH_STUDENT: 'Failed to fetch student data. Please try again.',
    CREATE_STUDENT: 'Failed to add student. Please try again.',
    UPDATE_STUDENT: 'Failed to update student. Please try again.',
    DELETE_STUDENT: 'Failed to delete student. Please try again.',
    NETWORK_ERROR: 'Network error. Please check your connection.',
    VALIDATION_ERROR: 'Please fix the validation errors and try again.',
  },
  CONFIRMATION: {
    DELETE_STUDENT: 'Are you sure you want to delete this student?',
  },
  LOADING: {
    FETCHING_STUDENTS: 'Loading students...',
    FETCHING_STUDENT: 'Loading student data...',
    SAVING_STUDENT: 'Saving student...',
    UPDATING_STUDENT: 'Updating student...',
    DELETING_STUDENT: 'Deleting student...',
  },
};

// Route Paths
export const ROUTES = {
  HOME: '/',
  STUDENTS: '/',
  ADD_STUDENT: '/add',
  EDIT_STUDENT: '/edit/:id',
  EDIT_STUDENT_PATH: (id) => `/edit/${id}`,
};

// Table Column Configuration
export const TABLE_COLUMNS = [
  { key: 'rollNo', label: 'Roll No', sortable: true },
  { key: 'name', label: 'Name', sortable: true },
  { key: 'email', label: 'Email', sortable: true },
  { key: 'actions', label: 'Actions', sortable: false },
];

// Theme Colors
export const THEME = {
  PRIMARY: '#007bff',
  SUCCESS: '#28a745',
  WARNING: '#ffc107',
  DANGER: '#dc3545',
  SECONDARY: '#6c757d',
  LIGHT: '#f8f9fa',
  DARK: '#343a40',
};

// Breakpoints for Responsive Design
export const BREAKPOINTS = {
  MOBILE: '480px',
  TABLET: '768px',
  DESKTOP: '1024px',
  LARGE_DESKTOP: '1200px',
};

// Local Storage Keys
export const STORAGE_KEYS = {
  STUDENTS_CACHE: 'students_cache',
  USER_PREFERENCES: 'user_preferences',
  LAST_FETCH_TIME: 'last_fetch_time',
};

// Cache Configuration
export const CACHE_CONFIG = {
  EXPIRY_TIME: 5 * 60 * 1000, // 5 minutes in milliseconds
  MAX_ITEMS: 100,
};

const constants = {
  API_CONFIG,
  STUDENT_FIELDS,
  VALIDATION_RULES,
  MESSAGES,
  ROUTES,
  TABLE_COLUMNS,
  THEME,
  BREAKPOINTS,
  STORAGE_KEYS,
  CACHE_CONFIG,
};

export default constants;

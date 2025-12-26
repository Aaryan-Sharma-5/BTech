import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { studentService } from '../services/studentService';
import './StudentForm.css';

const AddStudent = () => {
  const [student, setStudent] = useState({
    name: '',
    email: '',
    rollNo: ''
  });
  const [loading, setLoading] = useState(false);
  const [errors, setErrors] = useState({});
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setStudent(prev => ({
      ...prev,
      [name]: value
    }));

    if (errors[name]) {
      setErrors(prev => ({
        ...prev,
        [name]: ''
      }));
    }
  };

  const validateForm = () => {
    const newErrors = {};

    if (!student.name.trim()) {
      newErrors.name = 'Name is required';
    }

    if (!student.email.trim()) {
      newErrors.email = 'Email is required';
    } else if (!/\S+@\S+\.\S+/.test(student.email)) {
      newErrors.email = 'Email is invalid';
    }

    if (!student.rollNo.trim()) {
      newErrors.rollNo = 'Roll Number is required';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!validateForm()) {
      return;
    }

    setLoading(true);
    try {
      await studentService.createStudent(student);
      alert('Student added successfully!');
      navigate('/'); 
    } catch (error) {
      alert(error.message || 'Failed to add student. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleCancel = () => {
    navigate('/');
  };

  return (
    <div className="student-form-container">
      <div className="form-header">
        <h2>Add New Student</h2>
        <button onClick={handleCancel} className="cancel-btn">
           Back to List
        </button>
      </div>

      <form onSubmit={handleSubmit} className="student-form">
        <div className="form-group">
          <label htmlFor="name">Name *</label>
          <input
            type="text"
            id="name"
            name="name"
            value={student.name}
            onChange={handleChange}
            className={errors.name ? 'error' : ''}
            placeholder="Enter student name"
          />
          {errors.name && <span className="error-message">{errors.name}</span>}
        </div>

        <div className="form-group">
          <label htmlFor="email">Email *</label>
          <input
            type="email"
            id="email"
            name="email"
            value={student.email}
            onChange={handleChange}
            className={errors.email ? 'error' : ''}
            placeholder="Enter email address"
          />
          {errors.email && <span className="error-message">{errors.email}</span>}
        </div>

        <div className="form-group">
          <label htmlFor="rollNo">Roll Number *</label>
          <input
            type="text"
            id="rollNo"
            name="rollNo"
            value={student.rollNo}
            onChange={handleChange}
            className={errors.rollNo ? 'error' : ''}
            placeholder="Enter roll number"
          />
          {errors.rollNo && <span className="error-message">{errors.rollNo}</span>}
        </div>

        <div className="form-actions">
          <button 
            type="button" 
            onClick={handleCancel}
            className="cancel-btn"
            disabled={loading}
          >
            Cancel
          </button>
          <button 
            type="submit" 
            className="submit-btn"
            disabled={loading}
          >
            {loading ? 'Adding...' : 'Add Student'}
          </button>
        </div>
      </form>
    </div>
  );
};

export default AddStudent;

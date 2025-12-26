import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { studentService } from '../services/studentService';
import './StudentForm.css';

const EditStudent = () => {
  const [student, setStudent] = useState({
    name: '',
    email: '',
    rollNo: ''
  });
  const [loading, setLoading] = useState(false);
  const [fetchLoading, setFetchLoading] = useState(true);
  const [errors, setErrors] = useState({});
  const [fetchError, setFetchError] = useState(null);
  const navigate = useNavigate();
  const { id } = useParams();

  useEffect(() => {
    const fetchStudent = async () => {
      try {
        setFetchLoading(true);
        setFetchError(null);
        const studentData = await studentService.getStudentById(id);
        
        setStudent({
          name: studentData.name,
          email: studentData.email,
          rollNo: studentData.rollNo
        });
      } catch (error) {
        setFetchError(error.message || 'Failed to fetch student data. Please try again.');
      } finally {
        setFetchLoading(false);
      }
    };

    fetchStudent();
  }, [id]);

  const retryFetch = async () => {
    try {
      setFetchLoading(true);
      setFetchError(null);
      const studentData = await studentService.getStudentById(id);
      
      setStudent({
        name: studentData.name,
        email: studentData.email,
        rollNo: studentData.rollNo
      });
    } catch (error) {
      setFetchError(error.message || 'Failed to fetch student data. Please try again.');
    } finally {
      setFetchLoading(false);
    }
  };

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
      const response = await studentService.updateStudent(id, student);
      console.log('Student updated:', response);
      
      alert('Student updated successfully!');
      navigate('/'); 
    } catch (error) {
      alert(error.message || 'Failed to update student. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleCancel = () => {
    navigate('/');
  };

  if (fetchLoading) {
    return (
      <div className="loading-container">
        <div className="loading-spinner"></div>
        <p>Loading student data...</p>
      </div>
    );
  }

  if (fetchError) {
    return (
      <div className="error-container">
        <h2>Error</h2>
        <p>{fetchError}</p>
        <div className="error-actions">
          <button onClick={retryFetch} className="retry-btn">
            Retry
          </button>
          <button onClick={handleCancel} className="cancel-btn">
            Back to List
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="student-form-container">
      <div className="form-header">
        <h2>Edit Student (ID: {id})</h2>
        <button onClick={handleCancel} className="cancel-btn">
          ← Back to List
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
            {loading ? 'Updating...' : 'Update Student'}
          </button>
        </div>
      </form>
    </div>
  );
};

export default EditStudent;

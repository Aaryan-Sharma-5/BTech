import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { studentService } from '../services/studentService';
import './StudentList.css';

const StudentList = () => {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    fetchStudents();
  }, []);

  const fetchStudents = async () => {
    try {
      setLoading(true);
      setError(null);
      const studentsData = await studentService.getAllStudents();
      setStudents(studentsData);
    } catch (err) {
      setError(err.message || 'Failed to fetch students. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (studentId) => {
    if (window.confirm('Are you sure you want to delete this student?')) {
      try {
        await studentService.deleteStudent(studentId);
        setStudents(students.filter(student => student.id !== studentId));
        alert('Student deleted successfully!');
      } catch (err) {
        alert('Failed to delete student. Please try again.');
      }
    }
  };

  const handleEdit = (studentId) => {
    navigate(`/edit/${studentId}`);
  };

  if (loading) {
    return (
      <div className="loading-container">
        <div className="loading-spinner"></div>
        <p>Loading students...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="error-container">
        <h2>Error</h2>
        <p>{error}</p>
        <button onClick={fetchStudents} className="retry-btn">
          Retry
        </button>
      </div>
    );
  }

  return (
    <div className="student-list-container">
      <div className="header">
        <h2>Student List</h2>
        <button 
          onClick={() => navigate('/add')} 
          className="add-btn"
        >
          Add New Student
        </button>
      </div>

      {students.length === 0 ? (
        <div className="no-students">
          <p>No students found.</p>
          <button onClick={() => navigate('/add')} className="add-btn">
            Add First Student
          </button>
        </div>
      ) : (
        <div className="table-container">
          <table className="students-table">
            <thead>
              <tr>
                <th>Roll No</th>
                <th>Name</th>
                <th>Email</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {students.map(student => (
                <tr key={student.id}>
                  <td>{student.rollNo}</td>
                  <td>{student.name}</td>
                  <td>{student.email}</td>
                  <td className="actions">
                    <button 
                      onClick={() => handleEdit(student.id)}
                      className="edit-btn"
                    >
                      Edit
                    </button>
                    <button 
                      onClick={() => handleDelete(student.id)}
                      className="delete-btn"
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default StudentList;

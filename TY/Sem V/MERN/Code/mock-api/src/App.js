import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import StudentList from './components/StudentList';
import AddStudent from './components/AddStudent';
import EditStudent from './components/EditStudent';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar">
          <h1 style={{ textAlign: 'center', margin: '20px 0' }}>Student Management System</h1>
        </nav>
        
        <main className="main-content">
          <Routes>
            <Route path="/" element={<StudentList />} />
            <Route path="/add" element={<AddStudent />} />
            <Route path="/edit/:id" element={<EditStudent />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;

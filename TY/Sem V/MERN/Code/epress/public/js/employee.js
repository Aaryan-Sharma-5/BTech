document.addEventListener('DOMContentLoaded', function () {
  fetchEmployeeData();
});

async function fetchEmployeeData() {
  try {
    const response = await fetch('/data/employees.json');
    if (!response.ok) {
      throw new Error('Failed to fetch employee data');
    }

    const data = await response.json();
    displayEmployees(data.employees);

  } catch (error) {
    console.error('Error fetching employee data:', error);
    document.getElementById('employeeContainer').innerHTML = `
            <div class="info-box" style="background: #f8d7da; border-color: #721c24;">
                <h3 style="color: #721c24;">Error Loading Data</h3>
                <p style="color: #721c24;">Unable to load employee information. Please try again later.</p>
            </div>
        `;
  }
}

function displayEmployees(employees) {
  const container = document.getElementById('employeeContainer');

  if (!employees || employees.length === 0) {
    container.innerHTML = '<p>No employee data available.</p>';
    return;
  }

  let html = '<div class="employee-grid">';

  employees.forEach(employee => {
    html += `
            <div class="employee-card">
                <h3>${employee.name}</h3>
                <p class="role">${employee.role}</p>
                <p><strong>Employee ID:</strong> ${employee.id}</p>
                <p><strong>Department:</strong> ${employee.department}</p>
                <p><strong>Email:</strong> ${employee.email}</p>
                <p><strong>Phone:</strong> ${employee.phone}</p>
                <p><strong>Join Date:</strong> ${employee.joinDate}</p>
                <p><strong>Experience:</strong> ${employee.experience}</p>
            </div>
        `;
  });

  html += '</div>';
  container.innerHTML = html;
}

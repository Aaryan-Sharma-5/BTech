import React, { useState } from 'react';
import './App.css'
import Greeting from './components/Greeting';

function App() {
  const [counter, setCounter] = useState(0);
  const [showList, setShowList] = useState(true);
  const user = 'Aaryan';

  const items = ['MongoDB', 'Expressjs', 'Nodejs', 'Reactjs'];

  return (
    <div className="App">
      <h1>Basic React</h1>
      <Greeting name={user} />

      <div className="counter-section">
        <h2>Counter: {counter}</h2>
        <button onClick={() => setCounter(counter + 1)}>Increment</button>
        <button onClick={() => setCounter(counter - 1)}>Decrement</button>
      </div>

      <div className="toggle-list">
        <button onClick={() => setShowList((v) => !v)}>
          {showList ? 'Hide' : 'Show'} List
        </button>
        {showList && (
          <ul>
            {items.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

export default App;

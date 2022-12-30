import React, { useState } from 'react';

function App() {
  // Initialize the AI bot's state and end states
  const [state, setState] = useState(0);
  const endStates = [3, 6];
  
  // Define the actions that the AI bot can take
  const actions = [
    { label: "Action 1", value: 0 },
    { label: "Action 2", value: 1 },
    { label: "Action 3", value: 2 }
  ];
  
  // Handle the action selection event
  function handleActionSelection(event) {
    // Update the AI bot's state based on the chosen action
    const action = event.target.value;
    if (action === 0) {
      setState(state + 1);
    } else if (action === 1) {
      setState(state + 2);
    } else if (action === 2) {
      setState(state + 3);
    }
    
    // Update the AI bot's policy based on the chosen action and reward
    // TODO: Update the AI bot's policy here
  }
  
  

  return (
    <div>
      {/* Render the action buttons in green on a black background */}
      {actions.map(action => (
        <button key={action.value} value={action.value} onClick={handleActionSelection}>
          {colored(action.label, color="green", on_color="on_black")}
        </button>
      ))}
    </div>
  );
}

export default App;

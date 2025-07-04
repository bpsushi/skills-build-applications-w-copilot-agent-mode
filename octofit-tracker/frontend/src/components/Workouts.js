import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    axios.get('https://-8000.app.github.dev/api/workouts/')
      .then(response => {
        setWorkouts(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the workouts!', error);
      });
  }, []);

  return (
    <div>
      <h1>Workouts</h1>
      <ul>
        {workouts.map(workout => (
          <li key={workout.id}>{workout.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Workouts;

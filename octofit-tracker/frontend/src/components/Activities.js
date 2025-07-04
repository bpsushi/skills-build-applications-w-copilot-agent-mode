import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    axios.get('https://-8000.app.github.dev/api/activities/')
      .then(response => {
        setActivities(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the activities!', error);
      });
  }, []);

  return (
    <div>
      <h1>Activities</h1>
      <ul>
        {activities.map(activity => (
          <li key={activity.id}>{activity.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Activities;

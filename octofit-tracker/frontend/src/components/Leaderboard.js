import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    axios.get('https://-8000.app.github.dev/api/leaderboard/')
      .then(response => {
        setLeaderboard(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the leaderboard!', error);
      });
  }, []);

  return (
    <div>
      <h1>Leaderboard</h1>
      <ul>
        {leaderboard.map(entry => (
          <li key={entry.id}>{entry.name}: {entry.score}</li>
        ))}
      </ul>
    </div>
  );
}

export default Leaderboard;

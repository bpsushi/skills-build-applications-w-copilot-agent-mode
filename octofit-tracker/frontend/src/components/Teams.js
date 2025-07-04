import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    axios.get('https://-8000.app.github.dev/api/teams/')
      .then(response => {
        setTeams(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the teams!', error);
      });
  }, []);

  return (
    <div>
      <h1>Teams</h1>
      <ul>
        {teams.map(team => (
          <li key={team.id}>{team.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Teams;

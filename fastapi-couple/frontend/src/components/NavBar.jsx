// project/frontend/src/components/NavBar.jsx
import React from 'react';
import { Link } from 'react-router-dom';

function NavBar() {
  return (
    <nav>
      <ul>
        <li><Link to="/">홈</Link></li>
        <li><Link to="/diary">다이어리</Link></li>
        <li><Link to="/calendar">캘린더</Link></li>
      </ul>
    </nav>
  );
}

export default NavBar;
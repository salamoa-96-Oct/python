// project/frontend/src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import NavBar from './components/NavBar'; // NavBar 임포트
import HomePage from './pages/HomePage';
import DiaryPage from './pages/DiaryPage';
import CalendarPage from './pages/CalendarPage';

function App() {
  return (
    <Router>
      <NavBar /> {/* 네비게이션 바 추가 */}
      <Switch>
        <Route path="/diary" component={DiaryPage} />
        <Route path="/calendar" component={CalendarPage} />
        <Route path="/" component={HomePage} />
      </Switch>
    </Router>
  );
}

export default App;
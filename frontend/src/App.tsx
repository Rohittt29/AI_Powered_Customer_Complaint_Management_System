import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { Dashboard } from './pages/Dashboard';
import { ComplaintPage } from './pages/ComplaintPage';
import { ChatPage } from './pages/ChatPage';
import { UploadPage } from './pages/UploadPage';
import { RiskPage } from './pages/RiskPage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/dashboard" replace />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/complaints" element={<ComplaintPage />} />
        <Route path="/chat" element={<ChatPage />} />
        <Route path="/upload" element={<UploadPage />} />
        <Route path="/risk" element={<RiskPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

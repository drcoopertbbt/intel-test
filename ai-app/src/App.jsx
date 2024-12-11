// src/App.jsx

import React from 'react';
import ChatbotComponent from './chatbot/ChatbotComponent'; // Import the Chatbot component

const App = () => {
  return (
    <div className="relative min-h-screen bg-gray-900 text-gray-100">
      {/* Existing Content */}
      <h1 className="text-3xl font-bold underline p-4">
        Hello world!
      </h1>

      {/* Chatbot */}
      <ChatbotComponent />
    </div>
  );
};

export default App;

// src/ChatbotComponent.jsx
import React from 'react';
import Chatbot from 'react-chatbot-kit';
import 'react-chatbot-kit/build/main.css';

const config = {
  initialMessages: [
    {
      type: 'bot',
      content: 'Hello! How can I help you with security operations today?'
    }
  ],
  botName: 'SecOps Assistant',
  customStyles: {
    botMessageBox: {
      backgroundColor: '#14b8a6',
    },
    chatButton: {
      backgroundColor: '#14b8a6',
    },
  },
};

const MessageParser = {
  parse(message) {
    return {
      type: 'user',
      content: message,
    };
  }
};

const ActionProvider = {
  handleMessage(message) {
    // Add your message handling logic here
    return {
      type: 'bot',
      content: `I received your message: ${message}`,
    };
  }
};

const ChatbotComponent = () => {
  return (
    <div className="fixed bottom-4 right-4 z-50">
      <div className="bg-gray-800 rounded-lg shadow-lg w-96">
        <Chatbot
          config={config}
          messageParser={MessageParser}
          actionProvider={ActionProvider}
        />
      </div>
    </div>
  );
};

export default ChatbotComponent;
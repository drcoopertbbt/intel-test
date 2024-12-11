// src/chatbot/config.js

import { createChatBotMessage } from 'react-chatbot-kit';
import ActionProvider from './ActionProvider';
import MessageParser from './MessageParser';
import './chatbot.css'; // Optional: For custom styling

const config = {
  botName: "SecOpsBot",
  initialMessages: [
    createChatBotMessage(`Hello! I'm SecOpsBot, your assistant for the AI SecOps Tool. How can I help you today?`),
  ],
  state: {
    // Define any initial state here if needed
  },
  customStyles: {
    botMessageBox: {
      backgroundColor: "#14b8a6",
    },
    chatButton: {
      backgroundColor: "#14b8a6",
    },
  },
  widgets: [
    // Define any widgets (like forms, links, etc.) here
  ],
};

export default config;

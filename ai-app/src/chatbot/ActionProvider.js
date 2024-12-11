// src/chatbot/ActionProvider.js

import { createChatBotMessage } from 'react-chatbot-kit';

class ActionProvider {
  constructor(createChatBotMessage, setStateFunc, createClientMessage) {
    this.createChatBotMessage = createChatBotMessage;
    this.setState = setStateFunc;
  }

  greet() {
    const message = this.createChatBotMessage("Hi there! How can I assist you with the AI SecOps Tool today?");
    this.addMessageToState(message);
  }

  help() {
    const message = this.createChatBotMessage(
      "Sure! I can help you with the following:\n- Overview of the tool\n- Device Log Retrieval\n- Packet Capture Setup\n- Network Traffic Analysis\n- AI Model Deployment\nFeel free to ask about any of these topics!"
    );
    this.addMessageToState(message);
  }

  handleUnknown() {
    const message = this.createChatBotMessage(
      "I'm sorry, I didn't understand that. Could you please rephrase or ask something else?"
    );
    this.addMessageToState(message);
  }

  addMessageToState(message) {
    this.setState((prevState) => ({
      ...prevState,
      messages: [...prevState.messages, message],
    }));
  }
}

export default ActionProvider;

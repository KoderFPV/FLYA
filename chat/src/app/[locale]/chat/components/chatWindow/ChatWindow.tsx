"use client";
import React from 'react';
import styles from './ChatWindow.module.scss';
import { useChat } from '../../hooks/useChat';
import { ChatInput } from './chatInput/ChatInput';
import { ChatMessages } from './chatMessages/ChatMessages';

export const ChatWindow = () => {
  const { messages, sendMessage } = useChat();

  return <div className={styles.chatWindow}>
    <ChatMessages messages={messages} />
    <ChatInput onSend={sendMessage} />
  </div>
};

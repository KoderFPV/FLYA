"use client";
import React from 'react';
import classnames from 'classnames';
import styles from './ChatWindow.module.scss';
import { useChat } from '../../hooks/useChat';
import { ChatInput } from './chatInput/ChatInput';
import { ChatMessages } from './chatMessages/ChatMessages';

export const ChatWindow = () => {
  const { messages, sendMessage, state } = useChat();

  const getBorderClass = () => {
    if (state.routerState?.nextNode === 'chat') return styles.chatWindowBorderBlue;
    if (state.routerState?.nextNode === 'cart') return styles.chatWindowBorderRed;
    if (state.routerState?.nextNode === 'products') return styles.chatWindowBorderGreen;
    if (state.routerState?.nextNode === 'product') return styles.chatWindowBorderYellow;
    return '';
  };

  return <div className={classnames(styles.chatWindowContainer, getBorderClass())}>
    <ChatMessages messages={messages} />
    <ChatInput onSend={sendMessage} />
  </div>
};

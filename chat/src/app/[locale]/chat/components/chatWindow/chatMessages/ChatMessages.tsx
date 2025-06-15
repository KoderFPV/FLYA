import React from 'react';
import styles from './ChatMessages.module.css';
import { IMessage } from '@/interfaces';

interface ChatMessages {
  messages: IMessage[];
}

export const ChatMessages: React.FC<ChatMessages> = (props) => {
  return <div className={styles.chatWindowMessages}>
    {props.messages.map((message, index) => <ChatBubble key={index} role={message.role} content={message.content} />)}
  </div>
}

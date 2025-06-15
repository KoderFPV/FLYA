import React from 'react';
import styles from './ChatBubble.module.scss';
import { ROLE } from '@/interfaces';

interface ChatBubbleProps {
  role: ROLE;
  content: string;
}

export const ChatBubble: React.FC<ChatBubbleProps> = ({ role, content }) => {
  const bubbleClass = (() => {
    switch (role) {
      case ROLE.USER:
        return styles.bubbleUser;
      case ROLE.ASSISTANT:
        return styles.bubbleAssistant;
      case ROLE.HINTS:
        return styles.bubbleHints;
      case ROLE.SYSTEM:
        return styles.bubbleSystem;
      case ROLE.ERROR:
        return styles.bubbleError;
    }
  })();

  return (
    <div className={`${styles.chatBubble} ${bubbleClass}`}>
      <p>{content}</p>
    </div>
  );
}

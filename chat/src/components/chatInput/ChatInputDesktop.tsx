'use client';

import styles from "./ChatInput.module.scss";
import TextareaAutosize from 'react-textarea-autosize';

export const ChatInputDesktop = () => {
  return <TextareaAutosize rows={1} className={styles.chatInputDesktopTextarea} placeholder="Ask about products or your order..." />;
}

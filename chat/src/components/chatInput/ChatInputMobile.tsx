'use client';
import styles from './ChatInput.module.scss';
import TextareaAutosize from 'react-textarea-autosize';

export const ChatInputMobile = () => {
  return <TextareaAutosize rows={1} className={styles.chatInputMobileTextarea} placeholder="Ask about products..." />
}

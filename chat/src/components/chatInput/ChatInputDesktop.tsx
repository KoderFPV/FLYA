'use client';

import { InputProps } from "./ChatInput";
import styles from "./ChatInput.module.scss";
import TextareaAutosize from 'react-textarea-autosize';

export const ChatInputDesktop: React.FC<InputProps> = (props) => {
  return (
    <TextareaAutosize
      rows={1}
      className={styles.chatInputDesktopTextarea}
      placeholder="Ask about products or your order..."
      onChange={props.handleChange}
      value={props.message?.content || ''}
      onKeyDown={(e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
          e.preventDefault();
          props.sendMessage();
        }
      }}
    />
  );
}

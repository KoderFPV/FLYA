import React from 'react';
import styles from './ChatInput.module.scss';
import { IMessage, ROLE } from '@/interfaces';
import { useTranslations } from 'next-intl';

interface ChatInputProps {
  onSend: (message: IMessage) => Promise<void>;
}

export const ChatInput: React.FC<ChatInputProps> = (props) => {
  const t = useTranslations('Chat');
  const [inputValue, setInputValue] = React.useState('');
  const [isLoading, setIsLoading] = React.useState(false);
  const inputRef = React.useRef<HTMLInputElement>(null);

  const handleSend = async () => {
    setIsLoading(true);

    try {
      if (inputValue.trim()) {
        const message: IMessage = {
          role: ROLE.USER,
          content: inputValue,
        };

        await props.onSend(message);

        setInputValue('');
        setTimeout(() => {
          inputRef.current?.focus();

        }, 10);
      }
    } catch (error) {
      alert(t('inputError'));
      console.error('Error sending message:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && !isLoading) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className={styles.chatInputContainer}>
      <input
        ref={inputRef}
        type="text"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder={t('inputPlaceholder')}
        className={styles.chatInputInput}
        disabled={isLoading}
      />
      <button disabled={isLoading} onClick={handleSend} className={styles.chatInputSendButton}>
        {t('sendButton')}
      </button>
    </div>
  );
};

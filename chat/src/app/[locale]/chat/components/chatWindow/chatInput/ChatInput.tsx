import React from 'react';
import styles from './ChatBubble.module.css';
import { IMessage, ROLE } from '@/interfaces';
import { useTranslations } from 'next-intl';

interface ChatInputProps {
  onSend: (message: IMessage) => Promise<void>;
}

export const ChatInput: React.FC<ChatInputProps> = (props) => {
  const t = useTranslations('Chat');
  const [inputValue, setInputValue] = React.useState('');
  const [isLoading, setIsLoading] = React.useState(false);

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
      }
    } catch (error) {
      alert(t('chatInputError'));
      console.error('Error sending message:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className={styles.chatInput}>
      <input
        type="text"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        placeholder={t('chatInputPlaceholder')}
        className={styles.inputField}
        disabled={isLoading}
      />
      <button disabled={isLoading} onClick={handleSend} className={styles.sendButton}>
        {t('chatInputSendButton')}
      </button>
    </div>
  );
};

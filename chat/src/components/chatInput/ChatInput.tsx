import React from "react";
import styles from "./ChatInput.module.scss";
import { ChatInputDesktop } from "./ChatInputDesktop";
import { ChatInputMobile } from "./ChatInputMobile";
import { IMessage, ROLE } from "@/interfaces";

interface ChatInputProps {
  sendMessage: (newMessage: IMessage) => Promise<void>;
}

export interface InputProps {
  handleChange: (e: React.ChangeEvent<HTMLTextAreaElement>) => void;
  sendMessage: () => Promise<void>;

}

export const ChatInput: React.FC<ChatInputProps> = (props) => {
  const [message, setMessage] = React.useState<IMessage>();

  const handleChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    const newMessage: IMessage = {
      id: "1",
      content: e.target.value,
      role: ROLE.USER,
    }
    setMessage(newMessage);
  };

  const sendMessage = async () => {
    if (!message) {
      console.error("Message is undefined");
      return;
    }

    await props.sendMessage(message);

    setMessage(undefined);
  }

  const inputProps = {
    handleChange,
    sendMessage,
  }

  return <>
    <div className={styles.chatInputMobile}>
      <ChatInputMobile {...inputProps} />
    </div>

    <div className={styles.chatInputDesktop}>
      <ChatInputDesktop {...inputProps} />
    </div>
  </>

}

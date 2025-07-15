"use client";
import styles from "./Chat.module.scss";
import { ChatInput } from "@/components/chatInput/ChatInput";
import { ChatWindow } from "@/components/chatWindow/ChatWindow";
import { useChat } from "@/hooks/useChat";

export const ChatClient = () => {
  const { messages, sendMessage } = useChat();

  return <div className={styles.chat}>
    <ChatWindow messages={messages} />
    <ChatInput sendMessage={sendMessage} />
  </div>;
}



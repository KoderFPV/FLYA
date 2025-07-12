import styles from "./Chat.module.scss";
import { ChatInput } from "@/components/chatInput/ChatInput";
import { ChatWindow } from "@/components/chatWindow/ChatWindow";

const Chat = () => {
  return <div className={styles.chat}>
    <ChatWindow />
    <ChatInput />
  </div>;
}

export default Chat;


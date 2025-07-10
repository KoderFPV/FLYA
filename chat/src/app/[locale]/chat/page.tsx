import styles from "./Chat.module.scss";
import { ChatWindow } from "./components/chatWindow/ChatWindow";

const Chat = () => {
  return <div className={styles.chatContainer}>
    <ChatWindow />
  </div>
}

export default Chat;


import styles from "./Chat.module.scss";
import { ActionWindow } from "./components/actionWindow/ActionWindow";
import { ChatWindow } from "./components/chatWindow/ChatWindow";

const Chat = () => {
  return <div className={styles.chatContainer}>
    <ChatWindow />
    <ActionWindow />
  </div>
}

export default Chat;


import { IMessage } from "@/interfaces";
import styles from "./ChatWindow.module.scss";
import { ChatBubble } from "../chatBubble/ChatBubble";

interface IChatWindow {
  messages: IMessage[];
}

export const ChatWindow: React.FC<IChatWindow> = (props) => {
  return <div className={styles.chatWindow}>
    {
      props.messages.map((msg, index) => (
        <ChatBubble
          key={index}
          message={msg.content}
          role={msg.role}
        />
      ))
    }
  </div>
};

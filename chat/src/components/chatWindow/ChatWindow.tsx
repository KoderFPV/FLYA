import { ROLE } from "@/interfaces";
import styles from "./ChatWindow.module.scss";
import { ChatBubble } from "../chatBubble/ChatBubble";

export const ChatWindow = () => {
  const messages = [
    {
      role: ROLE.USER,
      message: "Hello, how are you?"
    },
    {
      role: ROLE.ASSISTANT,
      message: "I'm fine, thank you! How can I assist you today?"
    },
    {
      role: ROLE.USER,
      message: "Can you tell me about the weather today?"
    },
    {
      role: ROLE.ASSISTANT,
      message: "Sure! The weather today is sunny with a high of 25°C."
    }
  ]
  return <div className={styles.chatWindow}>
    {
      messages.map((msg, index) => (
        <ChatBubble
          key={index}
          message={msg.message}
          role={msg.role}
        />
      ))
    }
  </div>
};

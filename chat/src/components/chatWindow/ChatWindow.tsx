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
    },
    {
      role: ROLE.USER,
      message: "Great! Thanks for the info."
    },
    {
      role: ROLE.ASSISTANT,
      message: "You're welcome! If you have any more questions, feel free to ask."
    },
    {
      role: ROLE.USER,
      message: "What about the weekend?"
    },
    {
      role: ROLE.ASSISTANT,
      message: "The weekend looks promising with clear skies and temperatures around 22°C."
    },
    {
      role: ROLE.USER,
      message: "Sounds perfect! I'll plan a picnic."
    },
    {
      role: ROLE.ASSISTANT,
      message: "That sounds like a great idea! Enjoy your picnic!"
    },
    {
      role: ROLE.USER,
      message: "Thank you! Bye!"
    },
    {
      role: ROLE.ASSISTANT,
      message: "Goodbye! Have a wonderful day!"
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

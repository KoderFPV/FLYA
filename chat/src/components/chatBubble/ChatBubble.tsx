import styles from "./ChatBubble.module.scss";
import { ROLE } from "@/interfaces";
import classNames from "classnames";

interface ChatBubbleProps {
  message: string;
  role: ROLE;
}

export const ChatBubble: React.FC<ChatBubbleProps> = (props) => {
  const bubbleClass = {
    [ROLE.ASSISTANT]: styles.chatBubbleAI,
    [ROLE.USER]: styles.chatBubbleUser,
  }[props.role]

  return (
    <div className={classNames(bubbleClass)}>
      <div>{props.message}</div>
    </div>
  );


}

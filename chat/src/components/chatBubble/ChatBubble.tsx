
import { ROLE } from "@/interfaces";

interface ChatBubbleProps {
  message: string;
  type: ROLE;
}

export const ChatBubble: React.FC<ChatBubbleProps> = (props) => {
  const { message, type } = props;

  return (
    <div className={`chat-bubble ${type}`}>
      <p>{message}</p>
    </div>
  );
};

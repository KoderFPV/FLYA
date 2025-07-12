import styles from "./ChatInput.module.scss";
import { ChatInputDesktop } from "./ChatInputDesktop";
import { ChatInputMobile } from "./ChatInputMobile";

export const ChatInput = () => {
  return <>
    <div className={styles.chatInputMobile}>
      <ChatInputMobile />
    </div>

    <div className={styles.chatInputDesktop}>
      <ChatInputDesktop />
    </div>
  </>

}

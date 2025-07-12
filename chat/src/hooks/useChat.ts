"use client";
import { useState } from "react";
import { useTranslations } from "next-intl";
import { IChatState, IMessage, ROLE } from "@/interfaces";
import { sendAndReceiveMessagesStream } from "../repositories/sendMessageAction";

export const useChat = () => {
  const t = useTranslations('Chat');

  const welcomeMessage: IMessage = {
    id: "0",
    role: ROLE.ASSISTANT,
    content: t("welcomeMessage"),
  };

  const [messages, setMessages] = useState<IMessage[]>([welcomeMessage]);
  const [state, setState] = useState<IChatState>({});

  const sendMessage = async (newMessage: IMessage) => {
    setMessages(prevMessages => {
      return [
        ...prevMessages,
        newMessage,
      ];
    });

    let message: IMessage;

    for await (const data of sendAndReceiveMessagesStream(newMessage.content, '1',)) {
      if (data.state) {
        setState(prevState => {
          return {
            ...prevState,
            ...data.state,
          };
        });
      }

      if (message && data.message !== null) {
        message.content += data.message.content;
      }

      if (!message && data.message !== null) {
        message = {
          id: data.message.id,
          role: data.message.role,
          content: data.message.content,
        };
      }

      setMessages(prevMessages => {
        if (data.message !== null) {
          const existingMessageIndex = prevMessages.findIndex(m => m.id === message?.id);

          if (existingMessageIndex !== -1) {
            const updatedMessages = [...prevMessages];
            updatedMessages[existingMessageIndex] = message;
            return updatedMessages;
          } else {
            return [...prevMessages, message];
          }
        }
        return prevMessages; // If data.message is null, return the previous messages unchanged
      });
    }

  };

  return {
    state,
    messages,
    sendMessage,
  }
}

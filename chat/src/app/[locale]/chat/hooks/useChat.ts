"use client";
import { useState } from "react";
import { useTranslations } from "next-intl";
import { IMessage, ROLE } from "@/interfaces";
import { sendAndReceiveMessagesStream } from "../repositories/sendMessageAction";

export const useChat = () => {
  const t = useTranslations('Chat');

  const welcomeMessage: IMessage = {
    role: ROLE.ASSISTANT,
    content: t("welcomeMessage"),
  };

  const [messages, setMessages] = useState<IMessage[]>([welcomeMessage]);

  const sendMessage = async (newMessage: IMessage) => {
    setMessages(prevMessages => {
      return [
        ...prevMessages,
        newMessage,
      ];
    });

    for await (const data of sendAndReceiveMessagesStream(newMessage.content, '1',)) {
      if (data.message !== messages?.at(-1).content) {
        return;
      }
      setMessages(prevMessages => [
        ...prevMessages,
        { role: ROLE.ASSISTANT, content: data.message?.content || '' },
      ]);
    }
  };

  return {
    messages,
    sendMessage,
  }
}

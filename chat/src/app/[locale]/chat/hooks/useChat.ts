"use client";
import { useState } from "react";
import { IMessage, ROLE } from "@/interfaces";
import { useTranslations } from "next-intl";
import { sendAndReciveMessages } from "../actions/sendMessageAction";

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

    const answear = await sendAndReciveMessages([...messages, {
      role: ROLE.USER,
      content: newMessage.content,
    }])

    setMessages(prevMessages => [
      ...prevMessages,
      ...answear,
    ]);
  };


  return {
    messages,
    sendMessage,
  }
}

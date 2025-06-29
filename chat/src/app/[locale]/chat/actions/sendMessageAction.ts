'use server';

import { IMessage, ROLE } from "@/interfaces";

export const sendAndReciveMessages = async (messages: IMessage[]): Promise<IMessage[]> => {
  console.log("sendAndReciveMessages called with messages:", messages);
  const AIPlaceholder = "AI answear here...";

  return [{
    role: ROLE.ASSISTANT,
    content: AIPlaceholder,
  }];
}

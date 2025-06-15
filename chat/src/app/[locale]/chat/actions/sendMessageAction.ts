'use server';

import { IMessage, ROLE } from "@/interfaces";

export const sendAndReciveMessages = async (messages: IMessage[]): Promise<IMessage[]> => {
  const AIPlaceholder = "AI answear here...";

  return [{
    role: ROLE.ASSISTANT,
    content: AIPlaceholder,
  }];
}

'use server';

import { IMessage, ROLE } from "@/interfaces";
import { appFetch } from "@/services/fetch.service";
import { getTranslations } from 'next-intl/server';

const debug = true;


export const sendAndReciveMessages = async (message: string, threadId: string): Promise<IMessage[]> => {
  const t = await getTranslations('Chat');
  const AIPlaceholder = "AI answear here...";

  const response = await appFetch('/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      message,
      threadId,
    }),
  });

  if (debug) {
    console.log("Fetch response:", JSON.stringify(response, null, 2));
  }


  if (!response) {
    console.error("Failed to fetch response from API");
    return [{
      role: ROLE.ASSISTANT,
      content: t("responseError"),
    }];
  }


  return [{
    role: ROLE.ASSISTANT,
    content: AIPlaceholder,
  }];
}

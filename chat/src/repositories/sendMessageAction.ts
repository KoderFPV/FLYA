import { ROLE } from "@/interfaces";
import { appFetchStream } from "@/services/fetch.service"; // albo appFetch z returnResponse=true

const debug = true;

interface StreamResponse {
  message: {
    id: string;
    role: ROLE;
    content: string;
  } | null;
  state: {
    routerState?: {
      nextNode: string
    }
  } | null;
}

export async function* sendAndReceiveMessagesStream(
  message: string,
  threadId: string
): AsyncGenerator<StreamResponse, void, unknown> {

  try {
    const response = await appFetchStream('/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        message,
        threadId,
      }),
    });

    if (!response.body) {
      yield {
        message: {
          id: "0",
          role: ROLE.ASSISTANT,
          content: "No response body received.",
        },
        state: {},
      };
      return;
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    while (true) {
      const { done, value } = await reader.read();

      if (done) {
        break;
      }

      const chunk = decoder.decode(value, { stream: true });
      const lines = chunk.split('\n');

      for (const line of lines) {
        if (line.trim()) {
          try {
            const jsonData: StreamResponse = JSON.parse(line);

            if (debug) {
              console.log("Stream chunk:", JSON.stringify(jsonData, null, 2));
            }

            yield jsonData;
          } catch (parseError) {
            console.error("Failed to parse JSON from stream:", parseError, "Line:", line);
          }
        }
      }
    }
  } catch (error) {
    console.error("Stream error:", error);
    yield {
      message: {
        id: "0",
        role: ROLE.ASSISTANT,
        content: "An error occurred while processing the stream.",
      },
      state: {},
    };
  }
}

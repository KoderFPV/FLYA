
export enum ROLE {
  USER = 'user',
  ASSISTANT = 'assistant',
  HINTS = 'hints',
  SYSTEM = 'system',
  ERROR = 'error',
}

export interface IMessage {
  role: ROLE;
  content: string;
  id: string;
}

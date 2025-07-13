
export enum ROLE {
  USER = 'user',
  ASSISTANT = 'assistant',
}

export interface IMessage {
  role: ROLE;
  content: string;
  id: string;
}

export interface IChatState {
  routerState?: {
    nextNode: string;
  };
}

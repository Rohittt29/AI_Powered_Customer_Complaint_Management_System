import { api } from './api';

export const chatService = {
  sendMessage: async (message: string, sessionId?: string) => {
    const response = await api.post('/chat', { message, session_id: sessionId });
    return response.data;
  }
};

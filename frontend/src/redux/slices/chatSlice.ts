import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { chatService } from '../../services/chatService';

interface Message {
  id: string;
  sender: 'ai' | 'user';
  text: string;
}

interface ChatState {
  messages: Message[];
  status: 'idle' | 'loading' | 'succeeded' | 'failed';
  error: string | null;
  sessionId: string | null;
}

const initialState: ChatState = {
  messages: [{ id: 'init', sender: 'ai', text: 'Hello! I am your QMS AI Copilot. How can I assist you today?' }],
  status: 'idle',
  error: null,
  sessionId: null,
};

export const sendMessage = createAsyncThunk(
  'chat/sendMessage',
  async (text: string, { getState }) => {
    // In a real app, grab sessionId from state
    return await chatService.sendMessage(text);
  }
);

const chatSlice = createSlice({
  name: 'chat',
  initialState,
  reducers: {
    addUserMessage: (state, action) => {
      state.messages.push({ id: Date.now().toString(), sender: 'user', text: action.payload });
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(sendMessage.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(sendMessage.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.messages.push({ id: Date.now().toString(), sender: 'ai', text: action.payload.message || 'Action completed.' });
      })
      .addCase(sendMessage.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message || 'Failed to send message';
      });
  },
});

export const { addUserMessage } = chatSlice.actions;
export default chatSlice.reducer;

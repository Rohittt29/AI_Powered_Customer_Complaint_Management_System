import { configureStore } from '@reduxjs/toolkit';
import uiReducer from './slices/uiSlice';
import complaintReducer from './slices/complaintSlice';
import chatReducer from './slices/chatSlice';
import riskReducer from './slices/riskSlice';
import uploadReducer from './slices/uploadSlice';

export const store = configureStore({
  reducer: {
    ui: uiReducer,
    complaint: complaintReducer,
    chat: chatReducer,
    risk: riskReducer,
    upload: uploadReducer,
  },
  // middleware and devTools are automatically configured by RTK
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

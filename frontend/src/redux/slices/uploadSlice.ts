import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { uploadService } from '../../services/uploadService';

interface UploadState {
  files: any[];
  status: 'idle' | 'loading' | 'succeeded' | 'failed';
  error: string | null;
}

const initialState: UploadState = {
  files: [],
  status: 'idle',
  error: null,
};

export const uploadDocument = createAsyncThunk('upload/document', async (file: File) => {
  return await uploadService.uploadDocument(file);
});

const uploadSlice = createSlice({
  name: 'upload',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(uploadDocument.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(uploadDocument.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.files.push(action.payload);
      })
      .addCase(uploadDocument.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message || 'Upload failed';
      });
  },
});

export default uploadSlice.reducer;

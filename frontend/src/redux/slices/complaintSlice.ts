import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { complaintService, ComplaintData } from '../../services/complaintService';

interface ComplaintState {
  complaints: ComplaintData[];
  activeComplaint: ComplaintData | null;
  status: 'idle' | 'loading' | 'succeeded' | 'failed';
  error: string | null;
}

const initialState: ComplaintState = {
  complaints: [],
  activeComplaint: null,
  status: 'idle',
  error: null,
};

export const fetchComplaints = createAsyncThunk('complaint/fetchComplaints', async () => {
  return await complaintService.getComplaints();
});

export const createComplaint = createAsyncThunk('complaint/create', async (data: ComplaintData) => {
  return await complaintService.createComplaint(data);
});

const complaintSlice = createSlice({
  name: 'complaint',
  initialState,
  reducers: {
    setActiveComplaint: (state, action) => {
      state.activeComplaint = action.payload;
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchComplaints.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(fetchComplaints.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.complaints = action.payload;
      })
      .addCase(fetchComplaints.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message || 'Failed to fetch complaints';
      })
      .addCase(createComplaint.fulfilled, (state, action) => {
        state.complaints.push(action.payload);
      });
  },
});

export const { setActiveComplaint } = complaintSlice.actions;
export default complaintSlice.reducer;

import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { riskService } from '../../services/riskService';

interface RiskState {
  assessment: any | null;
  status: 'idle' | 'loading' | 'succeeded' | 'failed';
  error: string | null;
}

const initialState: RiskState = {
  assessment: null,
  status: 'idle',
  error: null,
};

export const generateRisk = createAsyncThunk('risk/generate', async (complaintId: string) => {
  return await riskService.generateRiskAssessment(complaintId);
});

const riskSlice = createSlice({
  name: 'risk',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(generateRisk.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(generateRisk.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.assessment = action.payload;
      })
      .addCase(generateRisk.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message || 'Failed to generate risk assessment';
      });
  },
});

export default riskSlice.reducer;

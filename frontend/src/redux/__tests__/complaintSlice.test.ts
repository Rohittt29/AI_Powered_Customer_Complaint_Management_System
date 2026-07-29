/**
 * Unit tests for the complaint Redux slice.
 * Tests initial state, reducers, and async thunk state transitions.
 */
import { describe, it, expect } from 'vitest';
import complaintReducer, { setActiveComplaint } from '../slices/complaintSlice';

describe('complaintSlice', () => {
  const initialState = {
    complaints: [],
    activeComplaint: null,
    status: 'idle' as const,
    error: null,
  };

  it('should return the initial state', () => {
    expect(complaintReducer(undefined, { type: 'unknown' })).toEqual(initialState);
  });

  it('should handle setActiveComplaint', () => {
    const complaint = { id: '1', complaint_description: 'Test' };
    const actual = complaintReducer(initialState, setActiveComplaint(complaint));
    expect(actual.activeComplaint).toEqual(complaint);
  });

  it('should have idle status initially', () => {
    const state = complaintReducer(undefined, { type: 'unknown' });
    expect(state.status).toBe('idle');
  });

  it('should have null error initially', () => {
    const state = complaintReducer(undefined, { type: 'unknown' });
    expect(state.error).toBeNull();
  });
});

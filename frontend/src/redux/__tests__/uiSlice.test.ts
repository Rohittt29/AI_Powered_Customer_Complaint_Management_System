/**
 * Unit tests for the UI Redux slice.
 * Tests toast management (add and remove).
 */
import { describe, it, expect } from 'vitest';
import uiReducer, { addToast, removeToast } from '../slices/uiSlice';

describe('uiSlice', () => {
  const initialState = {
    toasts: [],
    globalLoading: false,
  };

  it('should return the initial state', () => {
    expect(uiReducer(undefined, { type: 'unknown' })).toEqual(initialState);
  });

  it('should add a toast', () => {
    const state = uiReducer(initialState, addToast({ type: 'success', message: 'Saved!' }));
    expect(state.toasts.length).toBe(1);
    expect(state.toasts[0].message).toBe('Saved!');
    expect(state.toasts[0].type).toBe('success');
    expect(state.toasts[0].id).toBeDefined();
  });

  it('should remove a toast by ID', () => {
    const stateWithToast = uiReducer(
      initialState,
      addToast({ type: 'error', message: 'Failed' })
    );
    const toastId = stateWithToast.toasts[0].id;
    const stateAfterRemove = uiReducer(stateWithToast, removeToast(toastId));
    expect(stateAfterRemove.toasts.length).toBe(0);
  });
});

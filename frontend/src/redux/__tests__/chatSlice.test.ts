/**
 * Unit tests for the chat Redux slice.
 * Tests initial state (welcome message) and addUserMessage reducer.
 */
import { describe, it, expect } from 'vitest';
import chatReducer, { addUserMessage } from '../slices/chatSlice';

describe('chatSlice', () => {
  it('should have a welcome message in initial state', () => {
    const state = chatReducer(undefined, { type: 'unknown' });
    expect(state.messages.length).toBe(1);
    expect(state.messages[0].sender).toBe('ai');
    expect(state.messages[0].text).toContain('QMS AI Copilot');
  });

  it('should add a user message', () => {
    const state = chatReducer(undefined, addUserMessage('Hello'));
    expect(state.messages.length).toBe(2);
    expect(state.messages[1].sender).toBe('user');
    expect(state.messages[1].text).toBe('Hello');
  });

  it('should have idle status initially', () => {
    const state = chatReducer(undefined, { type: 'unknown' });
    expect(state.status).toBe('idle');
  });
});

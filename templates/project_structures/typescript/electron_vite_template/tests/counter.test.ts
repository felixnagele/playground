import { describe, it, expect } from 'vitest';
import { CounterState } from '../src/shared/types';

describe('CounterState', () => {
  it('should initialize with count property', () => {
    const state: CounterState = { count: 0 };
    expect(state.count).toBe(0);
  });

  it('should increment count correctly', () => {
    const state: CounterState = { count: 5 };
    state.count += 1;
    expect(state.count).toBe(6);
  });

  it('should handle negative counts', () => {
    const state: CounterState = { count: -3 };
    state.count += 10;
    expect(state.count).toBe(7);
  });
});

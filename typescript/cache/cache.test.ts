import { expect, test, describe } from 'vitest';
import { SimpleCache } from './cache.js';

describe('SimpleCache', () => {
  test('should store and get value', () => {
    const cache = new SimpleCache();
    cache.set('greet', 'hello');
    expect(cache.get('greet')).toBe('hello');
  });

  test('should return null if expired', async () => {
    const cache = new SimpleCache(10); // 10ms
    cache.set('fast', 'bye');

    await new Promise((res) => setTimeout(res, 20));

    expect(cache.get('fast')).toBe(null);
  });
});

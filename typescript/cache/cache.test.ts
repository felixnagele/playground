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

  test('should return null for missing key', () => {
    const cache = new SimpleCache();
    expect(cache.get('nonexistent')).toBeNull();
  });

  test('should respect custom TTL per entry', async () => {
    const cache = new SimpleCache(60_000); // long default
    cache.set('short', 'value', 10); // override with 10ms

    await new Promise((res) => setTimeout(res, 20));

    expect(cache.get('short')).toBeNull();
  });

  test('should keep entry with long custom TTL alive', () => {
    const cache = new SimpleCache(10);
    cache.set('long', 'persistent', 60_000);
    expect(cache.get('long')).toBe('persistent');
  });

  test('should overwrite existing key with new value', () => {
    const cache = new SimpleCache();
    cache.set('key', 'first');
    cache.set('key', 'second');
    expect(cache.get('key')).toBe('second');
  });

  test('should isolate multiple independent keys', () => {
    const cache = new SimpleCache();
    cache.set('a', 1);
    cache.set('b', 2);
    expect(cache.get('a')).toBe(1);
    expect(cache.get('b')).toBe(2);
  });

  test('should store and retrieve typed values', () => {
    const cache = new SimpleCache();
    const obj = { id: 42, name: 'Alice' };
    cache.set('user', obj);
    expect(cache.get<typeof obj>('user')).toEqual(obj);
  });

  test('should delete expired entry on access', async () => {
    const cache = new SimpleCache(10);
    cache.set('temp', 'gone');
    await new Promise((res) => setTimeout(res, 20));

    expect(cache.get('temp')).toBeNull();
    // Accessing again should still return null (entry was removed)
    expect(cache.get('temp')).toBeNull();
  });
});

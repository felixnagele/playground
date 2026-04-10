import { expect, test } from 'vitest';
import { validatePassword } from './validator.js';

test('should fail weak passwords', () => {
  const result = validatePassword('123');
  expect(result.isValid).toBe(false);
  expect(result.errors).toContain('Too short');
});

test('should pass strong passwords', () => {
  const result = validatePassword('SuperSafe123!');
  expect(result.isValid).toBe(true);
  expect(result.score).toBe(3);
});

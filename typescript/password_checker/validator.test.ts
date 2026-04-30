import { expect, test, describe } from 'vitest';
import { validatePassword } from './validator.js';

describe('validatePassword', () => {
  test('should fail weak passwords', () => {
    const result = validatePassword('123');
    expect(result.isValid).toBe(false);
    expect(result.errors).toContain('Too short');
  });

  test('should pass strong passwords', () => {
    const result = validatePassword('SuperSafe123!');
    expect(result.isValid).toBe(true);
    expect(result.score).toBe(3);
    expect(result.errors).toHaveLength(0);
  });

  test('should fail when number is missing', () => {
    const result = validatePassword('LongPassword!');
    expect(result.isValid).toBe(false);
    expect(result.errors).toContain('No number');
    expect(result.errors).not.toContain('Too short');
    expect(result.errors).not.toContain('No special char');
    expect(result.score).toBe(2);
  });

  test('should fail when special char is missing', () => {
    const result = validatePassword('LongPassword1');
    expect(result.isValid).toBe(false);
    expect(result.errors).toContain('No special char');
    expect(result.errors).not.toContain('Too short');
    expect(result.errors).not.toContain('No number');
    expect(result.score).toBe(2);
  });

  test('should fail when too short but has number and special char', () => {
    const result = validatePassword('Ab1!');
    expect(result.isValid).toBe(false);
    expect(result.errors).toContain('Too short');
    expect(result.errors).not.toContain('No number');
    expect(result.errors).not.toContain('No special char');
    expect(result.score).toBe(2);
  });

  test('should pass with exactly 8 characters including number and special char', () => {
    const result = validatePassword('Abcde1!x');
    expect(result.isValid).toBe(true);
    expect(result.score).toBe(3);
  });

  test('should produce score 2 when one rule fails', () => {
    const result = validatePassword('nospeci1'); // has number, no special, length ok
    expect(result.score).toBe(2);
    const result2 = validatePassword('short!1'); // too short
    expect(result2.score).toBe(2);
  });

  test('should produce score 0 when all rules fail', () => {
    const result = validatePassword('abc'); // too short, no number, no special
    expect(result.isValid).toBe(false);
    expect(result.score).toBe(0);
    expect(result.errors).toHaveLength(3);
  });

  test('should fail empty password with all three errors', () => {
    const result = validatePassword('');
    expect(result.isValid).toBe(false);
    expect(result.errors).toContain('Too short');
    expect(result.errors).toContain('No number');
    expect(result.errors).toContain('No special char');
    expect(result.score).toBe(0);
  });

  test('should accept all valid special characters', () => {
    for (const char of ['!', '@', '#', '$', '%']) {
      const result = validatePassword(`Password1${char}`);
      expect(result.errors).not.toContain('No special char');
    }
  });
});

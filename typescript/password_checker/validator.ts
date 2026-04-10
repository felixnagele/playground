export interface ValidationResult {
  isValid: boolean;
  score: number;
  errors: string[];
}

export function validatePassword(password: string): ValidationResult {
  const errors: string[] = [];

  if (password.length < 8) errors.push('Too short');
  if (!/\d/.test(password)) errors.push('No number');
  if (!/[!@#$%]/.test(password)) errors.push('No special char');

  return {
    isValid: errors.length === 0,
    score: 3 - errors.length,
    errors,
  };
}

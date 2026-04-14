interface CacheEntry {
  value: unknown;
  expiresAt: number;
}

export class SimpleCache {
  private data: Partial<Record<string, CacheEntry>> = {};

  constructor(private defaultTtl: number = 5000) {}

  set<T>(key: string, value: T, customTtl?: number): void {
    const ttl = customTtl ?? this.defaultTtl;
    this.data[key] = {
      value,
      expiresAt: Date.now() + ttl,
    };
  }

  get<T>(key: string): T | null {
    const entry = this.data[key];
    if (!entry) return null;

    if (Date.now() > entry.expiresAt) {
      delete this.data[key];
      return null;
    }
    return entry.value as T;
  }
}

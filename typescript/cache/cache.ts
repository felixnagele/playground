interface CacheEntry {
  value: any;
  expiresAt: number;
}

export class SimpleCache {
  private data: Record<string, CacheEntry> = {};

  constructor(private defaultTtl: number = 5000) {}

  set(key: string, value: any, customTtl?: number): void {
    const ttl = customTtl ?? this.defaultTtl;
    this.data[key] = {
      value,
      expiresAt: Date.now() + ttl,
    };
  }

  get(key: string): any {
    const entry = this.data[key];
    if (!entry) return null;

    if (Date.now() > entry.expiresAt) {
      delete this.data[key];
      return null;
    }
    return entry.value;
  }
}

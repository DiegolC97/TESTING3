import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface Item {
  id?: number;
  name: string;
  description?: string;
  created_at?: string;
}

export const api = {
  // Health check
  healthCheck: async () => {
    const response = await apiClient.get('/api/health');
    return response.data;
  },

  // Items
  getItems: async (): Promise<Item[]> => {
    const response = await apiClient.get('/api/v1/items');
    return response.data;
  },

  getItem: async (id: number): Promise<Item> => {
    const response = await apiClient.get(`/api/v1/items/${id}`);
    return response.data;
  },

  createItem: async (item: Omit<Item, 'id' | 'created_at'>): Promise<Item> => {
    const response = await apiClient.post('/api/v1/items', item);
    return response.data;
  },

  updateItem: async (id: number, item: Partial<Item>): Promise<Item> => {
    const response = await apiClient.put(`/api/v1/items/${id}`, item);
    return response.data;
  },

  deleteItem: async (id: number): Promise<void> => {
    await apiClient.delete(`/api/v1/items/${id}`);
  },
};

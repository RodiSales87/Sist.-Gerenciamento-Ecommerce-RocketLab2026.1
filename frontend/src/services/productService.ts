import { api } from './api';
import { Product, ProductCreate, ProductUpdate } from '../types/product';

export const productService = {
    getAll: async (skip = 0, limit = 100) => {
        const response = await api.get<Product[]>('/produtos/', {
            params: { skip, limit }
        });
        return response.data;
    },

    getById: async (id: string) => {
        const response = await api.get<Product>(`/produtos/${id}`);
        return response.data;
    },

    create: async (data: ProductCreate) => {
        const response = await api.post<Product>('/produtos/', data);
        return response.data;
    },

    update: async (id: string, data: ProductUpdate) => {
        const response = await api.patch<Product>(`/produtos/${id}`, data);
        return response.data;
    },

    delete: async (id: string) => {
        await api.delete(`/produtos/${id}`);
    }
};
import { api } from './api';
import { Product, ProductCreate, ProductUpdate } from '../types/product';

export interface Avaliacao {
    id_avaliacao: string;
    id_pedido: string;
    avaliacao: number;
    titulo_comentario?: string;
    comentario?: string;
}

export const productService = {
    getAll: async (skip = 0, limit = 10000) => {  // <- MUDE O LIMIT PARA 10000 AQUI
        const response = await api.get<Product[]>('/produtos/', {
            params: { skip, limit }
        });
        return response.data;
    },

    getById: async (id: string) => {
        const response = await api.get<Product>(`/produtos/${id}`);
        return response.data;
    },

    getEvaluations: async (id: string) => {
        const response = await api.get<Avaliacao[]>(`/produtos/${id}/avaliacoes`);
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
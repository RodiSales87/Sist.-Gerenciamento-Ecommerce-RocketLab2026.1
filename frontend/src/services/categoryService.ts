import { api } from './api';

export interface Category {
    categoria_produto: string;
    link_imagem: string;
}

export const categoryService = {
    async getAll(): Promise<Category[]> {
        const response = await api.get<Category[]>('/categorias-imagens/');
        return response.data;
    }
};
export interface Product {
  id_produto: string;
  nome_produto: string;
  categoria_produto: string;
  peso_produto_gramas?: number | null;
  comprimento_centimetros?: number | null;
  altura_centimetros?: number | null;
  largura_centimetros?: number | null;
  media_avaliacao?: number | null;
}

export interface ProductCreate extends Omit<Product, 'id_produto' | 'media_avaliacao'> {
  id_produto: string;
}

export type ProductUpdate = Partial<ProductCreate>;
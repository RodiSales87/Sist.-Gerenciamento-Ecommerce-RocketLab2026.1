import { useEffect, useState } from 'react';
import { ProductCard } from '../components/productCard';
import { productService } from '../services/productService';
import { Product } from '../types/product';
import { Plus } from 'lucide-react';

export function MainPage() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);

  // Assim que a tela carregar, chama a API!
  useEffect(() => {
    loadProducts();
  }, []);

  const loadProducts = async () => {
    try {
      const data = await productService.getAll();
      setProducts(data);
    } catch (error) {
      console.error("Erro ao buscar produtos da API:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-extrabold text-gray-900">Catálogo de Produtos</h1>
        <button className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg font-medium flex items-center space-x-2 transition-colors shadow-sm cursor-pointer">
          <Plus className="w-5 h-5" />
          <span>Novo Produto</span>
        </button>
      </div>

      {loading ? (
        <div className="text-center py-20 text-gray-500 font-medium animate-pulse">
          Carregando catálogo...
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {products.map(product => (
            <ProductCard key={product.id_produto} product={product} />
          ))}
          
          {products.length === 0 && (
            <div className="col-span-full text-center py-12 text-gray-500 bg-white rounded-xl border border-dashed border-gray-300">
              Nenhum produto encontrado. Clique em "Novo Produto" para começar!
            </div>
          )}
        </div>
      )}
    </div>
  );
}
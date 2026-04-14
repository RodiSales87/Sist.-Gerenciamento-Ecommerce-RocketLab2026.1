import { useParams, useSearchParams } from 'react-router-dom';
import { useState, useEffect } from 'react';
import { Search } from 'lucide-react';
import { ProductCard } from '../components/productCard';
import { productService } from '../services/productService';
import { Product } from '../types/product';

export function CategoryPage() {
  const { categoryName } = useParams<{ categoryName: string }>();
  const [searchParams] = useSearchParams();
  const query = searchParams.get('q');

  const [searchTerm, setSearchTerm] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const [products, setProducts] = useState<Product[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const itemsPerPage = 8; // changed to 8 products per page to better fill the grid

  useEffect(() => {
    async function loadProducts() {
      setIsLoading(true);
      try {
        const data = await productService.getAll();
        setProducts(data);
      } catch (error) {
        console.error("Erro ao buscar produtos:", error);
      } finally {
        setIsLoading(false);
      }
    }
    loadProducts();
  }, []);

  const displayCategoryName = categoryName?.replace(/_/g, ' ');

  let title = categoryName === 'busca'
    ? `Resultados da busca por: "${query || searchTerm}"`
    : `Navegando em: ${displayCategoryName?.toUpperCase()}`;

  const filteredProducts = products.filter(p => {
    const matchCategory = categoryName && categoryName !== 'busca'
      ? p.categoria_produto.toLowerCase().replace(/_/g, ' ') === categoryName.toLowerCase().replace(/_/g, ' ')
      : true;

    const activeSearch = searchTerm || query || '';
    const matchSearch = activeSearch
      ? p.nome_produto.toLowerCase().includes(activeSearch.toLowerCase())
      : true;

    return matchCategory && matchSearch;
  });

  const totalPages = Math.ceil(filteredProducts.length / itemsPerPage);
  const currentProducts = filteredProducts.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage);

  return (
    <div className="w-full space-y-8">
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
        <h1 className="text-2xl font-bold text-white">{title}</h1>

        <div className="relative w-full md:w-72">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-white/50" />
          <input
            type="text"
            placeholder="Filtrar produtos..."
            value={searchTerm}
            onChange={(e) => {
              setSearchTerm(e.target.value);
              setCurrentPage(1);
            }}
            className="w-full bg-[#111111] border border-white/10 rounded-md py-2 pl-10 pr-4 text-white placeholder-white/30 text-sm focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary"
          />
        </div>
      </div>

      {isLoading ? (
        <div className="text-center py-20 text-white/50">Carregando produtos...</div>
      ) : filteredProducts.length === 0 ? (
        <div className="text-center py-20 text-white/50">
          Nenhum produto encontrado.
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {currentProducts.map(p => (
            <ProductCard key={p.id_produto} product={p} />
          ))}
        </div>
      )}

      {totalPages > 1 && (
        <div className="flex items-center justify-center gap-4 mt-12">
          <button
            disabled={currentPage === 1}
            onClick={() => setCurrentPage(prev => prev - 1)}
            className="px-4 py-2 border border-white/10 rounded-md bg-[#111111] hover:bg-white/5 disabled:opacity-50 disabled:hover:bg-[#111111] transition-colors"
          >
            Anterior
          </button>
          <span className="text-white/60 text-sm">Página {currentPage} de {totalPages}</span>
          <button
            disabled={currentPage === totalPages}
            onClick={() => setCurrentPage(prev => prev + 1)}
            className="px-4 py-2 border border-white/10 rounded-md bg-[#111111] hover:bg-white/5 disabled:opacity-50 disabled:hover:bg-[#111111] transition-colors"
          >
            Próxima
          </button>
        </div>
      )}
    </div>
  );
}

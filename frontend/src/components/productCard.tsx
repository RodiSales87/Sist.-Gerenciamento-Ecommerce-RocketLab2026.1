import { Star, Edit, Trash2 } from 'lucide-react';
import { Product } from '../types/product';
import { Link } from 'react-router-dom';

interface ProductCardProps {
    product: Product;
}

export function ProductCard({ product }: ProductCardProps) {
    return (
        <div className="bg-white rounded-xl shadow-md p-5 border border-gray-100 hover:shadow-lg transition-shadow">
            <div className="flex justify-between items-start mb-4">
                <div>
                    <span className="text-xs font-semibold text-blue-600 bg-blue-50 px-2 py-1 rounded-full uppercase tracking-wider">
                        {product.categoria_produto}
                    </span>
                    <h3 className="text-lg font-bold text-gray-800 mt-2 line-clamp-2">
                        {product.nome_produto}
                    </h3>
                </div>
            </div>

            <div className="flex items-center space-x-1 mb-4">
                <Star className="text-yellow-400 w-5 h-5 fill-current" />
                <span className="font-bold text-gray-700">
                    {product.media_avaliacao?.toFixed(1) || '0.0'}
                </span>
            </div>

            <div className="flex justify-between items-center pt-4 border-t border-gray-100">
                <Link to={`/produtos/${product.id_produto}`} className="text-sm font-medium text-blue-600 hover:text-blue-800">
                    Ver detalhes
                </Link>
                <div className="flex space-x-2">
                    {/* Estes botões chamarão os modais na nossa próxima etapa! */}
                    <button className="p-2 text-gray-400 hover:text-blue-600 hover:bg-blue-50 rounded-full transition-colors">
                        <Edit className="w-4 h-4" />
                    </button>
                    <button className="p-2 text-gray-400 hover:text-red-600 hover:bg-red-50 rounded-full transition-colors">
                        <Trash2 className="w-4 h-4" />
                    </button>
                </div>
            </div>
        </div>
    );
}
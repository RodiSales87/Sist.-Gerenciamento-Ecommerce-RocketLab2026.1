import { Star, StarHalf } from 'lucide-react';
import { Link } from 'react-router-dom';
import { Product } from '../types/product';

interface ProductCardProps {
    product: Product;
}

export function ProductCard({ product }: ProductCardProps) {
    const rating = typeof product.media_avaliacao === 'number' ? product.media_avaliacao : parseFloat(product.media_avaliacao || '0') || 0;
    const fullStars = Math.floor(rating);
    const hasHalfStar = rating % 1 !== 0 && rating > 0;
    const filledStars = fullStars + (hasHalfStar ? 1 : 0);
    const emptyStars = Math.max(0, 5 - filledStars);

    // Substitui os underlines "_" por espaços " " para exibição mais limpa da categoria
    const displayCategory = (product.categoria_produto || 'Sem Categoria').replace(/_/g, ' ');

    return (
        <div className="bg-[#111111] border border-white/10 rounded-xl p-6 hover:border-primary/50 transition-colors flex flex-col h-full group overflow-hidden">
            <div className="mb-4 flex-1">
                <span className="inline-block px-3 py-1 bg-primary/10 text-primary text-xs font-bold rounded-full uppercase tracking-wider mb-4">
                    {displayCategory}
                </span>
                <Link to={`/produto/${product.id_produto}`} className="group-hover:text-primary transition-colors">
                    <h3 className="text-xl font-bold text-white leading-tight mb-2 line-clamp-3">
                        {product.nome_produto}
                    </h3>
                </Link>
            </div>

            <div className="mt-auto pt-4 border-t border-white/5">
                <div className="flex items-center mb-6">
                    <div className="flex gap-1">
                        {Array.from({ length: fullStars }).map((_, i) => (
                            <Star key={`full-${i}`} className="w-4 h-4 fill-primary text-primary" />
                        ))}
                        {hasHalfStar && <StarHalf key="half" className="w-4 h-4 fill-primary text-primary" />}
                        {Array.from({ length: emptyStars }).map((_, i) => (
                            <Star key={`empty-${i}`} className="w-4 h-4 text-white/20" />
                        ))}
                    </div>
                    <span className="text-white/50 text-sm ml-2 font-medium">
                        {rating > 0 ? rating.toFixed(1) : 'Sem avaliações'}
                    </span>
                </div>

                <Link
                    to={`/produto/${product.id_produto}`}
                    className="w-full block text-center bg-transparent border border-primary text-primary hover:bg-primary hover:text-black py-3 rounded-md font-bold transition-colors"
                >
                    Ver Detalhes
                </Link>
            </div>
        </div>
    );
}
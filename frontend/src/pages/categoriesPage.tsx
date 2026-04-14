import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Loader2 } from 'lucide-react';
import { categoryService, Category } from '../services/categoryService';

export function CategoriesPage() {
    const [categories, setCategories] = useState<Category[]>([]);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        async function fetchCategories() {
            try {
                const data = await categoryService.getAll();
                setCategories(data);
            } catch (error) {
                console.error("Erro ao carregar categorias:", error);
            } finally {
                setIsLoading(false);
            }
        }
        fetchCategories();
    }, []);

    return (
        <div className="w-full space-y-8">
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
                <h1 className="text-2xl md:text-3xl font-bold text-white">Todas as Categorias</h1>
            </div>

            {isLoading ? (
                <div className="flex items-center justify-center py-20 text-white/50">
                    <Loader2 className="w-8 h-8 text-primary animate-spin" />
                    <span className="ml-3 font-medium text-lg">Carregando categorias...</span>
                </div>
            ) : categories.length === 0 ? (
                <div className="text-center py-20 text-white/50">
                    Nenhuma categoria encontrada.
                </div>
            ) : (
                <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 sm:gap-6">
                    {categories.map((category) => {
                        // Substitui os underlines "_" por espaços " " para exibição
                        const displayName = category.categoria_produto.replace(/_/g, ' ');

                        return (
                            <Link
                                key={category.categoria_produto} // Usado para navegação e key original da API
                                to={`/categoria/${encodeURIComponent(category.categoria_produto)}`}
                                className="bg-[#111111] hover:bg-white/5 border border-white/10 hover:border-primary/50 transition-all duration-300 rounded-2xl flex items-center justify-center p-4 sm:p-8 group min-h-[120px] sm:min-h-[160px] h-full"
                            >
                                <h3 className="text-white font-bold text-base sm:text-lg tracking-wide text-center uppercase break-words w-full group-hover:text-primary transition-colors">
                                    {displayName}
                                </h3>
                            </Link>
                        );
                    })}
                </div>
            )}
        </div>
    );
}
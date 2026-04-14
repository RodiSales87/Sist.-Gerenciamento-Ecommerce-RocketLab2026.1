import { Plus } from 'lucide-react';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import { ProductFormDrawer } from './productFormDrawer';

export function Header() {
    const [isDrawerOpen, setIsDrawerOpen] = useState(false);

    return (
        <>
            <header className="sticky top-0 z-40 w-full bg-black/90 backdrop-blur-md border-b border-white/10">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">

                    <div className="flex items-center gap-8">
                        <Link to="/" className="flex items-center"></Link>

                        <nav className="hidden md:flex items-center gap-6 text-sm font-medium">
                            <Link to="/" className="text-white/70 hover:text-white transition-colors">
                                <img src="/v-commerci_digital_logo.png" alt="RocketLab" className="h-16 w-auto object-contain" />
                            </Link>
                            <Link to="/categorias" className="text-white/70 hover:text-white transition-colors">Categorias</Link>
                        </nav>
                    </div>

                    <div className="flex items-center gap-4">
                        <button
                            onClick={() => setIsDrawerOpen(true)}
                            className="flex items-center gap-2 bg-primary hover:bg-primary/90 text-black px-4 py-2 rounded-md font-semibold text-sm transition-colors"
                        >
                            <Plus className="w-4 h-4" />
                            Adicionar Produto
                        </button>
                    </div>
                </div>
            </header>

            <ProductFormDrawer
                isOpen={isDrawerOpen}
                onClose={() => setIsDrawerOpen(false)}
            />
        </>
    );
}

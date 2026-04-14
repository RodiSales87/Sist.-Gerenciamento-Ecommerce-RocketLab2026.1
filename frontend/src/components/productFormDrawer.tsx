import { X, Loader2 } from 'lucide-react';
import { FormEvent, useEffect, useState } from 'react';
import { toast } from 'sonner';
import { productService } from '../services/productService';
import { categoryService, Category } from '../services/categoryService';
import { Product } from '../types/product';

interface ProductFormDrawerProps {
    isOpen: boolean;
    onClose: () => void;
    product?: Product | null;
    onSuccess?: () => void;
}

export function ProductFormDrawer({ isOpen, onClose, product, onSuccess }: ProductFormDrawerProps) {
    const [isLoading, setIsLoading] = useState(false);

    const [availableCategories, setAvailableCategories] = useState<Category[]>([]);
    const [loadingCategories, setLoadingCategories] = useState(false);

    const [nome, setNome] = useState('');
    const [categoria, setCategoria] = useState('');
    const [imagem, setImagem] = useState('');
    const [peso, setPeso] = useState('');
    const [comprimento, setComprimento] = useState('');
    const [altura, setAltura] = useState('');
    const [largura, setLargura] = useState('');

    useEffect(() => {
        if (isOpen && product) {
            setNome(product.nome_produto || '');
            setCategoria(product.categoria_produto || '');
            setImagem(product.imagem_produto || '');
            setPeso(product.peso_produto_gramas?.toString() || '');
            setComprimento(product.comprimento_centimetros?.toString() || '');
            setAltura(product.altura_centimetros?.toString() || '');
            setLargura(product.largura_centimetros?.toString() || '');
        } else if (isOpen && !product) {
            setNome('');
            setCategoria('');
            setImagem('');
            setPeso('');
            setComprimento('');
            setAltura('');
            setLargura('');
        }

        if (isOpen) {
            async function fetchCategories() {
                try {
                    setLoadingCategories(true);
                    const data = await categoryService.getAll();
                    setAvailableCategories(data);
                } catch (error) {
                    console.error("Erro ao carregar categorias dinâmicas:", error);
                    toast.error("Falha ao carregar as categorias.");
                } finally {
                    setLoadingCategories(false);
                }
            }
            fetchCategories();
        }
    }, [isOpen, product]);

    if (!isOpen) return null;

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault();
        setIsLoading(true);

        const payload = {
            id_produto: product ? product.id_produto : `prod-${Date.now()}`,
            nome_produto: nome,
            categoria_produto: categoria,
            imagem_produto: imagem || null,
            peso_produto_gramas: peso ? parseFloat(peso.toString()) : null,
            comprimento_centimetros: comprimento ? parseFloat(comprimento.toString()) : null,
            altura_centimetros: altura ? parseFloat(altura.toString()) : null,
            largura_centimetros: largura ? parseFloat(largura.toString()) : null,
        };

        try {
            if (product) {
                await productService.update(product.id_produto, payload);
                toast.success('Produto atualizado com sucesso!');
            } else {
                await productService.create(payload);
                toast.success('Produto criado com sucesso!');
            }

            if (onSuccess) onSuccess();
            onClose();
        } catch (error) {
            console.error(error);
            toast.error('Ocorreu um erro ao salvar o produto.');
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <>
            <div className="fixed inset-0 bg-black/60 z-50 transition-opacity" onClick={onClose} />
            <div
                className="fixed inset-y-0 right-0 z-50 w-full max-w-md bg-[#111111] border-l border-white/10 shadow-xl overflow-y-auto transform transition-transform duration-300"
            >
                <div className="p-6">
                    <div className="flex items-center justify-between mb-8">
                        <h2 className="text-xl font-bold text-white">
                            {product ? 'Editar Produto' : 'Adicionar Produto'}
                        </h2>
                        <button onClick={onClose} className="p-2 text-white/50 hover:text-white rounded-full hover:bg-white/5 transition-colors">
                            <X className="w-5 h-5" />
                        </button>
                    </div>

                    <form onSubmit={handleSubmit} className="flex flex-col gap-6 text-sm">
                        {/* Nome do Produto */}
                        <div>
                            <label className="block text-white/70 mb-2 font-medium">Nome do Produto</label>
                            <input
                                required
                                type="text"
                                value={nome}
                                onChange={(e) => setNome(e.target.value)}
                                placeholder="Ex: Notebook Gamer"
                                className="w-full bg-black border border-white/10 rounded-md p-3 text-white placeholder-white/30 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary transition-all"
                            />
                        </div>

                        {/* Imagem */}
                        <div>
                            <label className="block text-white/70 mb-2 font-medium">Link da Imagem (URL)</label>
                            <input
                                required={false}
                                type="url"
                                value={imagem}
                                onChange={(e) => setImagem(e.target.value)}
                                placeholder="https://exemplo.com/imagem.png"
                                className="w-full bg-black border border-white/10 rounded-md p-3 text-white placeholder-white/30 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary transition-all"
                            />
                        </div>

                        {/* Categoria Carregada por API e sem _ */}
                        <div>
                            <label className="block text-white/70 mb-2 font-medium">Categoria</label>
                            <div className="relative">
                                <select
                                    required
                                    value={categoria}
                                    onChange={(e) => setCategoria(e.target.value)}
                                    disabled={loadingCategories}
                                    className="w-full bg-black border border-white/10 rounded-md p-3 text-white focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary transition-all disabled:opacity-50 appearance-none"
                                >
                                    <option value="" disabled>Selecione uma categoria</option>

                                    {availableCategories.map((cat) => (
                                        <option key={cat.categoria_produto} value={cat.categoria_produto}>
                                            {/* Limpando a estética visual da Categoria ("_" virando espaço) e aplicando uppercase */}
                                            {cat.categoria_produto.replace(/_/g, ' ').toUpperCase()}
                                        </option>
                                    ))}
                                </select>

                                {loadingCategories && (
                                    <div className="absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none">
                                        <Loader2 className="w-4 h-4 text-white/50 animate-spin" />
                                    </div>
                                )}
                            </div>
                        </div>

                        <div className="grid grid-cols-2 gap-4">
                            <div>
                                <label className="block text-white/70 mb-2 font-medium">Peso (g)</label>
                                <input
                                    required
                                    type="number"
                                    value={peso}
                                    onChange={(e) => setPeso(e.target.value)}
                                    placeholder="Ex: 500"
                                    className="w-full bg-black border border-white/10 rounded-md p-3 text-white placeholder-white/30 focus:outline-none focus:border-primary transition-all"
                                />
                            </div>
                        </div>

                        <div className="grid grid-cols-3 gap-4">
                            <div>
                                <label className="block text-white/70 mb-2 font-medium">Comp (cm)</label>
                                <input
                                    required
                                    type="number"
                                    value={comprimento}
                                    onChange={(e) => setComprimento(e.target.value)}
                                    placeholder="20"
                                    className="w-full bg-black border border-white/10 rounded-md p-3 text-white placeholder-white/30 focus:outline-none focus:border-primary transition-all"
                                />
                            </div>
                            <div>
                                <label className="block text-white/70 mb-2 font-medium">Alt (cm)</label>
                                <input
                                    required
                                    type="number"
                                    value={altura}
                                    onChange={(e) => setAltura(e.target.value)}
                                    placeholder="10"
                                    className="w-full bg-black border border-white/10 rounded-md p-3 text-white placeholder-white/30 focus:outline-none focus:border-primary transition-all"
                                />
                            </div>
                            <div>
                                <label className="block text-white/70 mb-2 font-medium">Larg (cm)</label>
                                <input
                                    required
                                    type="number"
                                    value={largura}
                                    onChange={(e) => setLargura(e.target.value)}
                                    placeholder="15"
                                    className="w-full bg-black border border-white/10 rounded-md p-3 text-white placeholder-white/30 focus:outline-none focus:border-primary transition-all"
                                />
                            </div>
                        </div>

                        <div className="mt-8 flex gap-3">
                            <button
                                type="button"
                                onClick={onClose}
                                disabled={isLoading}
                                className="flex-1 px-4 py-3 bg-transparent border border-white/10 text-white rounded-md hover:bg-white/5 font-semibold transition-colors disabled:opacity-50"
                            >
                                Cancelar
                            </button>
                            <button
                                type="submit"
                                disabled={isLoading}
                                className="flex-1 px-4 py-3 bg-primary text-black rounded-md hover:bg-primary/90 font-bold transition-colors shadow-lg shadow-primary/20 disabled:opacity-50"
                            >
                                {isLoading ? 'Salvando...' : 'Salvar Produto'}
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </>
    );
}
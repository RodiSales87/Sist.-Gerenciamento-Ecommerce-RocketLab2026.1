import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Star, StarHalf, Pencil, Trash2, MessageSquarePlus, AlertTriangle } from 'lucide-react';
import { toast } from 'sonner';
import { ProductFormDrawer } from '../components/productFormDrawer';
import { productService, Avaliacao } from '../services/productService';
import { Product } from '../types/product';


export function ProductDetailsPage() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [product, setProduct] = useState<Product | null>(null);
  const [reviews, setReviews] = useState<Avaliacao[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isEditDrawerOpen, setIsEditDrawerOpen] = useState(false);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);

  const loadProduct = async () => {
    if (!id) return;
    try {
      setIsLoading(true);
      const data = await productService.getById(id);
      setProduct(data);

      const productReviews = await productService.getEvaluations(id);
      setReviews(productReviews);

    } catch (error) {
      console.error("Erro ao carregar produto:", error);
      toast.error('Produto não encontrado!');
      navigate('/');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    loadProduct();
  }, [id]);

  const handleDelete = async () => {
    if (!product) return;
    try {
      await productService.delete(product.id_produto);
      setIsDeleteModalOpen(false);
      toast.success('Produto excluído com sucesso!');
      navigate('/');
    } catch (error) {
      toast.error('Erro ao excluir produto.');
    }
  };

  const handleProductSaved = () => {
    loadProduct(); // reload to get updated remote data
  };

  const renderStars = (rating: number) => {
    const stars = [];
    const fullStars = Math.floor(rating);
    const hasHalfStar = rating % 1 !== 0;

    for (let i = 0; i < fullStars; i++) {
      stars.push(<Star key={`full-${i}`} className="w-4 h-4 fill-primary text-primary" />);
    }
    if (hasHalfStar) {
      stars.push(<StarHalf key="half" className="w-4 h-4 fill-primary text-primary" />);
    }
    const emptyStars = 5 - Math.ceil(rating);
    for (let i = 0; i < emptyStars; i++) {
      stars.push(<Star key={`empty-${i}`} className="w-4 h-4 text-white/20" />);
    }
    return stars;
  };

  if (isLoading) {
    return <div className="text-center py-20 text-white/50">Carregando detalhes do produto...</div>;
  }

  if (!product) {
    return <div className="text-center py-20 text-red-500">Produto não encontrado.</div>;
  }

  const rating = typeof product.media_avaliacao === 'number' ? product.media_avaliacao : parseFloat(product.media_avaliacao || '0') || 0;

  return (
    <div className="w-full max-w-5xl mx-auto space-y-12 pb-24">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-12">
        {/* Imagem do Produto */}
        <div className="bg-[#111111] border border-white/10 rounded-2xl aspect-square flex items-center justify-center overflow-hidden">
          {product.imagem_produto ? (
            <img src={product.imagem_produto} alt={product.nome_produto} className="w-full h-full object-cover" />
          ) : (
            <div className="text-white/20 text-center">
              <div className="w-24 h-24 mx-auto mb-4 bg-white/5 rounded-full flex items-center justify-center">
                <span className="text-4xl text-primary">?</span>
              </div>
              <p>Sem Imagem</p>
            </div>
          )}
        </div>

        {/* Product Info */}
        <div className="space-y-6 flex flex-col">
          <div>
            <span className="inline-block px-3 py-1 bg-primary/10 text-primary text-xs font-bold rounded-full uppercase tracking-wider mb-4">
              {product.categoria_produto || 'Sem categoria'}
            </span>
            <h1 className="text-3xl md:text-4xl font-extrabold text-white leading-tight mb-4">
              {product.nome_produto}
            </h1>
            <div className="flex items-center gap-2 mb-6">
              <div className="flex gap-1">{renderStars(rating)}</div>
              <span className="text-white/50 text-sm ml-2">
                {rating > 0 ? `${rating.toFixed(1)} / 5.0` : 'Sem avaliações'}
              </span>
            </div>
          </div>

          <div className="bg-[#111111] rounded-xl p-6 border border-white/10 space-y-4 flex-1">
            <h3 className="font-semibold text-white mb-4">Especificações Técnicas</h3>
            <div className="grid grid-cols-2 gap-4 text-sm text-white/70">
              <div><span className="text-white/40 block mb-1">Peso</span> {product.peso_produto_gramas || '-'} g</div>
              <div><span className="text-white/40 block mb-1">Comprimento</span> {product.comprimento_centimetros || '-'} cm</div>
              <div><span className="text-white/40 block mb-1">Altura</span> {product.altura_centimetros || '-'} cm</div>
              <div><span className="text-white/40 block mb-1">Largura</span> {product.largura_centimetros || '-'} cm</div>
            </div>
          </div>
        </div>
      </div>

      {/* Reviews Section */}
      <div className="border-t border-white/10 pt-12">
        <div className="flex items-center justify-between mb-8">
          <h2 className="text-2xl font-bold text-white">Avaliações</h2>
          <button className="text-primary hover:text-primary/80 font-medium text-sm transition-colors cursor-pointer">
            Ver todas as avaliações
          </button>
        </div>

        <div className="space-y-4">
          {reviews.length === 0 ? (
            <div className="text-white/50 text-center py-8 bg-[#111111] rounded-xl border border-white/5">
              Nenhuma avaliação encontrada para este produto ainda.
            </div>
          ) : (
            reviews.map(review => (
              <div key={review.id_avaliacao} className="bg-[#111111] border border-white/5 p-6 rounded-xl">
                <div className="flex gap-1 mb-3">{renderStars(review.avaliacao)}</div>

                {review.titulo_comentario && (
                  <h4 className="text-white font-bold mb-2">{review.titulo_comentario}</h4>
                )}

                <p className="text-white/80 mb-4">
                  "{review.comentario ? review.comentario : 'Nenhum comentário providenciado pelo consumidor.'}"
                </p>

                <span className="text-white/40 text-xs font-medium uppercase tracking-wider">
                  Compra: {review.id_pedido}
                </span>
              </div>
            ))
          )}
        </div>
      </div>

      {/* Sticky Action Bar */}
      <div className="fixed bottom-0 left-0 right-0 bg-[#000000]/80 backdrop-blur-md border-t border-white/10 p-4 z-40">
        <div className="max-w-5xl mx-auto flex items-center justify-end gap-4">
          <button
            onClick={() => toast.success('Função de avaliar em desenvolvimento!')}
            className="flex items-center gap-2 px-4 py-2 border border-white/10 text-white rounded-md hover:bg-white/5 font-semibold transition-colors"
          >
            <MessageSquarePlus className="w-4 h-4" /> Avaliar
          </button>

          <button
            onClick={() => setIsEditDrawerOpen(true)}
            className="flex items-center gap-2 px-4 py-2 border border-primary text-primary rounded-md hover:bg-primary hover:text-black font-semibold transition-colors shadow-[0_0_15px_rgba(221,170,51,0.2)] hover:shadow-[0_0_20px_rgba(221,170,51,0.4)]"
          >
            <Pencil className="w-4 h-4" /> Editar Produto
          </button>

          <button
            onClick={() => setIsDeleteModalOpen(true)}
            className="flex items-center gap-2 px-4 py-2 bg-red-500/10 hover:bg-red-500 text-red-500 hover:text-white border border-red-500/20 hover:border-red-500 rounded-md font-bold transition-all"
          >
            <Trash2 className="w-4 h-4" /> Excluir Produto
          </button>
        </div>
      </div>

      <ProductFormDrawer
        isOpen={isEditDrawerOpen}
        onClose={() => setIsEditDrawerOpen(false)}
        product={product}
        onSuccess={handleProductSaved}
      />

      {/* Delete Confirmation Modal */}
      {isDeleteModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm">
          <div className="bg-[#111111] border border-white/10 rounded-2xl max-w-md w-full p-8 shadow-2xl">
            <div className="flex items-center justify-center w-16 h-16 rounded-full bg-red-500/10 text-red-500 mb-6 mx-auto">
              <AlertTriangle className="w-8 h-8" />
            </div>
            <h2 className="text-2xl font-bold text-center text-white mb-4">Você tem certeza?</h2>
            <p className="text-white/60 text-center mb-8">
              Esta ação é irreversível. O produto será permanentemente removido do catálogo.
            </p>
            <div className="flex gap-4">
              <button
                onClick={() => setIsDeleteModalOpen(false)}
                className="flex-1 px-4 py-3 border border-white/10 text-white rounded-xl hover:bg-white/5 font-semibold transition-colors"
              >
                Cancelar
              </button>
              <button
                onClick={handleDelete}
                className="flex-1 px-4 py-3 bg-red-500 text-white rounded-xl hover:bg-red-600 font-bold transition-colors shadow-lg shadow-red-500/20"
              >
                Sim, Excluir
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

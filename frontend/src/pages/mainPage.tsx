import { Search, Monitor, BookOpen, Shirt, Utensils, Headphones, Gamepad2 } from 'lucide-react';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const CATEGORIES = [
  { id: 'eletronicos', name: 'Eletrônicos', icon: Monitor },
  { id: 'livros', name: 'Livros', icon: BookOpen },
  { id: 'vestuario', name: 'Vestuário', icon: Shirt },
  { id: 'casa', name: 'Casa e Cozinha', icon: Utensils },
  { id: 'acessorios', name: 'Acessórios', icon: Headphones },
  { id: 'games', name: 'Games', icon: Gamepad2 },
];

export function MainPage() {
  const [searchTerm, setSearchTerm] = useState('');
  const navigate = useNavigate();

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (searchTerm.trim()) {
      navigate(`/categoria/busca?q=${encodeURIComponent(searchTerm)}`);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-[70vh] text-center">
      <div className="max-w-3xl w-full space-y-8">
        <div className="space-y-4 flex justify-center w-full">
          <img
            src="/v-commerci_digital_logo.png"
            alt="RocketLab"
            className="h-48 md:h-64 lg:h-72 w-auto mx-auto object-contain"
          />
        </div>

        <form onSubmit={handleSearch} className="relative w-full max-w-2xl mx-auto mt-12 mb-16 flex items-center group">
          <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
            <Search className="h-5 w-5 text-white/40 group-focus-within:text-primary transition-colors" />
          </div>
          <input
            type="text"
            placeholder="Buscar produtos..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full bg-[#111111] border border-white/10 rounded-l-md py-4 pl-12 pr-4 text-white placeholder-white/30 text-lg focus:outline-none focus:border-primary/50 focus:ring-1 focus:ring-primary/50 transition-all font-medium"
          />
          <button
            type="submit"
            className="bg-primary hover:bg-primary/90 text-black px-8 py-4 rounded-r-md font-bold text-lg transition-colors whitespace-nowrap"
          >
            Buscar
          </button>
        </form>
      </div>
    </div>
  );
}

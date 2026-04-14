import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { MainPage } from './pages/mainPage';

export default function App() {
    return (
        <BrowserRouter>
            {/* Container principal cinza claro pro fundo inteiro */}
            <div className="min-h-screen bg-gray-50 font-sans">

                {/* Header fixo base do nosso app */}
                <header className="bg-white border-b border-gray-200 py-4 px-6 shadow-sm sticky top-0 z-10">
                    <div className="max-w-7xl mx-auto flex items-center">
                        <span className="text-2xl font-black text-blue-600 tracking-tighter">ROCKETLAB</span>
                    </div>
                </header>

                {/* Carga das Rotas */}
                <main>
                    <Routes>
                        <Route path="/" element={<MainPage />} />
                        {/* Logo criaremos a rota: <Route path="/produtos/:id" element={<ProductPage />} /> */}
                    </Routes>
                </main>
            </div>
        </BrowserRouter>
    )
}
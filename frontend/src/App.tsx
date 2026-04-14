import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Toaster } from 'sonner';
import { Header } from './components/header';
import { MainPage } from './pages/mainPage';
import { CategoriesPage } from './pages/categoriesPage';
import { CategoryPage } from './pages/categoryPage';
import { ProductDetailsPage } from './pages/productDetailsPage';

export default function App() {
    return (
        <BrowserRouter>
            <div className="min-h-screen bg-black text-white font-sans flex flex-col">
                <Header />
                <main className="flex-1 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                    <Routes>
                        <Route path="/" element={<MainPage />} />
                        <Route path="/categorias" element={<CategoriesPage />} />
                        <Route path="/categoria/:categoryName" element={<CategoryPage />} />
                        <Route path="/produto/:id" element={<ProductDetailsPage />} />
                    </Routes>
                </main>
                <Toaster richColors theme="dark" />
            </div>
        </BrowserRouter>
    );
}

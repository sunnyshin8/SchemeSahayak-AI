'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { useLanguage } from './context/LanguageContext';

export default function Home() {
  const [query, setQuery] = useState('');
  const router = useRouter();
  const { t } = useLanguage();

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (query.trim()) {
      router.push(`/results?q=${encodeURIComponent(query)}`);
    }
  };

  return (
    <div className="flex-grow bg-gradient-to-br from-indigo-900 via-purple-900 to-black text-white flex flex-col items-center justify-center p-4 py-12 md:py-16 w-full">
      <main className="w-full max-w-3xl text-center space-y-8">
        <h1 className="text-4xl md:text-5xl lg:text-7xl font-extrabold tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-purple-400">
          {t.title}
        </h1>
        <p className="text-xl md:text-2xl text-gray-300 font-light">
          {t.subtitle}
        </p>

        <form onSubmit={handleSearch} className="w-full relative group">
          <div className="absolute -inset-0.5 bg-gradient-to-r from-pink-600 to-purple-600 rounded-lg blur opacity-75 group-hover:opacity-100 transition duration-1000 group-hover:duration-200"></div>
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder={t.searchPlaceholder}
            className="relative w-full bg-gray-900 text-white border-none rounded-lg py-5 px-6 text-lg focus:outline-none focus:ring-2 focus:ring-cyan-500 shadow-2xl"
            suppressHydrationWarning
          />
          <button
            type="submit"
            className="absolute right-3 top-2.5 bottom-2.5 bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-400 hover:to-blue-400 text-white font-bold py-2 px-6 rounded-md transition-all duration-300"
          >
            {t.searchButton}
          </button>
        </form>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 text-left mt-12 opacity-80">
          <div className="p-6 bg-white/5 backdrop-blur-lg rounded-xl border border-white/10 hover:bg-white/10 transition">
            <h3 className="text-xl font-bold text-cyan-300 mb-2">{t.discoveryTitle}</h3>
            <p className="text-sm text-gray-400">{t.discoveryDesc}</p>
          </div>
          <div className="p-6 bg-white/5 backdrop-blur-lg rounded-xl border border-white/10 hover:bg-white/10 transition">
            <h3 className="text-xl font-bold text-purple-300 mb-2">{t.privacyTitle}</h3>
            <p className="text-sm text-gray-400">{t.privacyDesc}</p>
          </div>
          <div className="p-6 bg-white/5 backdrop-blur-lg rounded-xl border border-white/10 hover:bg-white/10 transition">
            <h3 className="text-xl font-bold text-pink-300 mb-2">{t.verifyTitle}</h3>
            <p className="text-sm text-gray-400">{t.verifyDesc}</p>
          </div>
        </div>
      </main>
    </div>
  );
}

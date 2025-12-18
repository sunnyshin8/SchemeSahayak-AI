'use client';
import { useLanguage } from '../context/LanguageContext';

export default function LanguageSwitch() {
    const { lang, toggleLanguage } = useLanguage();
    return (
        <button
            onClick={toggleLanguage}
            className="fixed top-4 right-4 z-50 bg-white/10 backdrop-blur-md border border-white/20 text-white px-3 py-1 rounded-full text-xs font-bold hover:bg-white/20 transition"
        >
            {lang === 'en' ? '🇮🇳 हिंदी' : '🇬🇧 English'}
        </button>
    );
}

'use client';

import React, { createContext, useContext, useState, ReactNode } from 'react';
import { translations } from '../utils/translations';

type Language = 'en' | 'hi';

interface LanguageContextType {
    lang: Language;
    toggleLanguage: () => void;
    t: typeof translations['en'];
}

const LanguageContext = createContext<LanguageContextType | undefined>(undefined);

export function LanguageProvider({ children }: { children: ReactNode }) {
    const [lang, setLang] = useState<Language>('en');

    const toggleLanguage = () => {
        setLang((prev) => (prev === 'en' ? 'hi' : 'en'));
    };

    const t = translations[lang];

    return (
        <LanguageContext.Provider value={{ lang, toggleLanguage, t }}>
            {children}
        </LanguageContext.Provider>
    );
}

export function useLanguage() {
    const context = useContext(LanguageContext);
    if (context === undefined) {
        throw new Error('useLanguage must be used within a LanguageProvider');
    }
    return context;
}

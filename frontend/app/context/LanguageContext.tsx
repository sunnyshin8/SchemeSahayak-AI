'use client';

import React, { createContext, useContext, useState, ReactNode } from 'react';
import { translations } from '../utils/translations';

type Language = 'en' | 'hi' | 'gu' | 'ur' | 'ta' | 'kn';

interface LanguageContextType {
    lang: Language;
    setLanguage: (lang: Language) => void;
    t: typeof translations['en'];
}

const LanguageContext = createContext<LanguageContextType | undefined>(undefined);

export function LanguageProvider({ children }: { children: ReactNode }) {
    const [lang, setLang] = useState<Language>('en');

    const setLanguage = (newLang: Language) => {
        setLang(newLang);
    };

    const t = translations[lang];

    return (
        <LanguageContext.Provider value={{ lang, setLanguage, t }}>
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

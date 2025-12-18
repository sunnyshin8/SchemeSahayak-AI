'use client';
import { useState, useRef, useEffect } from 'react';
import { useLanguage } from '../context/LanguageContext';

interface LanguageSwitchProps {
    className?: string;
    dropdownClassName?: string;
}

export default function LanguageSwitch({ className = "", dropdownClassName = "" }: LanguageSwitchProps) {
    const { lang, setLanguage } = useLanguage();
    const [isOpen, setIsOpen] = useState(false);
    const dropdownRef = useRef<HTMLDivElement>(null);

    const languages = [
        { code: 'en', label: 'English', flag: '🇬🇧' },
        { code: 'hi', label: 'हिंदी', flag: '🇮🇳' },
        { code: 'gu', label: 'ગુજરાતી', flag: '🇮🇳' },
        { code: 'ur', label: 'اردو', flag: '🇮🇳' },
        { code: 'ta', label: 'தமிழ்', flag: '🇮🇳' },
        { code: 'kn', label: 'ಕನ್ನಡ', flag: '🇮🇳' },
    ];

    const currentLang = languages.find(l => l.code === lang) || languages[0];

    useEffect(() => {
        const handleClickOutside = (event: MouseEvent) => {
            if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
                setIsOpen(false);
            }
        };

        document.addEventListener('mousedown', handleClickOutside);
        return () => {
            document.removeEventListener('mousedown', handleClickOutside);
        };
    }, []);

    return (
        <div className={`relative ${className}`} ref={dropdownRef}>
            <button
                onClick={() => setIsOpen(!isOpen)}
                className="bg-white/10 backdrop-blur-md border border-white/20 text-white px-3 py-1.5 rounded-full text-xs font-bold hover:bg-white/20 transition flex items-center gap-2 shadow-lg"
            >
                <span className="text-sm">{currentLang.flag}</span>
                <span>{currentLang.label}</span>
                <span className={`text-[10px] opacity-70 transform transition-transform ${isOpen ? 'rotate-180' : 'rotate-0'}`}>▼</span>
            </button>

            {isOpen && (
                <div className={`absolute right-0 mt-2 w-32 bg-black/90 border border-white/10 rounded-lg shadow-2xl overflow-hidden backdrop-blur-xl z-50 py-1 ${dropdownClassName}`}>
                    {languages.map((l) => (
                        <button
                            key={l.code}
                            onClick={() => {
                                setLanguage(l.code as any);
                                setIsOpen(false);
                            }}
                            className={`w-full text-left px-4 py-2.5 text-xs font-medium flex items-center gap-3 hover:bg-white/10 transition ${lang === l.code ? 'bg-purple-500/20 text-purple-300' : 'text-gray-300'
                                }`}
                        >
                            <span className="text-sm">{l.flag}</span>
                            <span>{l.label}</span>
                        </button>
                    ))}
                </div>
            )}
        </div>
    );
}

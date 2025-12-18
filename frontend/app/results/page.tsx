'use client';

import { Suspense, useEffect, useState } from 'react';
import { useSearchParams } from 'next/navigation';
import { searchSchemes } from '../utils/api';
import Link from 'next/link';
import { useLanguage } from '../context/LanguageContext';
import LanguageSwitch from '../components/LanguageSwitch';

function ResultsContent() {
    const searchParams = useSearchParams();
    const query = searchParams.get('q');
    const [results, setResults] = useState<any[]>([]);
    const [loading, setLoading] = useState(true);
    const { t } = useLanguage();

    useEffect(() => {
        if (query) {
            setLoading(true);
            searchSchemes(query)
                .then((data) => setResults(data.results || []))
                .catch((err) => console.error(err))
                .finally(() => setLoading(false));
        }
    }, [query]);

    return (
        <div className="min-h-screen bg-gray-900 text-white p-6">
            <LanguageSwitch />
            <header className="max-w-6xl mx-auto flex justify-between items-center mb-8 border-b border-gray-800 pb-4">
                <Link href="/">
                    <h1 className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-purple-400 cursor-pointer">
                        {t.title}
                    </h1>
                </Link>
                <div className="bg-gray-800 px-4 py-2 rounded-full text-sm text-gray-400">
                    Query: <span className="text-white italic">"{query}"</span>
                </div>
            </header>

            <main className="max-w-6xl mx-auto">
                <h2 className="text-3xl font-bold mb-6">{t.resultsTitle}</h2>

                {loading ? (
                    <div className="space-y-4">
                        {[1, 2, 3].map(i => (
                            <div key={i} className="h-32 bg-gray-800 rounded-xl animate-pulse"></div>
                        ))}
                    </div>
                ) : (
                    <div className="grid gap-6">
                        {results.length > 0 ? (
                            results.map((item: any, idx: number) => {
                                const detailsUrl = `/scheme/${item.id}`;

                                return (
                                    <div key={idx} className="bg-gray-800 rounded-xl p-6 border border-gray-700 hover:border-cyan-500 transition duration-300 shadow-lg flex flex-col justify-between">
                                        <div className="flex justify-between items-start">
                                            <div className="flex-1">
                                                <Link href={detailsUrl} className="hover:underline">
                                                    <h3 className="text-xl font-bold text-cyan-300 mb-2 flex items-center gap-2">
                                                        {item.metadata?.title || 'Unknown Scheme'}
                                                        <span className="text-sm opacity-50">→</span>
                                                    </h3>
                                                </Link>

                                                <p className="text-gray-300 mb-4">{item.metadata?.description}</p>

                                                <div className="flex flex-wrap gap-3 text-xs uppercase tracking-wider font-semibold">
                                                    <span className="bg-blue-900 text-blue-300 px-3 py-1 rounded-full">
                                                        {item.metadata?.ministry || item.metadata?.bank || 'Scheme'}
                                                    </span>
                                                    {item.metadata?.category && <span className="bg-purple-900 text-purple-300 px-3 py-1 rounded-full">{item.metadata?.category}</span>}
                                                    {item.metadata?.benefits && <span className="bg-green-900 text-green-300 px-3 py-1 rounded-full">{item.metadata?.benefits}</span>}
                                                    {item.metadata?.backing_scheme_name && (
                                                        <span className="bg-yellow-900 text-yellow-300 px-3 py-1 rounded-full border border-yellow-700 flex items-center gap-1">
                                                            <span>🏦 Backed by</span>
                                                            <span className="underline decoration-dotted">{item.metadata.backing_scheme_name}</span>
                                                        </span>
                                                    )}
                                                </div>
                                            </div>
                                            <div className="text-right ml-4 min-w-[80px]">
                                                <div className="text-sm text-gray-400">{t.relevance}</div>
                                                <div className="text-2xl font-bold text-green-400">{(item.score * 100).toFixed(0)}%</div>
                                            </div>
                                        </div>

                                        <div className="mt-4 pt-4 border-t border-gray-700 flex justify-end">
                                            <Link
                                                href={detailsUrl}
                                                className="text-cyan-400 hover:text-cyan-300 font-semibold text-sm flex items-center gap-1 transition-colors"
                                            >
                                                View Full Details & AI Chat →
                                            </Link>
                                        </div>
                                    </div>
                                );
                            })
                        ) : (
                            <div className="text-center text-gray-400 py-20">
                                {t.noResults}
                            </div>
                        )}
                    </div>
                )}
            </main>
        </div>
    );
}

export default function Results() {
    return (
        <Suspense fallback={<div className="text-white p-10">Loading search parameters...</div>}>
            <ResultsContent />
        </Suspense>
    );
}

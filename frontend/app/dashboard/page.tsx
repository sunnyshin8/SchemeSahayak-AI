'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { verifyCitizen } from '../utils/api';
import Link from 'next/link';
import { useLanguage } from '../context/LanguageContext';
import LanguageSwitch from '../components/LanguageSwitch';

export default function Dashboard() {
    const [form, setForm] = useState({ name: '', citizen_id: '', details: '' });
    const [result, setResult] = useState<any>(null);
    const [loading, setLoading] = useState(false);
    const { t } = useLanguage();
    const [authorized, setAuthorized] = useState(false);
    const router = useRouter();



    const [userName, setUserName] = useState('');

    useEffect(() => {
        const userInfo = localStorage.getItem('user_info');
        if (!userInfo) {
            router.push('/login');
        } else {
            const user = JSON.parse(userInfo);
            setUserName(user.name || 'User');
            setAuthorized(true);
        }
    }, []);

    const handleVerify = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setResult(null);
        try {
            // In a real app, we'd pass the token in headers here
            const data = await verifyCitizen(form);
            setResult(data);
        } finally {
            setLoading(false);
        }
    };

    if (!authorized) return null;

    return (
        <div className="min-h-screen bg-gradient-to-br from-indigo-900 via-purple-900 to-black text-white p-6">
            <LanguageSwitch />
            <header className="max-w-6xl mx-auto flex justify-between items-center mb-10 border-b border-white/10 pb-4">
                <Link href="/">
                    <h1 className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-blue-400 cursor-pointer">
                        {t.title} <span className="text-white text-lg font-medium ml-2">| User - {userName}</span>
                    </h1>
                </Link>
            </header>

            <main className="max-w-4xl mx-auto bg-white/10 backdrop-blur-lg rounded-2xl p-8 border border-white/20 shadow-2xl">
                <h2 className="text-2xl font-semibold mb-6 flex items-center gap-3">
                    🕵️ {t.interAgencyVerify}
                </h2>

                <form onSubmit={handleVerify} className="space-y-6">
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <label className="block text-sm text-gray-400 mb-2">{t.citizenName}</label>
                            <input
                                className="w-full bg-gray-800 border border-gray-700 rounded-lg p-3 focus:ring-2 focus:ring-orange-500 outline-none"
                                value={form.name} onChange={e => setForm({ ...form, name: e.target.value })}
                                placeholder={t.namePlaceholder}
                                required
                            />
                        </div>
                        <div>
                            <label className="block text-sm text-gray-400 mb-2">{t.idHash}</label>
                            <input
                                className="w-full bg-gray-800 border border-gray-700 rounded-lg p-3 focus:ring-2 focus:ring-orange-500 outline-none"
                                value={form.citizen_id} onChange={e => setForm({ ...form, citizen_id: e.target.value })}
                                placeholder={t.idPlaceholder}
                                required
                            />
                        </div>
                    </div>
                    <div>
                        <label className="block text-sm text-gray-400 mb-2">{t.appDetails}</label>
                        <textarea
                            className="w-full bg-gray-800 border border-gray-700 rounded-lg p-3 focus:ring-2 focus:ring-orange-500 outline-none h-32"
                            value={form.details} onChange={e => setForm({ ...form, details: e.target.value })}
                            placeholder={t.detailsPlaceholder}
                            required
                        />
                    </div>

                    <button
                        type="submit"
                        disabled={loading}
                        className="w-full bg-gradient-to-r from-orange-600 to-red-600 hover:from-orange-500 hover:to-red-500 text-white font-bold py-3 rounded-lg transition"
                    >
                        {loading ? t.verifying : t.verifyBtn}
                    </button>
                </form>

                {result && (
                    <div className={`mt-8 p-6 rounded-xl border ${result.is_fraud ? 'bg-red-900/20 border-red-500' : 'bg-green-900/20 border-green-500'}`}>
                        <h3 className={`text-xl font-bold mb-2 ${result.is_fraud ? 'text-red-400' : 'text-green-400'}`}>
                            {result.is_fraud ? `⚠️ ${t.fraudDetected}` : `✅ ${t.cleared}`}
                        </h3>

                        <p className="text-white/80 mb-4">
                            {result.is_fraud
                                ? t.fraudMsg
                                : t.clearedMsg}
                        </p>

                        {result.match_details && (
                            <div className="bg-black/40 p-4 rounded text-sm text-gray-300 font-mono">
                                <p>{t.matchScore}: <span className="text-yellow-400">{(result.match_details.score * 100).toFixed(2)}%</span></p>
                                <p>{t.matchedId}: {result.match_details.id}</p>
                                <p>{t.existingData}: {JSON.stringify(result.match_details.metadata)}</p>
                            </div>
                        )}
                    </div>
                )}
            </main>
        </div>
    );
}

'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';

export default function Login() {
    const [isLogin, setIsLogin] = useState(true);
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        password: ''
    });
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        const base_url = 'http://localhost:8000/api/auth';

        try {
            if (isLogin) {
                console.log('Logging in with:', formData.email);
                const res = await fetch(`${base_url}/login`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email: formData.email, password: formData.password })
                });

                const data = await res.json();
                if (res.ok) {
                    // Save user info
                    localStorage.setItem('user_info', JSON.stringify(data.user));
                    alert('Login Successful!');
                    router.push('/dashboard');
                } else {
                    alert(data.detail || 'Login Failed');
                }
            } else {
                console.log('Signing up with:', formData.name, formData.email);
                const res = await fetch(`${base_url}/register`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(formData)
                });

                const data = await res.json();
                if (res.ok) {
                    alert('Registration Successful! Please Login.');
                    setIsLogin(true); // Switch to login
                } else {
                    alert(data.detail || 'Registration Failed');
                }
            }
        } catch (error) {
            console.error(error);
            alert('An error occurred. Please try again.');
        }
    };

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    return (
        <div className="flex-grow bg-gradient-to-br from-indigo-900 via-purple-900 to-black text-white flex items-center justify-center p-6 w-full">
            <div className="w-full max-w-md bg-white/10 backdrop-blur-lg p-8 rounded-2xl border border-white/20 shadow-2xl">
                <div className="flex justify-center mb-8">
                    <div className="bg-black/40 p-1 rounded-lg inline-flex">
                        <button
                            onClick={() => setIsLogin(true)}
                            className={`px-6 py-2 rounded-md text-sm font-medium transition-all ${isLogin
                                ? 'bg-gradient-to-r from-cyan-500 to-blue-500 text-white shadow-lg'
                                : 'text-gray-400 hover:text-white'
                                }`}
                        >
                            Login
                        </button>
                        <button
                            onClick={() => setIsLogin(false)}
                            className={`px-6 py-2 rounded-md text-sm font-medium transition-all ${!isLogin
                                ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white shadow-lg'
                                : 'text-gray-400 hover:text-white'
                                }`}
                        >
                            Sign Up
                        </button>
                    </div>
                </div>

                <h1 className="text-3xl font-bold text-center mb-2 bg-clip-text text-transparent bg-gradient-to-r from-white to-gray-400">
                    {isLogin ? 'Welcome Back' : 'Create Account'}
                </h1>
                <p className="text-center text-gray-400 mb-8 text-sm">
                    {isLogin
                        ? 'Enter your credentials to access your account'
                        : 'Join SchemeSahayak to discover benefits'}
                </p>

                <form onSubmit={handleSubmit} className="space-y-5">
                    {!isLogin && (
                        <div>
                            <label className="block text-sm font-medium text-gray-300 mb-1.5">Full Name</label>
                            <input
                                type="text"
                                name="name"
                                value={formData.name}
                                onChange={handleChange}
                                className="w-full bg-black/50 border border-white/10 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:ring-2 focus:ring-purple-500 focus:border-transparent outline-none transition"
                                placeholder="John Doe"
                                required
                            />
                        </div>
                    )}

                    <div>
                        <label className="block text-sm font-medium text-gray-300 mb-1.5">Email Address</label>
                        <input
                            type="email"
                            name="email"
                            value={formData.email}
                            onChange={handleChange}
                            className="w-full bg-black/50 border border-white/10 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:ring-2 focus:ring-cyan-500 focus:border-transparent outline-none transition"
                            placeholder="name@example.com"
                            required
                        />
                    </div>

                    <div>
                        <label className="block text-sm font-medium text-gray-300 mb-1.5">Password</label>
                        <input
                            type="password"
                            name="password"
                            value={formData.password}
                            onChange={handleChange}
                            className="w-full bg-black/50 border border-white/10 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:ring-2 focus:ring-pink-500 focus:border-transparent outline-none transition"
                            placeholder="••••••••"
                            required
                        />
                    </div>

                    <div className="pt-2">
                        <button
                            type="submit"
                            className={`w-full py-3.5 rounded-lg font-bold text-white shadow-lg transition transform hover:scale-[1.02] active:scale-[0.98] ${isLogin
                                ? 'bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 shadow-cyan-500/25'
                                : 'bg-gradient-to-r from-purple-500 to-pink-600 hover:from-purple-400 hover:to-pink-500 shadow-purple-500/25'
                                }`}
                        >
                            {isLogin ? 'Sign In' : 'Create Account'}
                        </button>
                    </div>
                </form>

                <div className="mt-6 text-center">
                    <p className="text-sm text-gray-400">
                        {isLogin ? "Don't have an account? " : "Already have an account? "}
                        <button
                            onClick={() => setIsLogin(!isLogin)}
                            className="text-white font-medium hover:underline focus:outline-none"
                        >
                            {isLogin ? 'Sign Up' : 'Login'}
                        </button>
                    </p>
                </div>
            </div>
        </div>
    );
}

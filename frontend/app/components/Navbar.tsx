'use client';

import Link from 'next/link';
import { useState } from 'react';

export default function Navbar() {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <nav className="bg-gradient-to-r from-indigo-900 via-purple-900 to-black border-b border-white/10 sticky top-0 z-50 backdrop-blur-lg">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex justify-between h-16">
                    <div className="flex items-center">
                        <Link href="/" className="flex-shrink-0 flex items-center group">
                            <span className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-purple-400 group-hover:from-cyan-300 group-hover:to-purple-300 transition-all duration-300">
                                SchemeSahayak
                            </span>
                        </Link>
                    </div>

                    {/* Desktop Navigation */}
                    <div className="hidden md:flex md:items-center md:space-x-1">
                        <Link
                            href="/"
                            className="px-4 py-2 rounded-lg text-gray-300 hover:text-white hover:bg-white/10 transition-all duration-200"
                        >
                            Home
                        </Link>
                        <Link
                            href="/about"
                            className="px-4 py-2 rounded-lg text-gray-300 hover:text-white hover:bg-white/10 transition-all duration-200"
                        >
                            About Us
                        </Link>
                        <Link
                            href="/features"
                            className="px-4 py-2 rounded-lg text-gray-300 hover:text-white hover:bg-white/10 transition-all duration-200"
                        >
                            Features
                        </Link>
                        <Link
                            href="/contact"
                            className="px-4 py-2 rounded-lg text-gray-300 hover:text-white hover:bg-white/10 transition-all duration-200"
                        >
                            Contact Us
                        </Link>
                        <Link
                            href="/login"
                            className="ml-4 px-6 py-2 bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-400 hover:to-blue-400 text-white font-semibold rounded-lg transition-all duration-300 shadow-lg hover:shadow-cyan-500/50"
                        >
                            Login
                        </Link>
                    </div>

                    {/* Mobile menu button */}
                    <div className="md:hidden flex items-center">
                        <button
                            onClick={() => setIsOpen(!isOpen)}
                            className="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-white/10 transition-all duration-200"
                        >
                            <svg
                                className="h-6 w-6"
                                fill="none"
                                viewBox="0 0 24 24"
                                stroke="currentColor"
                            >
                                {isOpen ? (
                                    <path
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                        strokeWidth={2}
                                        d="M6 18L18 6M6 6l12 12"
                                    />
                                ) : (
                                    <path
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                        strokeWidth={2}
                                        d="M4 6h16M4 12h16M4 18h16"
                                    />
                                )}
                            </svg>
                        </button>
                    </div>
                </div>
            </div>

            {/* Mobile menu */}
            {isOpen && (
                <div className="md:hidden bg-black/50 backdrop-blur-lg border-t border-white/10">
                    <div className="px-2 pt-2 pb-3 space-y-1">
                        <Link
                            href="/"
                            className="block px-3 py-2 rounded-md text-gray-300 hover:text-white hover:bg-white/10 transition-all"
                            onClick={() => setIsOpen(false)}
                        >
                            Home
                        </Link>
                        <Link
                            href="/about"
                            className="block px-3 py-2 rounded-md text-gray-300 hover:text-white hover:bg-white/10 transition-all"
                            onClick={() => setIsOpen(false)}
                        >
                            About Us
                        </Link>
                        <Link
                            href="/features"
                            className="block px-3 py-2 rounded-md text-gray-300 hover:text-white hover:bg-white/10 transition-all"
                            onClick={() => setIsOpen(false)}
                        >
                            Features
                        </Link>
                        <Link
                            href="/contact"
                            className="block px-3 py-2 rounded-md text-gray-300 hover:text-white hover:bg-white/10 transition-all"
                            onClick={() => setIsOpen(false)}
                        >
                            Contact Us
                        </Link>
                        <Link
                            href="/login"
                            className="block mx-3 mt-2 px-4 py-2 bg-gradient-to-r from-cyan-500 to-blue-500 text-white font-semibold rounded-lg text-center"
                            onClick={() => setIsOpen(false)}
                        >
                            Login
                        </Link>
                    </div>
                </div>
            )}
        </nav>
    );
}

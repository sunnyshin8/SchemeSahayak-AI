export const API_BASE_URL = 'http://localhost:8000/api';

export async function searchSchemes(query: string) {
    try {
        const res = await fetch(`${API_BASE_URL}/citizen/search`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query }),
        });
        if (!res.ok) throw new Error('Failed to fetch schemes');
        return await res.json();
    } catch (error) {
        console.error(error);
        return { results: [] };
    }
}

export async function verifyCitizen(data: any) {
    try {
        const token = localStorage.getItem('agency_token');
        const headers: Record<string, string> = { 'Content-Type': 'application/json' };
        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }

        console.log("Verifying citizen at:", `${API_BASE_URL}/agency/verify`); // Debug log

        const res = await fetch(`${API_BASE_URL}/agency/verify`, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(data),
        });
        if (!res.ok) throw new Error('Verification failed');
        return await res.json();
    } catch (error) {
        console.error(error);
        return { is_fraud: false, match_details: null }; // Fail safe
    }
}

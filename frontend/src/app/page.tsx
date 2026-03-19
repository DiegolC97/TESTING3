'use client';

import { useEffect, useState } from 'react';
import styles from './page.module.css';

interface HealthResponse {
  status: string;
  message: string;
}

export default function Home() {
  const [apiStatus, setApiStatus] = useState<string>('Checking...');
  const [error, setError] = useState<string>('');

  useEffect(() => {
    const checkApiHealth = async () => {
      try {
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/health`);
        const data: HealthResponse = await response.json();
        setApiStatus(data.message);
      } catch (err) {
        setError('Failed to connect to API');
        setApiStatus('Disconnected');
      }
    };

    checkApiHealth();
  }, []);

  return (
    <main className={styles.main}>
      <div className={styles.container}>
        <h1 className={styles.title}>Welcome to TESTEST</h1>
        <p className={styles.description}>
          A full-stack application built with Next.js, Python (FastAPI), and PostgreSQL
        </p>

        <div className={styles.statusCard}>
          <h2>API Status</h2>
          <p className={error ? styles.error : styles.success}>
            {error || apiStatus}
          </p>
        </div>

        <div className={styles.grid}>
          <a
            href="http://localhost:8000/docs"
            className={styles.card}
            target="_blank"
            rel="noopener noreferrer"
          >
            <h3>API Documentation →</h3>
            <p>Explore the FastAPI backend endpoints</p>
          </a>

          <a
            href="https://nextjs.org/docs"
            className={styles.card}
            target="_blank"
            rel="noopener noreferrer"
          >
            <h3>Next.js Docs →</h3>
            <p>Learn about Next.js features and API</p>
          </a>

          <a
            href="https://fastapi.tiangolo.com"
            className={styles.card}
            target="_blank"
            rel="noopener noreferrer"
          >
            <h3>FastAPI Docs →</h3>
            <p>Discover FastAPI documentation</p>
          </a>

          <a
            href="https://www.postgresql.org/docs"
            className={styles.card}
            target="_blank"
            rel="noopener noreferrer"
          >
            <h3>PostgreSQL Docs →</h3>
            <p>Learn about PostgreSQL database</p>
          </a>
        </div>
      </div>
    </main>
  );
}

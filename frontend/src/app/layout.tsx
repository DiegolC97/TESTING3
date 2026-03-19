import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'TESTEST',
  description: 'A full-stack application built with Next.js, Python, and PostgreSQL',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

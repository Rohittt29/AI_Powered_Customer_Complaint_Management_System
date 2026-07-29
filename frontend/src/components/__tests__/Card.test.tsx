/**
 * Component test for Card components.
 */
import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import React from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '../common/Card';

describe('Card', () => {
  it('renders children correctly', () => {
    render(<Card><div>Card Content</div></Card>);
    expect(screen.getByText('Card Content')).toBeInTheDocument();
  });

  it('renders a full card with header and content', () => {
    render(
      <Card>
        <CardHeader>
          <CardTitle>Test Title</CardTitle>
        </CardHeader>
        <CardContent>Body text</CardContent>
      </Card>
    );
    expect(screen.getByText('Test Title')).toBeInTheDocument();
    expect(screen.getByText('Body text')).toBeInTheDocument();
  });
});

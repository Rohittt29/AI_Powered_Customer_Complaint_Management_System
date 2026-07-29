import { test, expect } from '@playwright/test';

test.describe('End-to-End Complaint Flow', () => {
  test('User can log a complaint and view it in the dashboard', async ({ page }) => {
    // 1. Navigate to the app
    await page.goto('/');
    
    // Check header
    await expect(page.locator('header')).toContainText('QMS');

    // 2. Open AI Copilot to submit a complaint
    // Assuming there's a button to open copilot or it's visible
    const chatInput = page.getByPlaceholder(/Type a message/i);
    await expect(chatInput).toBeVisible();

    // 3. User logs complaint
    await chatInput.fill('The display on my new monitor is flickering constantly and it gives me a headache.');
    await page.keyboard.press('Enter');

    // 4. Wait for AI response
    // AI should reply confirming extraction
    await expect(page.locator('.chat-message-ai').last()).toContainText(/extracted/i, { timeout: 15000 });

    // 5. Check dashboard for the new complaint
    // Navigate to dashboard if not already there, or if it auto-updates, check the table
    // Assuming the table shows the complaint description or summary
    await expect(page.locator('table')).toContainText('monitor is flickering', { timeout: 10000 });
    
    // 6. Click on the complaint to view details
    await page.getByText('monitor is flickering').click();
    
    // 7. Verify details (risk assessment, sentiment)
    await expect(page.getByText('Risk Level:')).toBeVisible();
    await expect(page.getByText('Sentiment:')).toBeVisible();
  });
});

#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int average = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            int sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            int sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

            // Ensure that the sepia values do not exceed 255
            if (sepiaRed > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = sepiaRed;
            }

            if (sepiaGreen > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = sepiaGreen;
            }

            if (sepiaBlue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = sepiaBlue;
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE tmp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = tmp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Declaration of the variables.
    RGBTRIPLE copy[height][width];
    int i, j, k, l;
    int totalRed, totalGreen, totalBlue;
    int count;

    for (i = 0; i < height; i++)
    {
        for (j = 0; j < width; j++)
        {
            count = 0;
            totalRed = 0;
            totalGreen = 0;
            totalBlue = 0;

            // Nested loops for boundaries check.
            for (k = -1; k <= 1; k++)
            {
                for (l = -1; l <= 1; l++)
                {
                    int row = i + k;
                    int coloumn = j + l;

                    // Check if the selected pixel is with the boundaries.
                    if (row >= 0 && row < height && coloumn >= 0 && coloumn < width)
                    {
                        totalRed += image[row][coloumn].rgbtRed;
                        totalGreen += image[row][coloumn].rgbtGreen;
                        totalBlue += image[row][coloumn].rgbtBlue;
                        count++;
                    }
                }
            }

            // Calculating the average of each color.
            copy[i][j].rgbtRed = round((float) totalRed / count);
            copy[i][j].rgbtGreen = round((float) totalGreen / count);
            copy[i][j].rgbtBlue = round((float) totalBlue / count);
        }
    }

    // Copying the value to Copy Variable.
    for (i = 0; i < height; i++)
    {
        for (j = 0; j < width; j++)
        {
            image[i][j] = copy[i][j];
        }
    }
    return;
}

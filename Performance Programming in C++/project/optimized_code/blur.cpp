#include "headers/blur.h"

using namespace std;

vector < vector <float> > blur(vector < vector < float> > &grid, float blurring) {
	int height = grid.size();
	int width = grid[0].size();
	vector < vector <float> > newGrid(height, vector<float>(width, 0.0));

	float center, corner, adjacent;
	center = 1.0 - blurring;
	corner = blurring / 12.0;
	adjacent = blurring / 6.0;

  	static vector < vector <float> > window = {
		{corner, adjacent, corner},
		{adjacent, center, adjacent},
		{corner, adjacent, corner}
	};

	static vector <int> DX = {-1, 0, 1};
	static vector <int> DY = {-1, 0, 1};

	int i, j;
	int dx;
	int dy;
	int ii;
	int jj;
	int new_i;
	int new_j;

	for (i=0; i< height; i++ ) {
		for (j=0; j<width; j++ ) {
			for (ii=0; ii<3; ii++) {
				dy = DY[ii];
				for (jj=0; jj<3; jj++) {
					dx = DX[jj];
					new_i = (i + dy + height) % height;
					new_j = (j + dx + width) % width;
					newGrid[new_i][new_j] += grid[i][j] * window[ii][jj];
				}
			}
		}
	}

	return newGrid;
}

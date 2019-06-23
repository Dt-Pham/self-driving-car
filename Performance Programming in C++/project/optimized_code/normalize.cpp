#include "headers/normalize.h"
#include <numeric>
using namespace std;

vector< vector<float> > normalize(vector< vector <float> > &grid) {
	float total = 0.0;
	for (auto &row : grid) {
		total = accumulate(row.begin(), row.end(), total);
	}

	vector< vector<float> > newGrid(grid.size(), vector<float>(grid[0].size()));

	int i;
	int j;
	for (i = 0; i < grid.size(); i++) {
		for (j = 0; j < grid[0].size(); j++) {
			newGrid[i][j] = grid[i][j] / total;
		}
	}

	return newGrid;
}

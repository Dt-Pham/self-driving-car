#include "headers/initialize_beliefs.h"

using namespace std;

vector< vector <float> > initialize_beliefs(vector< vector <char> > &grid) {
	int height = grid.size();
	int width = grid[0].size();

  	float prob_per_cell = 1.0 / ( (float) height * width) ;

	return vector<vector<float>>(height, vector<float>(width, prob_per_cell));
}
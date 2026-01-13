#include <ios>
#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

typedef long long ll;

ll solve(vector<vector<ll>> &field, vector<vector<ll>> &oldField,
         vector<vector<ll>> &maxStartingHere, ll N, ll K, ll rowChanged,
         ll colChanged, ll previousBest) {
  ll maxSum = 0;

  ll increase =
      field[rowChanged][colChanged] - oldField[rowChanged][colChanged];

  ll startI = max(rowChanged - K + 1, 0LL);
  ll startJ = max(colChanged - K + 1, 0LL);

  for (ll i = startI; i <= rowChanged; i++) {
    for (ll j = startJ; j <= colChanged; j++) {
      maxStartingHere[i][j] += increase;

      maxSum = max(maxSum, maxStartingHere[i][j]);
    }
  }

  return max(maxSum, previousBest);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  ll N, K, Q;
  cin >> N >> K >> Q;

  vector<vector<ll>> field(N, std::vector<ll>(N, 0));
  vector<vector<ll>> oldField(N, std::vector<ll>(N, 0));
  vector<vector<ll>> maxStartingHere(N, std::vector<ll>(N, 0));
  ll previousBest = 0;

  for (int i = 0; i < Q; i++) {
    ll row, col, val;
    cin >> row >> col >> val;

    oldField[row - 1][col - 1] = field[row - 1][col - 1];
    field[row - 1][col - 1] = val;

    previousBest = solve(field, oldField, maxStartingHere, N, K, row - 1,
                         col - 1, previousBest);

    cout << previousBest << "\n";
  }
}

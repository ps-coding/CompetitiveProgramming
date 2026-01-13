#include <ios>
#include <iostream>
#include <math.h>

using namespace std;

typedef long long ll;

ll solve(ll A, ll B, ll cA, ll cB, ll fA) {
  ll toTransfer = B - (B % cB);
  B -= toTransfer;
  A += toTransfer / cB * cA;

  if (A >= fA)
    return 0;

  if (cA >= cB) {
    ll bWasted = cB - (B % cB) - 1;

    return fA - A + bWasted;
  } else {
    ll fB = (long long)ceil(((long double)(fA) - (long double)(A)) /
                            ((long double)(cA))) *
            cB;

    ll finalA = A + (fB / cB * cA);

    if (finalA - cA + 1 >= fA) {
      return fB - B;
    } else {
      return fB - B + (fA - (finalA - cA + 1));
    }
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  ll T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    ll A, B, cA, cB, fA;

    cin >> A >> B >> cA >> cB >> fA;

    cout << solve(A, B, cA, cB, fA) << "\n";
  }
}

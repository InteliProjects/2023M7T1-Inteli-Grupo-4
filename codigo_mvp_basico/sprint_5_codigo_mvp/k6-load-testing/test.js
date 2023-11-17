import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  vus: 1000,
  duration: '30s',
  ext: {
    loadimpact: {
      // Project: Stress Test Loja Stone
      projectID: 3662241,
      // Test runs with the same name groups test runs together.
      name: 'Test (04/10/2023-15:18:44)',
    },
  },
};

export default function () {
  http.get('<URL_A_SER_TESTADA>');
  sleep(1);
}

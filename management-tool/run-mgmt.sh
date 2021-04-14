#!/bin/bash
docker run -it -p 3000:5000 \
	--name management-tool \
	-e REACT_APP_ARROWHEAD_SR_URL=https://127.0.0.1:8443 \
	-e REACT_APP_ARROWHEAD_AUTH_URL=https://127.0.0.1:8445 \
	-e REACT_APP_ARROWHEAD_ORCH_URL=https://127.0.0.1:8441 \
	-e REACT_APP_ARROWHEAD_GK_URL=https://127.0.0.1:8449 \
	-e REACT_APP_ARROWHEAD_GW_URL=https://127.0.0.1:8453 \
	-e REACT_APP_ARROWHEAD_EH_URL=https://127.0.0.1:8455 \
	--rm -d \
	svetlint/management-tool

FROM quay.io/condaforge/miniforge3:24.11.3-2

COPY environment.yml /opt/simula/environment.yml
COPY start.sh /opt/simula/start.sh
COPY UHI_Fortaleza_2024_pivoted.csv /opt/simula/UHI_Fortaleza_2024_pivoted.csv

RUN chmod +x /opt/simula/start.sh

RUN set -e && \
    export PIP_ROOT_USER_ACTION=ignore && \
    . /opt/conda/etc/profile.d/conda.sh && \
    mamba env create -f /opt/simula/environment.yml && \
    mamba clean -afy && \

ENTRYPOINT ["/bin/bash", "-c", ". /opt/simula/start.sh && exec \"$@\"", "--"]
CMD ["/bin/bash"]

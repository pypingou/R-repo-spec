%global packname  ddepn
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.2
Release:          1%{?dist}
Summary:          Dynamic Deterministic Effects Propagation Networks: Infer signalling networks for timecourse RPPA data.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graph R-Rgraphviz R-KEGGgraph R-RBGL R-genefilter R-gam R-lattice R-coda R-gplots 

BuildRequires:    R-devel tex(latex) R-graph R-Rgraphviz R-KEGGgraph R-RBGL R-genefilter R-gam R-lattice R-coda R-gplots 

%description
DDEPN (Dynamic Deterministic Effects Propagation Networks): Infer
signalling networks for timecourse data. Given a matrix of high-throughput
genomic or proteomic timecourse data, generated after external
perturbation of the biological system, DDEPN models the time-dependent
propagation of active and passive states depending on a network structure.
Optimal network structures given the experimental data are reconstructed.
Two network inference algorithms can be used: inhibMCMC, a Markov Chain
Monte Carlo sampling approach and GA, a Genetic Algorithm network
optimisation. Inclusion of prior biological knowledge can be done using
different network prior models.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.2-1
- initial package for Fedora
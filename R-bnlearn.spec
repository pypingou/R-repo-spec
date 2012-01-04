%global packname  bnlearn
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.7
Release:          1%{?dist}
Summary:          Bayesian network structure learning, parameter learning and inference

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

%description
Bayesian network structure learning (via constraint-based, score-based and
hybrid algorithms), parameter learning (via ML and Bayesian estimators)
and inference.  This package implements the Grow-Shrink (GS) algorithm,
the Incremental Association (IAMB) algorithm, the Interleaved-IAMB
(Inter-IAMB) algorithm, the Fast-IAMB (Fast-IAMB) algorithm, the Max-Min
Parents and Children (MMPC) algorithm, the ARACNE and Chow-Liu algorithms,
the Hill-Climbing (HC) greedy search algorithm, the Tabu Search (TABU)
algorithm, the Max-Min Hill-Climbing (MMHC) algorithm and the two-stage
Restricted Maximization (RSMAX2) algorithm for both discrete and Gaussian
networks, along with many score functions and conditional independence
tests.  Some utility functions (model comparison and manipulation, random
data generation, arc orientation testing, simple and advanced plots) are
included, as well as support for parameter estimation and inference,
conditional probability queries and cross-validation.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.7-1
- initial package for Fedora
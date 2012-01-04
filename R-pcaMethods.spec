%global packname  pcaMethods
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.40.0
Release:          1%{?dist}
Summary:          A collection of PCA methods.

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-MASS R-pls R-methods R-Rcpp 


BuildRequires:    R-devel tex(latex) R-Biobase R-MASS R-pls R-methods R-Rcpp



%description
Provides Bayesian PCA, Probabilistic PCA, Nipals PCA, Inverse Non-Linear
PCA and the conventional SVD PCA. A cluster based method for missing value
estimation is included for comparison. BPCA, PPCA and NipalsPCA may be
used to perform PCA on incomplete data as well as for accurate missing
value estimation. A set of methods for printing and plotting the results
is also provided. All PCA methods make use of the same data structure
(pcaRes) to provide a unique interface to the PCA results. Initiated at
the Max-Planck Institute for Molecular Plant Physiology, Golm, Germany.
Now developed at CAS-MPG Partner Institute for Computational Biology
(PICB) Shanghai, P.R. China and RIKEN Plant Science Center, Yokohama

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.40.0-1
- initial package for Fedora
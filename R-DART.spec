%global packname  DART
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Denoising Algorithm based on Relevance network Topology

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-igraph 

BuildRequires:    R-devel tex(latex) R-igraph 

%description
Denoising Algorithm based on Relevance network Topology (DART) is an
algorithm designed to evaluate the consistency of prior information
molecular signatures (e.g in-vitro perturbation expression signatures) in
independent molecular data (e.g gene expression data sets). If consistent,
a pruning network strategy is then used to infer the activation status of
the molecular signature in individual samples.

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
%doc %{rlibdir}/DART/html
%doc %{rlibdir}/DART/DESCRIPTION
%{rlibdir}/DART/R
%{rlibdir}/DART/data
%{rlibdir}/DART/help
%{rlibdir}/DART/INDEX
%{rlibdir}/DART/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora
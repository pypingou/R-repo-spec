%global packname  iFad
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          An integrative factor analysis model for drug-pathway association inference

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rlab R-MASS R-coda R-ROCR 


BuildRequires:    R-devel tex(latex) R-Rlab R-MASS R-coda R-ROCR



%description
This package implements a bayesian sparse factor model for the joint
analysis of paired datasets, one is the gene expression dataset and the
other is the drug sensitivity profiles, measured across the same panel of
samples, e.g., cell lines. Prior knowledge about gene-pathway associations
can be easily incorporated in the model to aid the inference of
drug-pathway associations.

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0-1
- initial package for Fedora
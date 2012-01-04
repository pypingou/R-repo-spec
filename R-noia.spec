%global packname  noia
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.94.1
Release:          1%{?dist}
Summary:          Implementation of the Natural and Orthogonal InterAction (NOIA) model

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
The NOIA model, as described extensively in Alvarez-Castro & Carlborg
(2007), is a framework facilitating the estimation of genetic effects and
genotype-to-phenotype maps. This package provides the basic tools to
perform linear and multilinear regressions from real populations (provided
the phenotype and the genotype of every individuals), estimating the
genetic effects from different reference points, the genotypic values, and
the decomposition of genetic variances in a multi-locus, 2 alleles system.
This package is presented in Le Rouzic & Alvarez-Castro (2008).

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
%doc %{rlibdir}/noia/DESCRIPTION
%doc %{rlibdir}/noia/html
%{rlibdir}/noia/R
%{rlibdir}/noia/NAMESPACE
%{rlibdir}/noia/Meta
%{rlibdir}/noia/data
%{rlibdir}/noia/help
%{rlibdir}/noia/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.94.1-1
- initial package for Fedora
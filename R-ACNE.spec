%global packname  ACNE
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Affymetrix SNP probe-summarization using non-negative matrix factorization

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-R.methodsS3 R-R.oo R-matrixStats R-aroma.affymetrix R-MASS 

BuildRequires:    R-devel tex(latex) R-R.methodsS3 R-R.oo R-matrixStats R-aroma.affymetrix R-MASS 

%description
Package for NMF summarization of SNP probes.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.0-1
- initial package for Fedora
%global packname  FIAR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4
Release:          1%{?dist}
Summary:          Functional Integration Analysis in R

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lavaan R-Matrix R-boot R-accuracy R-np 


BuildRequires:    R-devel tex(latex) R-lavaan R-Matrix R-boot R-accuracy R-np



%description
Contains DCM, (autoregressive) SEM, and multivariate Granger causality
tests for analyzing fMRI connectivity data.

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
%doc %{rlibdir}/FIAR/html
%doc %{rlibdir}/FIAR/DESCRIPTION
%doc %{rlibdir}/FIAR/CITATION
%{rlibdir}/FIAR/help
%{rlibdir}/FIAR/INDEX
%{rlibdir}/FIAR/data
%{rlibdir}/FIAR/Meta
%{rlibdir}/FIAR/R
%{rlibdir}/FIAR/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4-1
- initial package for Fedora
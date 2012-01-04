%global packname  multxpert
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Common Multiple Testing Procedures and Gatekeeping Procedures

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-stats R-mvtnorm 

%description
Implementation of commonly used p-value-based and parametric multiple
testing procedures (computation of adjusted p-values and simultaneous
confidence intervals) and parallel gatekeeping procedures based on the
methodology presented in the book "Multiple Testing Problems in
Pharmaceutical Statistics" (edited by Alex Dmitrienko, Ajit C. Tamhane and
Frank Bretz) published by Chapman and Hall/CRC Press 2009.

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
%doc %{rlibdir}/multxpert/html
%doc %{rlibdir}/multxpert/DESCRIPTION
%{rlibdir}/multxpert/help
%{rlibdir}/multxpert/NAMESPACE
%{rlibdir}/multxpert/R
%{rlibdir}/multxpert/INDEX
%{rlibdir}/multxpert/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora
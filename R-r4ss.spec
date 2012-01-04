%global packname  r4ss
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.16
Release:          1%{?dist}
Summary:          R code for Stock Synthesis

Group:            Applications/Engineering 
License:          MIT License
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-tcltk R-coda 


BuildRequires:    R-devel tex(latex) R-tcltk R-coda



%description
Functions for reading output, plotting, exploring and manipulating input
files for Richard Methot's Stock Synthesis fisheries stock assessment
modeling platform.

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
%doc %{rlibdir}/r4ss/DESCRIPTION
%doc %{rlibdir}/r4ss/html
%{rlibdir}/r4ss/Meta
%{rlibdir}/r4ss/INDEX
%{rlibdir}/r4ss/R
%{rlibdir}/r4ss/NAMESPACE
%{rlibdir}/r4ss/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.16-1
- initial package for Fedora
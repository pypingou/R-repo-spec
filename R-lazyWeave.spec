%global packname  lazyWeave
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.1.0
Release:          1%{?dist}
Summary:          LaTeX Wrappers for R Users

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Hmisc 

BuildRequires:    R-devel tex(latex) R-Hmisc 

%description
Provides the functionality to write LaTeX code from within R without
having to learn LaTeX.

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
%doc %{rlibdir}/lazyWeave/DESCRIPTION
%doc %{rlibdir}/lazyWeave/html
%{rlibdir}/lazyWeave/data
%{rlibdir}/lazyWeave/help
%{rlibdir}/lazyWeave/INDEX
%{rlibdir}/lazyWeave/R
%{rlibdir}/lazyWeave/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.0-1
- initial package for Fedora
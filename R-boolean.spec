%global packname  boolean
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0.2
Release:          1%{?dist}
Summary:          Boolean Binary Response Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Zelig 

BuildRequires:    R-devel tex(latex) R-Zelig 

%description
This package implements a partial-observability procedure for testing
Boolean hypotheses that generalizes the binary response GLM.

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
%doc %{rlibdir}/boolean/DESCRIPTION
%doc %{rlibdir}/boolean/html
%{rlibdir}/boolean/NAMESPACE
%{rlibdir}/boolean/INDEX
%{rlibdir}/boolean/Meta
%{rlibdir}/boolean/help
%{rlibdir}/boolean/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.2-1
- initial package for Fedora
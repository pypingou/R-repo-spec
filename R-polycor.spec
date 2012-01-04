%global packname  polycor
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.7.8
Release:          1%{?dist}
Summary:          Polychoric and Polyserial Correlations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvtnorm R-sfsmisc 

BuildRequires:    R-devel tex(latex) R-mvtnorm R-sfsmisc 

%description
Computes polychoric and polyserial correlations by quick "two-step"
methods or ML, optionally with standard errors; tetrachoric and biserial
correlations are special cases.

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
%doc %{rlibdir}/polycor/html
%doc %{rlibdir}/polycor/DESCRIPTION
%{rlibdir}/polycor/R
%{rlibdir}/polycor/help
%{rlibdir}/polycor/INDEX
%{rlibdir}/polycor/NAMESPACE
%{rlibdir}/polycor/Meta
%{rlibdir}/polycor/CHANGES

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.8-1
- initial package for Fedora